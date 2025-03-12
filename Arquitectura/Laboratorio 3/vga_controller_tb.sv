`timescale 10ns/1ns

module vga_controller_tb;

  logic clk_tb = 0;
  logic [8:0] sw_tb = 0;
  logic clk_en_25MHz_tb;
  logic [2:0] red_tb;
  logic [2:0] green_tb;
  logic [2:0] blue_tb;
  logic h_sync_tb;
  logic v_sync_tb;  

  vga_controller vga_controller1 (
    .clk(clk_tb), 
    .sw(sw_tb),
    .clk_en_25MHz(clk_en_25MHz_tb),
    .red(red_tb),
    .green(green_tb),
    .blue(blue_tb),
    .h_sync(h_sync_tb),
    .v_sync(v_sync_tb)
  );

  always #1 clk_tb = !clk_tb;

  initial begin
    $dumpfile("vga_controller_tb.vcd");
    $dumpvars(0,vga_controller_tb);
    sw_tb = 9'b000000000; // Black
    #1680000
    sw_tb = 9'b111000000; // Red
    #1680000
    sw_tb = 9'b000111000; // Green
    #1680000 $finish;
  end

endmodule