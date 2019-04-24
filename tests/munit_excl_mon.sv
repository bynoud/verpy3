//-----------------------------------------------------------------------------
// Title         : munit_excl_mon
// Project       : fabric12
//-----------------------------------------------------------------------------
// File          : munit_excl_mon.sv
// Author        : MTVL - Duc
// Created       : 12-03-2019
// History
//-----------------------------------------------------------------------------
// MODULE NAME : munit_excl_mon
// Description :
// v0.0  12-03-2019
//-----------------------------------------------------------------------------
// Copyright (c) 2019 by Marvell Semiconductor Inc. This model is the
// confidential and  proprietary property of Marvell Semiconductor Inc. and
// the possession or use of this file requires a written license from Marvell
// Semiconductor Inc..
//-----------------------------------------------------------------------------

`ifdef MUNIT_FUNC_COV_ON
`define _cpn(name, expr) cp_``name: coverpoint expr
`define _cpc(name, expr, cond) cp_``name: coverpoint expr iff (cond)
`define _cvc(name, expr, cond=1) cov_``name: cover property (@(posedge clk) disable iff (!rst_n && (cond)) expr)
`endif

module munit_excl_mon #(parameter IW=17, AW=23, MON=2) (
  // System
  input  wire clk,
  input  wire rst_n,

  input  wire [MON-1:0] mon_clr,  // reset the monitor to open

  input  wire           arvalid,
  input  wire           arready,
  input  wire [AW-1:0]  araddr,
  input  wire [IW-1:0]  arid,
  input  wire [7:0]     arlen,
  input  wire           arlock,
  input  wire [2:0]     arsize,

  input  wire           r_push,
  input  wire [IW-1:0]  rid,

  input  wire           awvalid,
  input  wire           awready,  // original ready, before being stall
  input  wire [AW-1:0]  awaddr,
  input  wire [IW-1:0]  awid,
  input  wire [7:0]     awlen,
  input  wire           awlock,
  input  wire [2:0]     awsize,
  input  wire [1:0]     awburst,

  input  wire           b_push,
  input  wire [IW-1:0]  bid,

  // exclusive decode
  output wire           awex_okay,
  output wire           stall_wr,   // stop AW
  output wire           stall_rd,   // stop AR

  output reg  [MON-1:0] mon_isclr   // 1 cycle pulse for each monitor

);

// monitors
reg  [MON-1:0] g_vld;
wire [MON-1:0] g_arid_hit;
wire [MON-1:0] g_free;
wire [MON-1:0] g_aw_hit;

genvar v;

assign awex_okay = |g_aw_hit;

wire aw_push = awvalid & awready & ~stall_wr;

wire awexcl_push = aw_push & awlock;
wire arexcl_push = arvalid & arlock & arready & ~stall_rd;

// all write outstanding
reg [5:0] wr_outs;  // support maximum 32 outstanding
always @(posedge clk or negedge rst_n) begin
  if (!rst_n)
    wr_outs <= #0.1 6'b0;
  else if (aw_push ^ b_push)
    wr_outs <= #0.1 wr_outs + (aw_push ? 6'h01 : 6'h3f/*-1*/ );
end

// Ex-Load pending is getting from each monitor status
reg [MON-1:0] g_exrd_pending;
wire exrd_pending = |g_exrd_pending;

// a normal Store whether overlapped is detected in each monitor
wire [MON-1:0] g_wr_overlap;
wire wr_overlap = |g_wr_overlap;

// saving ID of overlapped write to know when it done
reg [IW-1:0] id_overlap;
reg overlap_pending;
always @(posedge clk or negedge rst_n) begin
  if (!rst_n)
    overlap_pending <= #0.1 1'b0;
  else if (aw_push && wr_overlap)
    overlap_pending <= #0.1 1'b1;
  else if (b_push && overlap_pending && (bid==id_overlap))
    overlap_pending <= #0.1 1'b0;
end
always @(posedge clk) begin
  if (aw_push && wr_overlap) id_overlap <= #0.1 awid;
end

// to make sure execution order in MUNIT, stall AR when:
// (1) It's Ex-Load, and there's an Ex-Store or Overlapped-Store in same cycle
// (2) It's Ex-Load, and there's write-outstanding (DON'T need to know if it's going to be saved or not, simple design)
// (3) It's Ex-Load, and there's Ex-Store in same cycle (covered by 1), or there's Ex-Store on-going (covered by 2)
// (4) It's Ex-Load, and there's Overlapped-Store in same cycle (covered by 1), or there's Overlapped-Store on-going (covered by 2)
// (5) safe-gaurd, dont accept new ex-load hit an entry, if that entry load is ongoing
//     since we need keep track on-going ex-load to stall write
wire stall_rd_by_exover_store = arlock & (awvalid & (awlock | wr_overlap));
wire stall_rd_by_wr_outs = arlock & (|wr_outs);
wire stall_rd_by_hit_ongoing_exload = |(g_arid_hit & g_exrd_pending);
assign stall_rd = stall_rd_by_exover_store |
                  stall_rd_by_wr_outs |
                  stall_rd_by_hit_ongoing_exload;

// to make sure execution order in MUNIT, stall AW when:
// (1) It's normal-Store (and not Overlapped), and there's Ex-Load on same cycle or on-going
// (2) It's success Ex-Store, and there's Ex-Load outstanding. A failed Ex-Store go on normally, as it'll not changing the memory, racing is not a concern
//     -> failed-ex store cause problem for scoreboard to proper record
//        stall it should not take long, so simply just stall it
// (3) It's overlapped-Store, and there's Ex-Load outstanding
// (4) It's overlapped-Store, and there's another overlapped-Store is on-going
wire stall_wr_by_exload = ~awlock & ~wr_overlap & ((arvalid & arlock) | exrd_pending);
wire stall_wr_by_exstore_ldouts = awlock & exrd_pending;
wire stall_wr_by_olstore_ldouts = wr_overlap & (exrd_pending | overlap_pending);
assign stall_wr = wr_outs[5] |
                  stall_wr_by_exload |
                  stall_wr_by_exstore_ldouts |
                  stall_wr_by_olstore_ldouts;


// Monitor is cleared pulse. This is not include monitor clear by register setting
wire [MON-1:0] g_vld_clr_pulse;
always @(posedge clk or negedge rst_n) begin
  if   (!rst_n) mon_isclr <= #0.1 2'b0;
  else          mon_isclr <= #0.1 g_vld_clr_pulse;
end

generate
for (v=0; v<MON; v=v+1) begin : monitors_gen
  //reg [AW-1:0]  m_add ;
  //reg [IW-1:0]  m_id  ;
  //reg [7:0]     m_len ;
  //reg [2:0]     m_size;
  wire [AW-1:0]  m_add ;
  wire [IW-1:0]  m_id  ;
  wire [7:0]     m_len ;
  wire [2:0]     m_size;

  assign g_arid_hit[v] = g_vld[v] && (arid == m_id);


  // monitor saved info: if ARID hit one of entry,
  // or there's free entry to save the new one
  wire m_wren = arexcl_push & ((|g_arid_hit) ? g_arid_hit[v] : g_free[v]);

  //always @(posedge clk) begin
  //  if (m_wren) begin
  //    m_add  <= #0.1 araddr;
  //    m_id   <= #0.1 arid;
  //    m_len  <= #0.1 arlen;
  //    m_size <= #0.1 arsize;
  //  end
  //end
  munit_excl_mon_dffinst #(AW+3) dff_addsize (
    .clk(clk), .enb(m_wren),
    .din({araddr, arsize}),
    .dout({m_add, m_size})
  );
  munit_excl_mon_dffinst #(IW+8) dff_idlen (
    .clk(clk), .enb(m_wren),
    .din({arid, arlen}),
    .dout({m_id, m_len})
  );

  // monitor valid
  // set when: it's going to store valid data
  // clear when ex-AW come:
  //   - Ex-Store hit any entry, and this entry is within 64Bytes block
  //   - Normal-Store, with address range cover 64Bytes block of this entry
  wire   m_awblock_hit = g_vld[v] && (m_add[AW-1:6] == awaddr[AW-1:6]);  // 64Bytes
  wire   m_awexhit = awlock & awex_okay & m_awblock_hit;

  assign g_vld_clr_pulse[v] = aw_push & (m_awexhit | g_wr_overlap[v]);

  always @(posedge clk or negedge rst_n) begin
    if (!rst_n)
      g_vld[v] <= #0.1 1'b0;
    else if (g_vld_clr_pulse[v] | mon_clr[v])
      g_vld[v] <= #0.1 1'b0;
    else if (m_wren)
      g_vld[v] <= #0.1 1'b1;
  end

  // Ex-Store hit an try when ALL bits matched
  assign g_aw_hit[v] = m_awblock_hit
                     && (m_add[5:0] == awaddr[5:0])
                     && (m_id == awid)
                     && (m_len == awlen)
                     && (m_size == awsize);
                     

  // free monitor, it's one hot, may be all 0
  if (v==0) begin : mon0_gen
    assign g_free[v] = ~g_vld[v];
  end else begin : monN_gen
    assign g_free[v] = ~g_vld[v] & (&g_vld[v-1:0]);
  end

  // record outstanding Ex-Load
  always @(posedge clk or negedge rst_n) begin
    if (!rst_n)
      g_exrd_pending[v] <= #0.1 1'b0;
    else if (r_push && g_exrd_pending[v] && (rid == m_id))
      g_exrd_pending[v] <= #0.1 1'b0;
    else if (m_wren)
      g_exrd_pending[v] <= #0.1 1'b1;
  end

  // normal Store overlap checking, 1-cycle calculated
  wire m_addoverlap;
  assign g_wr_overlap[v] = ~awlock & m_addoverlap & g_vld[v];

  munit_excl_mon_addrange_cal #(.AW(AW))
    i_overlap_chk (
    .addr        ( awaddr       ),  //I\munit_excl_mon_addrange_cal[AW-1:0]
    .burst       ( awburst      ),  //I\munit_excl_mon_addrange_cal[1:0]
    .len         ( awlen        ),  //I\munit_excl_mon_addrange_cal[7:0]
    .size        ( awsize       ),  //I\munit_excl_mon_addrange_cal[2:0]
    .mark_addr   ( m_add        ),  //I\munit_excl_mon_addrange_cal[AW-1:0]
    .hit         ( m_addoverlap )   //O\munit_excl_mon_addrange_cal
  );

  `ifdef MUNIT_FUNC_COV_ON
  covergroup cg_excl_mon @(posedge clk);
    `_cpc(entry_arhit, g_arid_hit[v], arexcl_push);
    `_cpc(entry_awhit, {|g_aw_hit, g_aw_hit[v], m_awblock_hit}, awexcl_push) {
      bins awhit_me = {3'b111};
      bins awhit_other_sameblk = {3'b101};
      bins awhit_other_diffblk = {3'b110};
    }
    `_cpc(entry_set_free, g_free[v], m_wren);
    `_cpc(entry_set_hit, g_arid_hit[v], m_wren);
    `_cpc(entry_clr_exhit, m_awexhit, aw_push);
    `_cpc(entry_clr_overlap, {|g_wr_overlap, g_wr_overlap[v], m_awblock_hit}, aw_push) {
      bins over_me = {3'b111};
      bins over_other_sameblk = {3'b101};
      bins over_other_diffblk = {3'b110};
    }
    `_cpc(hit_cond, {m_add == awaddr,
                     m_id == awid,
                     m_len == awlen,
                     m_size == awsize}, g_vld[v] & aw_push) {
      bins b_onecold[] = {4'hf, 4'h7, 4'hb, 4'hd, 4'he};
    }
  endgroup
  initial begin
    cg_excl_mon u_cg_excl_mon;
    u_cg_excl_mon = new();
  end

  // cover sequence
  sequence seq_exld_exstr;
    (m_wren) ##1
    ((!m_wren) throughout (##[1:$] aw_push ##0 m_awexhit));
  endsequence
  
  sequence seq_exld_ovstr(overme, sameblk);
    (m_wren) ##1
    ((!m_wren) throughout (##[1:$] aw_push ##0 (|g_wr_overlap) ##0
      (g_wr_overlap[v]==overme) ##0 (m_awblock_hit==sameblk)));
  endsequence

  sequence seq_exld_exlddup_exstrf_exstrok;
    logic [AW-1:0] add;
    (m_wren,add=araddr) ##1
    ((!aw_push) throughout (##[1:$] m_wren ##0 g_arid_hit[v] ##0 (araddr!==add))) ##1
    ((!m_wren) throughout (##[1:$] aw_push ##0 !awex_okay)) ##1
    ((!m_wren) throughout (##[1:$] aw_push ##0 awex_okay));
  endsequence

  sequence seq_hit_another(sameblk);
    (m_wren) ##1
    ((!m_wren) throughout (##[1:$] aw_push ##0 awex_okay ##0 (m_awexhit==sameblk)));
  endsequence
  
  `_cvc(exld_free_exstr, (m_wren&g_free[v]) |-> seq_exld_exstr);
  `_cvc(exld_dup_exstr, (m_wren&g_arid_hit[v]) |-> seq_exld_exstr);
  `_cvc(exld_ovstr_myself, m_wren |-> seq_exld_ovstr(1,1));
  `_cvc(exld_ovstr_other_sameblk, m_wren |-> seq_exld_ovstr(0,1));
  `_cvc(exld_ovstr_other_diffblk, m_wren |-> seq_exld_ovstr(0,0));
  `_cvc(exld_dup, m_wren |-> seq_exld_exlddup_exstrf_exstrok);
  `_cvc(exstr_hit_another_sameblk, m_wren |-> seq_hit_another(1));
  `_cvc(exstr_hit_another_diffblk, m_wren |-> seq_hit_another(0));
  `endif


end
endgenerate


// ==============================================================================
// Functional coverage
// ==============================================================================

`ifdef MUNIT_FUNC_COV_ON
covergroup cg_excl_read_common @(posedge clk iff (arvalid && arready));
  //`_cpn(lock_stall, {arlock, stall_rd});// only stall when  arlock request
  `_cpn(lock, arlock);// only stall when  arlock request
  // cover one hot case, to make sure each one is covered approriated
  `_cpc(stall_conds, {stall_rd_by_exover_store & ~awlock,
                      stall_rd_by_exover_store & ~wr_overlap,
                      stall_rd_by_wr_outs,
                      stall_rd_by_hit_ongoing_exload}, arlock) {
    bins b_onehot[] = {4'b0, 4'b1000, 4'b0100, 4'b0010, 4'b0001};
  }
  // where to save in stack
  `_cpc(where_to_save, {|g_arid_hit, |g_free}, arexcl_push) {
    bins b_onehot[] = {2'b00, 2'b01, 2'b10};
  }
endgroup

covergroup cg_excl_write_common @(posedge clk iff (awvalid && awready));
  `_cpn(lock_stall, {awlock, stall_wr});
  `_cpn(overlapped, wr_overlap);
  `_cpn(stall_conds, {wr_outs[5],
                      stall_wr_by_exload & ~exrd_pending,
                      stall_wr_by_exload & ~(arvalid & arlock),
                      stall_wr_by_exstore_ldouts,
                      stall_wr_by_olstore_ldouts & ~exrd_pending,
                      stall_wr_by_olstore_ldouts & ~overlap_pending}) {
    bins b_onehot[] = {6'h0, 6'h20, 6'h10, 6'h08, 6'h04, 6'h02, 6'h01};
  }
  `_cpc(overlap_size, awsize, wr_overlap) {
    bins b_allow[] = {[0:5]};
  }
  `_cpc(overlap_len, awlen, wr_overlap) {
    bins b_allow[] = {[0:15]};
  }
  `_cpc(overlap_burst, awburst, wr_overlap) {
    bins b_allow[] = {2'b01, 2'b10};
  }
endgroup

//sequence seq_exld_exstr;
//  logic [IW-1:0] id;
//  (arexcl_push,id=arid) ##1
//  ((!arexcl_push) throughout (##[1:$] awexcl_push ##0 (awid===id)));
//endsequence
//
//sequence seq_ex_load_id_dup;
//  logic [IW-1:0] id;
//  (arexcl_push,id=arid) ##1 ~awexcl_push[*] ##0 arexcl_push[->1] ##0 (arid===id);
//endsequence
//
//cover_exld_str: cover property (@(posedge clk) disable iff (!rst_n) seq_ex_load_store);


initial begin
  cg_excl_read_common  u_cg_excl_read_common;
  cg_excl_write_common u_cg_excl_write_common;
  u_cg_excl_read_common = new();
  u_cg_excl_write_common = new();
end

`undef _cpc
`undef _cpn
`undef _cvc
`endif // MUNIT_FUNC_COV_ON

endmodule

// ECO need instant clock gate in design?
module munit_excl_mon_dffinst #(parameter DW=32) (
  input clk, enb,
  input [DW-1:0] din,
  output [DW-1:0] dout
);
wire gclk;
genvar v;
//strange, it fix TX as 1?? m_tlatnca _mi_cg (.e(enb), .ck(clk), .eck(gclk));
m_tlatntsca _mi_cg (.se(1'b0), .e(enb), .ck(clk), .eck(gclk));
generate
for (v=0; v<DW; v=v+1) begin : dffinst_gen
  m_dffq idff (.q(dout[v]), .d(din[v]), .cp(gclk));
end
endgenerate
endmodule


