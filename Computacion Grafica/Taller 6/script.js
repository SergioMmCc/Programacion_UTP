const inputsDiv = document.getElementById("inputs");
const salida = document.getElementById("salida");
let estadoSecuencial = null; // usado para controlar el flujo en 4 y 6

function mostrarFormulario(){
  inputsDiv.innerHTML = "";
  salida.value = "";
  estadoSecuencial = null;
  const opcion = document.getElementById("menu").value;

  const crearInput = (label, name, type = "text") =>{
    return `<label>${label}</label><input name="${name}" type="${type}" required />`;
  };

  switch (opcion){
    case "1":
      inputsDiv.innerHTML = crearInput("Número de la tabla:", "num") +
                            crearInput("Hasta qué número:", "hasta");
      break;
    case "2":
      inputsDiv.innerHTML = crearInput("Ancho del rectángulo:", "ancho") +
                            crearInput("Alto del rectángulo:", "alto") +
                            crearInput("Carácter:", "caracter");
      break;
    case "3":
      inputsDiv.innerHTML = crearInput("Año inicial:", "inicio") +
                            crearInput("Año final:", "fin");
      break;
    case "4":
      inputsDiv.innerHTML = crearInput("Cantidad de números:", "cantidad") +
                            `<button type="button" onclick="iniciarSecuencialNumeros()">Comenzar</button>`;
      break;
    case "5":
      inputsDiv.innerHTML = crearInput("Ingrese el correo:", "correo");
      break;
    case "6":
      inputsDiv.innerHTML = crearInput("Cantidad de cadenas:", "cantidad") +
                            `<button type="button" onclick="iniciarSecuencialCadenas()">Comenzar</button>`;
      break;
  }
}

function iniciarSecuencialNumeros(){
  const cantidad = parseInt(document.querySelector("input[name='cantidad']").value);
  if (isNaN(cantidad) || cantidad <= 0) return alert("Cantidad inválida");
  inputsDiv.innerHTML = `<label id="etiquetaSecuencial">Ingrese número 1:</label>
    <input id="inputSecuencial" type="number" />
    <button type="button" onclick="procesarNumeroSecuencial()">Siguiente</button>`;
  salida.value = "";
  estadoSecuencial = {
    tipo: "numeros",
    cantidad,
    index: 0,
    suma: 0,
    anterior: null,
    out: ""
  };
}

function procesarNumeroSecuencial(){
  const input = document.getElementById("inputSecuencial");
  const val = parseInt(input.value);
  if (isNaN(val)) return alert("Ingrese un número válido");

  if (val === estadoSecuencial.anterior){
    salida.value += `¡${val} no es distinto de ${estadoSecuencial.anterior}!\n`;
    return;
  }

  estadoSecuencial.suma += val;
  estadoSecuencial.anterior = val;
  estadoSecuencial.index++;

  if (estadoSecuencial.index >= estadoSecuencial.cantidad){
    salida.value += `Gracias por su colaboración.\nLa sumatoria es: ${estadoSecuencial.suma}`;
    inputsDiv.innerHTML = ""; // limpiar formulario
  } else{
    input.value = "";
    input.focus();
    document.getElementById("etiquetaSecuencial").textContent = `Ingrese número ${estadoSecuencial.index + 1}:`;
  }
}

function iniciarSecuencialCadenas(){
  const cantidad = parseInt(document.querySelector("input[name='cantidad']").value);
  if (isNaN(cantidad) || cantidad <= 0) return alert("Cantidad inválida");
  inputsDiv.innerHTML = `<label id="etiquetaSecuencial">Ingrese cadena 1:</label>
    <input id="inputSecuencial" type="text" />
    <button type="button" onclick="procesarCadenaSecuencial()">Siguiente</button>`;
  salida.value = "";
  estadoSecuencial ={
    tipo: "cadenas",
    cantidad,
    index: 0,
    total: 0,
    out: ""
  };
}

function procesarCadenaSecuencial(){
  const input = document.getElementById("inputSecuencial");
  const cad = input.value.trim();
  if (!cad) return alert("Ingrese una cadena válida");

  estadoSecuencial.total += cad.length;
  salida.value += `Longitud de "${cad}": ${cad.length}\n`;
  estadoSecuencial.index++;

  if (estadoSecuencial.index >= estadoSecuencial.cantidad){
    salida.value += `\nSumatoria total de longitudes: ${estadoSecuencial.total}`;
    inputsDiv.innerHTML = ""; // limpiar formulario
  } else{
    input.value = "";
    input.focus();
    document.getElementById("etiquetaSecuencial").textContent = `Ingrese cadena ${estadoSecuencial.index + 1}:`;
  }
}

function ejecutar(e){
  e.preventDefault();
  const form = new FormData(e.target);
  const opcion = document.getElementById("menu").value;
  salida.value = "";

  switch (opcion){
    case "1":{
      const num = parseInt(form.get("num"));
      const hasta = parseInt(form.get("hasta"));
      let out = "";
      for (let i = 1; i <= hasta; i++){
        out += `${num} x ${i} = ${num * i}\n`;
      }
      salida.value = out;
      break;
    }
    case "2":{
      const ancho = parseInt(form.get("ancho"));
      const alto = parseInt(form.get("alto"));
      const caracter = form.get("caracter");
      let rect = "";
      for (let i = 0; i < alto; i++){
        rect += caracter.repeat(ancho) + "\n";
      }
      salida.value = rect;
      break;
    }
    case "3":{
      const inicio = parseInt(form.get("inicio"));
      const fin = parseInt(form.get("fin"));
      let contador = 0;
      for (let i = inicio; i <= fin; i++){
        if ((i % 4 === 0 && i % 100 !== 0) || i % 400 === 0) contador++;
      }
      salida.value = `Entre ${inicio} y ${fin} hay ${contador} años bisiestos.`;
      break;
    }
    case "5":{
      const correo = form.get("correo");
      const valido = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(correo);
      salida.value = valido ? "El correo es válido." : "El correo NO es válido.";
      break;
    }
  }
}
