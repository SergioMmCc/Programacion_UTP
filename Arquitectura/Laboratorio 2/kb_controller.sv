module PS2(
    input logic ps2_clk, // PS2 Clock
    input logic ps2_data, //PS2 Data
    output logic [7:0] leds // 8 LEDs
);

    logic [3:0] count = 11;
    logic paridad;
    logic [7:0] aux;
    always_ff @(negedge ps2_clk) begin
        if(count == 11) begin 
            if(~ps2_data) begin 
                count <= 1;
                paridad <= 1;
            end
            leds <= 8'b00000000;
        end
        else if(count < 9) begin 
            aux[count-1] <= ps2_data;
            if(ps2_data) begin 
                paridad <= ~paridad;
            end

            count <= count + 1;
        end
        else if(count == 9) begin 
            if(paridad == ps2_data) begin 
                leds <= aux;
            end
            else begin 
                leds <= 8'b00000000;
            end

            count <= 10;
        end
        else begin 
            count <= 11;
        end
    end

endmodule