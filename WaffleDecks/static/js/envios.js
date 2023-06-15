import { fetchRegiones, fetchComunas } from "./api.js";
window.addEventListener("load", addRegiones);
/*Va a buscar las regiones a la API, y añade las regiones como opciones al select.*/
async function addRegiones() {
  const regiones = await fetchRegiones();
  const selectElement = document.getElementById("select-region");
  regiones.map((region) => {
    const option = document.createElement("option");
    option.text = region.nombre;
    option.value = region.codigo;
    selectElement.add(option);
  });
}

/*Va a buscar las comunas de la región seleccionada, y las añade como opciones en el select. */
async function addComunas() {
  let codigoRegion = document.getElementById("select-region").value;
  document.getElementById("select-comuna").length = 0;
  let comunas = await fetchComunas(codigoRegion);

  if (codigoRegion == 0) {
    document.getElementById("select-comuna").disabled = true;
  } else {
    const selectElement = document.getElementById("select-comuna");
    comunas.map((comuna) => {
      const option = document.createElement("option");
      option.text = comuna.nombre;
      option.value = comuna.codigo;
      selectElement.add(option);
    });
    document.getElementById("select-comuna").disabled = false;
  }
}

/*Cuando cambie el valor, se enecuta la función addComunas*/
document.getElementById("select-region").addEventListener("change", addComunas);
addRegiones();
