//-----------------------------------------------------------------------------
// Title         : <TFILEN>
// Project       : fabrico1f
//-----------------------------------------------------------------------------
// File          : <TFILE>
// Author        : MTVL - Duc
// Created       : 09-05-2018
// History
//-----------------------------------------------------------------------------
// MODULE NAME : <TFILEN>
// Description : 
// v0.0  09-05-2018
//-----------------------------------------------------------------------------
// Copyright (c) 2018 by Marvell Semiconductor Inc. This model is the 
// confidential and  proprietary property of Marvell Semiconductor Inc. and 
// the possession or use of this file requires a written license from Marvell 
// Semiconductor Inc..
//-----------------------------------------------------------------------------

`define ANOTHER in_wpat3

module legacy_direct (
  clk, rstn,
  in0, in1,
  out0, out1,
  `ifdef ENTHIS
  in_wpat1,
  `elsif ENTHAT
  in_wpat2,
  `else
  `ANOTHER,
  `endif
  out_wpat1, out_wpat2
);

parameter AW=4;
input clk, rstn;
input [AW-1:0] in0;
input wire [7:0] in1;
output wire [AW+11:8] out0;
output [7:4] out1;
reg [7:4] out1;

`ifdef ENTHIS
input [7:3] in_wpat1;
wire [7:3] in_wpat1;
`define TBU in_wpat1[7:5]
`elsif ENTHAT
input [15:12] in_wpat2;
`define TBU in_wpat2[14:12]
`else
input [4:0] `ANOTHER;
`define TBU `ANOTHER[4:1]
`endif

`define CLKEDGE(c,r) (posedge c or negedge r)

output [3:1] out_wpat1;
output reg [5:3] out_wpat2;

`ifndef ENTHIS
    `ifndef ENTHAT
        `include "incthis.inc"
    `else
        assign out_wpat1 = 'h1;
    `endif
`else
    assign out_wpat1 = 'b0;
    always @* out_wpat2 = 'b0;
`endif

wire [4:0] wirename1 = `TBU & in1[AW-1:3];

`define ENCOND(s) (s && `TBU==0)

always @`CLKEDGE ( clk, rstn) begin
  if (rstn) out1 <= #0.1 4'b0;
  else if (`ENCOND(in0[2])) out1 <= #0.1 wirename1[3:1];
end

assign out0 = in1;


endmodule


