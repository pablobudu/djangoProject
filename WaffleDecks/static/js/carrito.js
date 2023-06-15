let carrito = [];
let contador = 0;
let botones = document.querySelectorAll(".agregar-carrito");

botones.forEach(function (boton) {
  boton.addEventListener("click", function () {
    let id = parseInt(boton.getAttribute("producto-id"));

    // Buscamos el producto por su id en el array de productos y lo agregamos al carrito de compras
    let producto = productos.find(function (p) {
      return p.id === id;
    });
    carrito.push(producto);

    console.log("Se agregó el producto al carrito");

    // Actualizamos la visualización del carrito de compras
    contador++;
    actualizarContador();
    actualizarCarrito();
  });
});

function actualizarTotal() {
  let total = 0;
  for (let i = 0; i < carrito.length; i++) {
    total += carrito[i].precio;
  }
  let totalElemento = document.querySelector(".total");
  totalElemento.textContent = "Total: $" + total;
}

function actualizarCarrito() {
  let carritoContenedor = document.querySelector(
    "#carritoOffcanvas .offcanvas-body .list-group"
  );
  carritoContenedor.innerHTML = "";

  carrito.forEach(function (producto) {
    let itemCarrito = document.createElement("li");
    itemCarrito.classList.add(
      "list-group-item",
      "d-flex",
      "justify-content-between",
      "lh-sm"
    );
    itemCarrito.innerHTML = `
        <div>
          <h6 class="my-0">${producto.nombre}</h6>
          <small class="text-muted">${producto.descripcion}</small>
        </div>
        <span class="text-muted">$${producto.precio}</span>
      `;
    carritoContenedor.appendChild(itemCarrito);
    actualizarTotal();
  });
}
function actualizarContador() {
  let contadorElemento = document.querySelector(".contador");
  contadorElemento.textContent = contador;
}
