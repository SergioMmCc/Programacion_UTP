let campo = document.getElementById("dibujo")
let lienzo = campo.getContext('2d')

// Triangulo
lienzo.beginPath()
lienzo.moveTo(100, 100)
lienzo.lineTo(150, 150)
lienzo.lineTo(50, 150)
lienzo.closePath()
lienzo.stroke()

// Rectangulo
lienzo.beginPath()
lienzo.moveTo(250, 100)
lienzo.lineTo(350, 100)
lienzo.lineTo(350, 150)
lienzo.lineTo(250, 150)
lienzo.closePath()
lienzo.stroke()

// Trapecio
lienzo.beginPath()
lienzo.moveTo(500, 100)
lienzo.lineTo(600, 100)
lienzo.lineTo(650, 150)
lienzo.lineTo(450, 150)
lienzo.closePath()
lienzo.stroke()

// Hexagono
lienzo.beginPath()
lienzo.moveTo(700, 150)
lienzo.lineTo(750, 100)
lienzo.lineTo(800, 100)
lienzo.lineTo(850, 150)
lienzo.lineTo(800, 200)
lienzo.lineTo(750, 200)
lienzo.closePath()
lienzo.stroke()