module mux4_1(
    input logic [1:0] A,
    input logic [1:0] B,
    input logic [1:0] C,
    input logic [1:0] D,
    input logic [1:0] S,
    output logic [1:0] O
);

assign O = S[1] ? (S[0] ? D : C) : (S[0] ? B : A);

endmodule