function graficar() {
    const canvas = document.getElementById("grafico");
    const ctx = canvas.getContext("2d");
  
    // Limpiar el canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  
    // Dibujar ejes
    ctx.beginPath();
    ctx.moveTo(30, 10);   // eje Y
    ctx.lineTo(30, 220);
    ctx.lineTo(290, 220); // eje X
    ctx.strokeStyle = "#555";
    ctx.stroke();
  
    // Obtener y procesar los datos ingresados
    const input = document.getElementById("datosInput").value;
    const datos = input.split(",").map(num => parseInt(num.trim()));
  
    if (datos.some(isNaN)) {
      alert("Por favor ingresa solo números separados por comas.");
      return;
    }
  
    // Escalado y origen
    const offsetX = 30;
    const offsetY = 220;
    const pasoX = 40;
  
    ctx.beginPath();
    ctx.moveTo(offsetX, offsetY - datos[0]);
  
    for (let i = 1; i < datos.length; i++) {
      const x = offsetX + pasoX * i;
      const y = offsetY - datos[i];
      ctx.lineTo(x, y);
    }
  
    ctx.strokeStyle = "rgba(0, 0, 255, 0.5)";
    ctx.lineWidth = 2;
    ctx.stroke();
  }
  