`timescale 1ns/100ps
// Escala de tiempo de 1 ns, resolucion de 100 ps

module mux_tb;

    logic A_tb = 0;
    logic B_tb = 0;
    logic S_tb = 0;
    logic O_tb; // No inicializar la salida porque puedo crear un conflicto

    mux mux1 (.A(A_tb), .B(B_tb), .S(S_tb), .O(O_tb));

    initial begin
        $dumpfile("mux_tb.vcd");
        $dumpvars(0, mux_tb);
        #10 // Cada #10 corresponde a 10 ns
            A_tb = 1;
            B_tb = 1;
            S_tb = 0;
        #10
            A_tb = 1;
            B_tb = 0;
            S_tb = 1;
        #10
            A_tb = 0;
            B_tb = 1;
            S_tb = 1;
        #10 $finish;
    end

endmodule