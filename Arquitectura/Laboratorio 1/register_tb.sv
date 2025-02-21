`timescale 1ns/100ps

module register_tb;

    logic clk_tb = 0;
    logic en_tb = 0;
    logic [31:0] D_tb = 0;
    logic [31:0] Q_tb;

    register register1 (.clk(clk_tb), .en(en_tb), .D(D_tb), .Q(Q_tb));

    always #10 clk_tb = !clk_tb;

    initial begin
        $dumpfile("register_tb.vcd");
        $dumpvars(0, register_tb);
        #20
            en_tb = 1;
            D_tb = 26;
        #20
            en_tb = 0;
            D_tb = 0;
        #80
            en_tb = 1;
            D_tb = 28;
        #20
            en_tb = 0;
            D_tb = 0;
        #20 $finish;
    end
endmodule