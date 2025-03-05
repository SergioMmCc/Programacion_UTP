`timescale 1ns/100ps

module vga_controller_tb;
    logic clk_tb = 0;
    logic [8:0] sw_tb = 0;
    logic clk_en_25MHz_tb;
    logic [2:0] red_tb;
    logic [2:0] green_tb;
    logic [2:0] blue_tb;
    logic hsync_tb;
    logic vsync_tb;

    vga_controller vga_controller1 (
        .clk(clk_tb),
        .sw(sw_tb),
        .clk_en_25MHz(clk_en_25MHz_tb),
        .red(red_tb),
        .green(green_tb),
        .blue(blue_tb),
        .hsync(hsync_tb),
        .vsync(vsync_tb)
    );

    always #1 clk_tb = !clk_tb;

    initial begin
        $dumpfile("vga_controller_tb.vcd");
        $dumpvars(0, vga_controller_tb);

        sw_tb = 9'b000000000; // Black
        #840000
        sw_tb = 9'b000000111; // Red
        #840000
        sw_tb = 9'b000111000; // Green
        #840000 $finish;
    end

endmodule