
assign out_wpat1 = out_wpat2[3] ? `ANOTHER[4:2]
                                : in1[7:5];
always @`CLKEDGE(clk, rstn)
    out_wpat2 <= #0.1 `ANOTHER;

