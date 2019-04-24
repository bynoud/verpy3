
module modname #(parameter AW=4) (
  input ck, rstn,
  input [AW-1:0] in0,
  output [AW-1:0] out0
);

assign out0 = in0;

endmodule

