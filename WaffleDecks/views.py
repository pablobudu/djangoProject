from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.views.static import serve
from .models import Carrito, Deck
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm

# Create your views here.

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


def signup(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registration/signup.html', {'form': form})


def serve_product_image(request, filename):
    return serve(request, filename, document_root=settings.MEDIA_ROOT)

# CARRITO


@csrf_exempt
def mostrar_carrito(request):
    # Obtener el carrito del usuario
    carrito = Carrito.objects.get(usuario=request.user)
    decks = carrito.decks.all()  # Obtener los decks del carrito
    return render(request, 'base.html', {'carrito': carrito})


@csrf_exempt
@login_required
def agregar_al_carrito(request, deck_id):
    deck = get_object_or_404(Deck, idDeck=deck_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    carrito.decks.add(deck)
    carrito.save()
    return redirect('tienda')
