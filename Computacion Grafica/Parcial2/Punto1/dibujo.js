let campo = document.getElementById("dibujo")
let lienzo = campo.getContext('2d')

// Figura superior izquierda
lienzo.beginPath()
lienzo.moveTo(250, 510)
lienzo.lineTo(330, 470)
lienzo.lineTo(330, 430)
lienzo.lineTo(290, 370)
lienzo.lineTo(250, 350)
lienzo.lineTo(170, 390)
lienzo.lineTo(170, 470)
lienzo.lineTo(250, 510)
lienzo.lineTo(250, 470)
lienzo.lineTo(330, 430)
lienzo.lineTo(290, 370)
lienzo.lineTo(210, 410)
lienzo.lineTo(170, 390)
lienzo.lineTo(210, 410)
lienzo.lineTo(250, 390)
lienzo.lineTo(290, 450)
lienzo.lineTo(250, 430)
lienzo.lineTo(250, 390)
lienzo.lineTo(250, 430)
lienzo.lineTo(210, 450)
lienzo.lineTo(250, 470)
lienzo.lineTo(210, 450)
lienzo.lineTo(210, 410)
lienzo.lineTo(210, 450)

// Rellenar
lienzo.fillStyle = "#FF8C00";
lienzo.fill();

lienzo.stroke()


// Figura superior derecha
lienzo.beginPath()
lienzo.moveTo(750, 510)
lienzo.lineTo(830, 470)
lienzo.lineTo(830, 390)
lienzo.lineTo(750, 350)
lienzo.lineTo(670, 390)
lienzo.lineTo(670, 470)
lienzo.lineTo(750, 510)
lienzo.lineTo(750, 470)
lienzo.lineTo(790, 450)
lienzo.lineTo(790, 410)
lienzo.lineTo(830, 390)
lienzo.lineTo(790, 410)
lienzo.lineTo(750, 390)
lienzo.lineTo(710, 410)
lienzo.lineTo(670, 390)
lienzo.lineTo(710, 410)
lienzo.lineTo(710, 450)
lienzo.lineTo(750, 470)
lienzo.lineTo(710, 450)
lienzo.lineTo(750, 430)
lienzo.lineTo(750, 390)
lienzo.lineTo(750, 430)
lienzo.lineTo(790, 450)
lienzo.lineTo(750, 470)

// Rellenar
lienzo.fillStyle = "#0000FF";
lienzo.fill();

lienzo.stroke()


// Figura inferior izquierda
lienzo.beginPath()
lienzo.moveTo(250, 680)
lienzo.lineTo(330, 640)
lienzo.lineTo(330, 600)
lienzo.lineTo(290, 540)
lienzo.lineTo(250, 520)
lienzo.lineTo(170, 560)
lienzo.lineTo(170, 640)
lienzo.lineTo(250, 680)
lienzo.lineTo(250, 640)
lienzo.lineTo(330, 600)
lienzo.lineTo(290, 540)
lienzo.lineTo(250, 560)
lienzo.lineTo(210, 540)
lienzo.lineTo(250, 600)
lienzo.lineTo(290, 620)
lienzo.lineTo(250, 560)
lienzo.lineTo(290, 620)
lienzo.lineTo(250, 640)
lienzo.lineTo(210, 620)
lienzo.lineTo(250, 600)
lienzo.lineTo(210, 620)
lienzo.lineTo(170, 560)

// Rellenar
lienzo.fillStyle = "#00FF00";
lienzo.fill();

lienzo.stroke()


// Figura inferior derecha
lienzo.beginPath()
lienzo.moveTo(750, 680)
lienzo.lineTo(830, 640)
lienzo.lineTo(830, 600)
lienzo.lineTo(790, 580)
lienzo.lineTo(790, 540)
lienzo.lineTo(750, 520)
lienzo.lineTo(670, 560)
lienzo.lineTo(670, 640)
lienzo.lineTo(750, 680)
lienzo.lineTo(790, 620)
lienzo.lineTo(830, 600)
lienzo.lineTo(790, 620)
lienzo.lineTo(710, 620)
lienzo.lineTo(790, 580)
lienzo.lineTo(750, 600)
lienzo.lineTo(750, 560)
lienzo.lineTo(710, 540)
lienzo.lineTo(670, 560)
lienzo.lineTo(750, 680)
lienzo.moveTo(790, 540)
lienzo.lineTo(750, 560)
lienzo.lineTo(710, 540)
lienzo.lineTo(750, 600)

// Rellenar
lienzo.fillStyle = "#FF0000";
lienzo.fill();

lienzo.stroke()