
module paramtest (
  a,b
);

parameter BW = AW -1;
parameter AW = 4;

input [AW-1:0] a;
output [BW-1:0] b;

assign b = a;

endmodule


