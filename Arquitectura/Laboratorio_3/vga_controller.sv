module vga_controller #(
  parameter H_BACK_PORCH = 48,      // Horizontal back porch
  parameter H_DISPLAY_TIME = 640,   // Horizontal display time
  parameter H_FRONT_PORCH = 16,     // Horizontal front porch
  parameter H_SYNC_TIME = 96,       // Horizontal sync pulse width
  parameter H_TOTAL = H_BACK_PORCH + H_DISPLAY_TIME + H_FRONT_PORCH + H_SYNC_TIME, 
  
  parameter V_BACK_PORCH = 33,      // Vertical back porch
  parameter V_DISPLAY_TIME = 480,   // Vertical display time
  parameter V_FRONT_PORCH = 10,     // Vertical front porch
  parameter V_SYNC_TIME = 2,        // Vertical sync pulse width
  parameter V_TOTAL = V_BACK_PORCH + V_DISPLAY_TIME + V_FRONT_PORCH + V_SYNC_TIME
)(
  input logic clk, // FPGA Clock 50 MHz
  input logic [8:0] sw, // Input from switches for pixel color
  output logic clk_en_25MHz = 0, // Clock enable 25 MHz
  output logic [2:0] red, // Red pixel color
  output logic [2:0] green, // Green pixel color
  output logic [2:0] blue, // Blue pixel color
  output logic h_sync = 0, // Horizontal sync signal   
  output logic v_sync = 0 // Vertical sync signal
);

  always_ff @(posedge clk) begin
    clk_en_25MHz <= !clk_en_25MHz;
  end

  logic [9:0] h_counter = 0; // Horizontal counter
  logic h_display = 0; // Vertical counter
  logic new_line = 0; // New line signal
  logic [9:0] h_counter_inc; // Horizontal counter increment signal
  assign h_counter_inc = h_counter + 1;

  always_ff @(posedge clk) begin
    if (clk_en_25MHz) begin
      if (h_counter == H_TOTAL - 1) begin
        h_counter <= 0;
      end else begin
        h_counter <= h_counter_inc;
      end
      h_display <= (h_counter_inc >= H_BACK_PORCH && h_counter_inc < H_BACK_PORCH + H_DISPLAY_TIME);
      h_sync <= (h_counter_inc >= H_BACK_PORCH + H_DISPLAY_TIME + H_FRONT_PORCH && h_counter_inc < H_TOTAL);
      new_line <= h_counter_inc == H_TOTAL - 1;
    end
  end

  logic [9:0] v_counter = 0; // Vertical counter
  logic v_display = 0; // Vertical display signal
  logic [9:0] v_counter_inc; // Horizontal counter increment signal
  assign v_counter_inc = v_counter + 1;

  always_ff @(posedge clk) begin
    if (clk_en_25MHz && new_line) begin
      if (v_counter == V_TOTAL - 1) begin
        v_counter <= 0;
      end else begin
        v_counter <= v_counter_inc;
      end
      v_display <= (v_counter_inc >= V_BACK_PORCH && v_counter_inc < V_BACK_PORCH + V_DISPLAY_TIME);
      v_sync <= (v_counter_inc >= V_BACK_PORCH + V_DISPLAY_TIME + V_FRONT_PORCH && v_counter_inc < V_TOTAL);
    end
  end
  
  assign red = (h_display && v_display)? sw[8:6]: 3'b0;
  assign green = (h_display && v_display)? sw[5:3]: 3'b0;
  assign blue = (h_display && v_display)? sw[2:0]: 3'b0;

endmodule