`timescale 1ns/100ps

module kb_controller_tb;

    logic ps2_clk_tb = 1;
    logic ps2_data_tb = 1;
    logic [7:0] leds_tb;

    PS2 ps2 (.ps2_clk(ps2_clk_tb), .ps2_data(ps2_data_tb), .leds(leds_tb));

    always #50 ps2_clk_tb = ~ps2_clk_tb;
    initial begin
        $dumpfile("kb_controller_tb.vcd");
        $dumpvars(0, kb_controller_tb);

        #125
            ps2_data_tb = 1;
        #100
            ps2_data_tb = 0; // Inicio
        #100
            ps2_data_tb = 1; // Bit 0
        #100
            ps2_data_tb = 0; // Bit 1
        #100
            ps2_data_tb = 0; // Bit 2
        #100
            ps2_data_tb = 1; // Bit 3
        #100
            ps2_data_tb = 0; // Bit 4
        #100
            ps2_data_tb = 0; // Bit 5
        #100
            ps2_data_tb = 1; // Bit 6
        #100
            ps2_data_tb = 0; // Bit 7
        #100
            ps2_data_tb = 0; // Paridad
        #100
            ps2_data_tb = 1; // Stop
        #100
            ps2_data_tb = 1;
        #100
            ps2_data_tb = 1;
        #100
            ps2_data_tb = 1;
        #100 $finish;
    end
endmodule