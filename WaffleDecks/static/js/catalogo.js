const productoCatalogoHTML = (producto) => {
  return `
    <div class="col">
      <div class="card" style="width: 18rem;">
        <img src="${producto.img}" class="card-img-top" alt="${producto.descripcion}">
        <div class="card-body">
          <h5 class="card-title">${producto.nombre}</h5>
          <p class="card-text">${producto.precio}</p>
          <button href="#" producto-id ="${producto.id}"class="btn btn-success agregar-carrito">Agregar</button>
        </div>
      </div>
    </div>
  `;
};

const mostrarCatalogo = () => {
  const catalogoNodo = document.getElementById("catalogo");
  let catalogoHTML = "";

  for (const producto of productos) {
    catalogoHTML += productoCatalogoHTML(producto);
  }
  catalogoNodo.innerHTML = catalogoHTML;
};

mostrarCatalogo();
