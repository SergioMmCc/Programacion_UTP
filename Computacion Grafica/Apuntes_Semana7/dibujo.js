let campo = document.getElementById("dibujo")
let lienzo = campo.getContext('2d')


// Cuadro forntal
lienzo.beginPath()

lienzo.moveTo(150, 100)
lienzo.lineTo(250, 50)
lienzo.lineTo(350, 100)
lienzo.lineTo(300, 150)
lienzo.lineTo(200, 150)
lienzo.lineTo(150, 100)
lienzo.lineTo(150, 400)
lienzo.lineTo(200, 450)
lienzo.lineTo(200, 150)
lienzo.lineTo(200, 450)
lienzo.lineTo(300, 450)
lienzo.lineTo(300, 150)
lienzo.lineTo(300, 450)
lienzo.lineTo(350, 400)
lienzo.lineTo(350, 100)

lienzo.strokeStyle = "blue"
lienzo.stroke()
lienzo.closePath()


lienzo.setLineDash([10, 5])
lienzo.beginPath()

lienzo.moveTo(150, 400)
lienzo.lineTo(250, 350)
lienzo.lineTo(350, 400)
lienzo.lineTo(250, 350)
lienzo.lineTo(250, 50)

lienzo.strokeStyle = "blue"
lienzo.stroke()
lienzo.closePath()