
let contador = 0;
let botones = document.querySelectorAll(".agregar-carrito");

botones.forEach(function (boton) {
  boton.addEventListener("click", function () {
    let deckId = boton.getAttribute("data-deck-id");

    // Enviar la solicitud al servidor utilizando Fetch
    fetch(`/agregar_al_carrito/${deckId}/`, {
      method: "POST",
    })
      .then(function (response) {
        if (response.ok) {
          console.log("Deck agregado al carrito");
          // Realizar cualquier acción adicional después de agregar el deck al carrito
        } else {
          console.log("Error al agregar el deck al carrito");
          // Manejar el error en caso de que ocurra
        }
      })
      .catch(function (error) {
        console.log("Error al enviar la solicitud");
        // Manejar el error en caso de que ocurra
      });
  });
});



function actualizarTotal() {
  let total = 0;
  for (let i = 0; i < carrito.length; i++) {
    total += carrito[i].precioDeck;
  }
  let totalElemento = document.querySelector(".total");
  totalElemento.textContent = "Total: $" + total;
}

function actualizarCarrito() {
  let carritoContenedor = document.querySelector(
    "#carritoOffcanvas .offcanvas-body .list-group"
  );
  carritoContenedor.innerHTML = "";

  carrito.forEach(function (deck) {
    let itemCarrito = document.createElement("li");
    itemCarrito.classList.add(
      "list-group-item",
      "d-flex",
      "justify-content-between",
      "lh-sm"
    );
    itemCarrito.innerHTML = `
        <div>
          <h6 class="my-0">${deck.nombreDeck}</h6>
          <small class="text-muted">${deck.descripcion}</small>
        </div>
        <span class="text-muted">$${deck.precioDeck}</span>
        <button class="agregar-carrito" data-deck-id="${deck.idDeck}">Agregar al carrito</button>
      `;
    carritoContenedor.appendChild(itemCarrito);
    actualizarTotal();
  });
}

function actualizarContador() {
  let contadorElemento = document.querySelector(".contador");
  contadorElemento.textContent = contador;
}
