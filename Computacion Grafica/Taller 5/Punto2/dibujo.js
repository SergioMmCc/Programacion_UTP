let campo = document.getElementById("dibujo")
let lienzo = campo.getContext('2d')

// Linea base
lienzo.beginPath()
lienzo.moveTo(100, 600)
lienzo.lineTo(900, 600)
lienzo.strokeStyle = "red"
lienzo.stroke()

// Parte frontal
lienzo.beginPath()
lienzo.moveTo(500, 600)
lienzo.lineTo(100, 500)
lienzo.lineTo(100, 300)
lienzo.lineTo(500, 400)
lienzo.lineTo(900, 300)
lienzo.lineTo(900, 500)
lienzo.lineTo(500, 600)
lienzo.lineTo(500, 400)
lienzo.strokeStyle = "blue"
lienzo.stroke()

// Parte superior
lienzo.beginPath()
lienzo.moveTo(100, 300)
lienzo.lineTo(500, 200)
lienzo.lineTo(900, 300)
lienzo.strokeStyle = "blue"
lienzo.stroke()

lienzo.beginPath()
lienzo.moveTo(500, 380)
lienzo.lineTo(165, 300)
lienzo.lineTo(500, 220)
lienzo.lineTo(835, 300)
lienzo.closePath()
lienzo.strokeStyle = "yellow"
lienzo.stroke()

// Linea interna
lienzo.beginPath()
lienzo.moveTo(500, 380)
lienzo.lineTo(500, 220)
lienzo.strokeStyle = "green"
lienzo.stroke()