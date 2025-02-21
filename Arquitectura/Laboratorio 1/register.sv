module register(
    input logic clk,
    input logic [31:0] D,
    input logic en,
    output logic [31:0] Q = 0); // Como es secuencial necesito que tenga un estado definido

    always_ff @(posedge clk)
        if(en)
            Q <= D;

endmodule