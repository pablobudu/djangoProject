//Este archivo exporta la función que va a buscar datos a la API de correos de Chile.
const apiUrlRegiones = "https://apis.digital.gob.cl/dpa/regiones";

/* Va a buscar las regiones*/
async function fetchRegiones() {
  const response = await fetch("https://apis.digital.gob.cl/dpa/regiones");
  return response.json();
}

/*Va a buscar las comunas pertenecientes a una determinada región. */
async function fetchComunas(region) {
  const response = await fetch(
    "https://apis.digital.gob.cl/dpa/regiones/" + region + "/comunas"
  );
  return response.json();
}


export { fetchRegiones, fetchComunas };