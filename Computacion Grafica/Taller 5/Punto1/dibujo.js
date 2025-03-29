let campo = document.getElementById("dibujo")
let lienzo = campo.getContext('2d')

lienzo.beginPath()
lienzo.arc(150, 150, 150, 0, 2 * Math.PI)
lienzo.strokeStyle = "green"
lienzo.stroke()

lienzo.beginPath()
lienzo.arc(350, 150, 150, 0, 2 * Math.PI)
lienzo.strokeStyle = "blue"
lienzo.stroke()

lienzo.beginPath()
lienzo.arc(250, 350, 150, 0, 2 * Math.PI)
lienzo.strokeStyle = "red"
lienzo.stroke()