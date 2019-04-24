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

module legacyver (
  clk, rstn,
  in0, in1,
  out0, out1,
  in_wpat1, in_wpat2,
  out_wpat1, out_wpat2
);

parameter AW=4;
input clk, rstn;
input [AW-1:0] in0;
input wire [7:0] in1;
output wire [AW+11:8] out0;
output [7:4] out1;
reg [7:4] out1;


input [7:3] in_wpat1;
wire [7:3] in_wpat1;
input [15:12] in_wpat2;

output [3:1] out_wpat1;
output reg [5:3] out_wpat2;

wire [4:0] wirename1 = in_wpat1[3] ? in_wpat1[7:5] : in1[AW-1:3];
wire [3:2] wirename2 = in_wpat1[4] ? in0[3:2] :
                       (in_wpat2==4) ? in1[3:2] : in1[7:5];
                        

always @(posedge clk or negedge rstn) begin
  if (rstn) out1 <= #0.1 4'b0;
  else if (in0[2]) out1 <= #0.1 wirename1[3:1];
end

assign out0 = in1;

legacy_direct #(6) i_direct (
  .clk(clk), .rstn(rstn), .in0(in0), .out0(out_wpat1));

  modname #(6) i_mod0 (clk, rstn, in1[7:4], out0[3:0]);
  modname #(8) i_mod1 (clk, rstn, in1, out0);

endmodule


