module decodificador(
    input logic [2:0] D,
    input logic en,
    output logic [7:0] Q
);

    always_comb
        if(en) begin // Preguntar si es necesario agregar estos end y begin
            case(D)
                3'b000: Q = 8'b00000001;
                3'b001: Q = 8'b00000010;
                3'b010: Q = 8'b00000100;
                3'b011: Q = 8'b00001000;
                3'b100: Q = 8'b00010000;
                3'b101: Q = 8'b00100000;
                3'b110: Q = 8'b01000000;
                3'b111: Q = 8'b10000000;
                default: Q = 8'b00000000;
            endcase
        end else begin
            Q = 8'b00000000;
        end

endmodule