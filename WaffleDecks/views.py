from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.views.static import serve
from .models import Usuario, Carrito, Deck
from .forms import RegistroUsuarioForm
from django.contrib.auth.decorators import login_required
# Create your views here.
# El index no requiere de ninguna información adicional: es una página estática.

# PAGINAS


def index(request):
    carrito = request.session.get('carrito')
    decks = Deck.objects.all()
    context = {
        'active_page': 'index',  # Variable que indica la página activa
        'decks': decks,
        'carrito': carrito
    }
    return render(request, "pages/index.html", context)


@login_required
def tienda(request):
    decks = Deck.objects.all()
    context = {
        'active_page': 'tienda',  # Variable que indica la página activa
        'decks': decks
    }
    return render(request, "pages/tienda.html", context)


def aboutus(request):
    context = {
        'active_page': 'aboutus',
    }
    return render(request, 'pages/aboutus.html', context)


def login(request):
    return render(request, 'registration/login.html')


def registro(request):
    form = RegistroUsuarioForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.region = request.POST.get('region')
            usuario.comuna = request.POST.get('comuna')
            usuario.save()
            print("Se registró un usuario")
            return redirect(login)
    return render(request, 'pages/registro.html', {"form": form})


def serve_product_image(request, filename):
    return serve(request, filename, document_root=settings.MEDIA_ROOT)

# CARRITO


def mostrar_carrito(request):
    if 'carrito' in request.session:
        carrito_id = request.session['carrito']
        carrito = Carrito.objects.get(id=carrito_id)
        decksCarrito = carrito.decks.all()
    else:
        decksCarrito = []

    return render(request, 'base.html', {'decksCarrito': decksCarrito})


def agregar_al_carrito(request, deck_id):
    # Verifica si el carrito ya existe en la sesión del usuario
    if 'carrito' not in request.session:
        # Si no existe, crea un nuevo carrito vacío y guárdalo en la sesión
        carrito = Carrito()
        carrito.save()
        request.session['carrito'] = carrito.id
    else:
        # Si el carrito ya existe, recupéralo de la sesión
        carrito_id = request.session['carrito']
        carrito = Carrito.objects.get(id=carrito_id)

    # Agrega el Deck al carrito
    deck = Deck.objects.get(id=deck_id)
    carrito.decks.add(deck)
