module mux(
    input logic A,
    input logic B,
    input logic S,
    output logic O
);

assign O = S ? B : A; // Mejor asi que como esta abajo

// Recomendable no usar reg ni wire, solo usar logic

// always_ff @( clock ) begin : blockName
    // Proceso secuencial
// end
// always_comb // Proceso totalmente combinatorio (Entradas dependen 100% de salidas)
//     if (S)
//         O = B;
//     else
//         O = A;

endmodule