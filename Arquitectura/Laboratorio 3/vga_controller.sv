module vga_controller(
    input logic clk, // FPGA Clock 50 MHz
    input logic [8:0] sw, // Input from switches for pixel color
    output logic clk_en_25MHz = 0, // Clock enable 25 MHz
    output logic [2:0] red = 0, // Red pixel color
    output logic [2:0] green = 0, // Green pixel color
    output logic [2:0] blue = 0, // Blue pixel color
    output logic hsync, // Horizontal sync signal 
    output logic vsync // Vertical sync signal
);

    // Clock enable 25MHz
    always_ff @(posedge clk) begin
        clk_en_25MHz <= !clk_en_25MHz;
    end

    logic [9:0] h_counter = 0; // Horizontal counter
    logic h_display; // Horizontal display signal, no la puedo inicializar porque es la salida de una compuerta
    logic new_line; // New line signal, no la puedo inicializar porque es la salida de una compuerta
    always_ff @(posedge clk) begin
        if(clk_en_25MHz) begin // Se activa con el reloj de la FPGA pero ese if hace que funcione con el de 25MHz
            if(h_counter == 799) begin
                h_counter <= 0;
            end else begin
                h_counter <= h_counter + 1;
            end
        end
    end
    assign h_display = h_counter < 640;
    assign hsync = h_counter >= 656 && h_counter < 752; // 799 - los 47 del back_porch
    assign new_line = h_counter == 799; // Me ayuda para la sincronizacion vertical

    logic [9:0] v_counter = 0; // Vertical Counter
    logic v_display; // Vertical display signal, no la puedo inicializar porque es la salida de una compuerta
    always_ff @(posedge clk) begin
        if(clk_en_25MHz && new_line) begin
            if(v_counter == 524) begin
                v_counter <= 0;
            end else begin
                v_counter <= v_counter + 1;
            end
        end
    end
    assign v_display = v_counter < 480;
    assign v_sync = v_counter >= 490 && v_counter < 492; // 525 - 33 del back_porch

    always_comb begin // always_comb crea un proceso totalmente combinacional (sin registros ni flip-flops)
        if(h_display && v_display) begin
            // assing red = sw[8:6];
            // assing green = sw[5:3];
            // assing blue = sw[2:0];
            red = 7;
            green = 0;
            blue = 0;
        end else begin
            red = 0;
            green = 0;
            blue = 0;
        end
    end


endmodule