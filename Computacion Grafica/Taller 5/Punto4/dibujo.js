let campo = document.getElementById("dibujo")
let lienzo = campo.getContext('2d')

lienzo.beginPath()
lienzo.rect(50, 50, 100, 150) // Crea un rectangulo con bordes y relleno
// El primer parametro representa la coordenada inicial en x, el segundo
// la coordenada inicial en y, el tercero el ancho y el cuarto el alto

lienzo.fillStyle = "red" // Define el color del relleno
lienzo.fill() // Dibuja el relleno
lienzo.lineWidth = 5 // Cambia el tamaño de los bordes
lienzo.strokeStyle = "blue" 
lienzo.stroke()

lienzo.beginPath()
lienzo.ellipse(300, 150, 60, 40, 0, 0, 2 * Math.PI) // Elipse
// El primer parametro representa la coordenada inicial en x, 
// el segundo la coordenada inicial en y, el tercero el ancho 
// en x, el cuarto el ancho en y, el quinto la rotacion, el 
// sexto el angulo inicial y el septimo el angulo final

lienzo.strokeStyle = "red"
lienzo.lineWidth = 1
lienzo.stroke()


lienzo.beginPath();
lienzo.moveTo(50, 300);
lienzo.quadraticCurveTo(100, 200, 250, 300); // Curva cuadrática
// Los primero dos parametros representan las coordenadas del punto 
// pivote, y los ultimos dos las coordenadas finales
lienzo.strokeStyle = "black"
lienzo.stroke();


lienzo.beginPath();
lienzo.moveTo(50, 350);
lienzo.bezierCurveTo(100, 250, 200, 450, 250, 350); // Curva Bézier
// Los primeros dos parametros representan las coordenadas del primer
// punto pivote, los siguientes el segundo punto pivote y los ultimos
// la coordenada del punto final

lienzo.stroke();
