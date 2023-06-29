import { fetchRegiones, fetchComunas } from "./api.js";
window.addEventListener("load", addRegiones);
/*Va a buscar las regiones a la API, y añade las regiones como opciones al select.*/
async function addRegiones() {
  const regiones = await fetchRegiones();
  const selectElement = document.getElementById("select-region");
  regiones.map((region) => {
    const option = document.createElement("option");
    option.text = region.nombre;
    option.value = region.nombre;
    option.setAttribute("data-codigo", region.codigo); // Guardar el código de la región en un atributo nuevo: data-codigo
    selectElement.add(option);
  });
}

async function addComunas() {
  const regionCodigo = document.getElementById("select-region").options[
    document.getElementById("select-region").selectedIndex
  ].getAttribute("data-codigo"); // Obtener el código de la región seleccionada
  document.getElementById("select-comuna").length = 0;
  let comunas = await fetchComunas(regionCodigo);

  if (regionCodigo === 0) {
    document.getElementById("select-comuna").disabled = true;
  } else {
    const selectElement = document.getElementById("select-comuna");
    comunas.map((comuna) => {
      const option = document.createElement("option");
      option.text = comuna.nombre;
      option.value = comuna.nombre;
      option.setAttribute("data-codigo", comuna.codigo); // Guardar el código de la comuna en el atributo data-codigo
      selectElement.add(option);
    });
    document.getElementById("select-comuna").disabled = false;
  }
}


/*Cuando cambie el valor, se enecuta la función addComunas*/
document.getElementById("select-region").addEventListener("change", addComunas);
addRegiones();
