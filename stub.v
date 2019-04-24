module legacy_direct (
  input wire clk,
  input wire rstn,
  input wire [3:0] in0,
  input wire [7:0] in1,
  output wire [15:8] out0,
  output reg [7:4] out1,
  input wire [7:3] in_wpat1,
  output wire [3:1] out_wpat1,
  output reg [5:3] out_wpat2
);
  assign out0 = 8'b0;
  assign out1 = 4'b0;
  assign out_wpat1 = 3'b0;
  assign out_wpat2 = 3'b0;
endmodule
