`timescale 1ns/100ps
// Escala de tiempo de 1 ns, resolucion de 100 ps

module decodificador_tb;

    logic [2:0] D_tb = 0;
    logic en_tb = 0;
    logic [7:0] Q_tb;

    decodificador dec1 (.D(D_tb), .en(en_tb), .Q(Q_tb));

    initial begin
        $dumpfile("decodificador_tb.vcd");
        $dumpvars(0, decodificador_tb);
        #10
            D_tb = 3'b000;
            en_tb = 1;
        #10
            D_tb = 3'b001;
            en_tb = 1;
        #10
            D_tb = 3'b010;
            en_tb = 1;
        #10
            D_tb = 3'b011;
            en_tb = 1;
        #10
            D_tb = 3'b100;
            en_tb = 1;
        #10
            D_tb = 3'b101;
            en_tb = 1;
        #10
            D_tb = 3'b110;
            en_tb = 1;
        #10
            D_tb = 3'b111;
            en_tb = 1;
        #10
            D_tb = 3'b000;
            en_tb = 1;
        #10
            D_tb = 3'b001;
            en_tb = 1;
        #10
            D_tb = 3'b010;
            en_tb = 1;
        #10 $finish;
    end

endmodule