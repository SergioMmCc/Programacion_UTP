`timescale 1ns/100ps
// Escala de tiempo de 1 ns, resolucion de 100 ps

module mux4_1_tb;

    logic [1:0] A_tb = 0;
    logic [1:0] B_tb = 0;
    logic [1:0] C_tb = 0;
    logic [1:0] D_tb = 0;
    logic [1:0] S_tb = 0;
    logic [1:0] O_tb;

    mux4_1 mux1 (.A(A_tb), .B(B_tb), .C(C_tb), .D(D_tb), .S(S_tb), .O(O_tb));

    initial begin
        $dumpfile("mux4_1_tb.vcd");
        $dumpvars(0, mux4_1_tb);
        #10
            A_tb = 2'b01;
            B_tb = 2'b10;
            C_tb = 2'b11;
            D_tb = 2'b00;
            S_tb = 2'b00;
        #10
            A_tb = 2'b01;
            B_tb = 2'b10;
            C_tb = 2'b11;
            D_tb = 2'b00;
            S_tb = 2'b01;
        #10
            A_tb = 2'b01;
            B_tb = 2'b10;
            C_tb = 2'b11;
            D_tb = 2'b00;
            S_tb = 2'b10;
        #10
            A_tb = 2'b01;
            B_tb = 2'b10;
            C_tb = 2'b11;
            D_tb = 2'b00;
            S_tb = 2'b11;
        #10 $finish;
    end

endmodule