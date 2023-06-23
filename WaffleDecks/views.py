from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.views.static import serve
from .models import Deck
# Create your views here.
# El index no requiere de ninguna información adicional: es una página estática.

# PAGINAS


def index(request):
    decks = Deck.objects.all()
    context = {
        'active_page': 'index',  # Variable que indica la página activa
        'decks': decks
    }
    return render(request, "pages/index.html", context)


def tienda(request):
    decks = Deck.objects.all()
    context = {
        'active_page': 'tienda',  # Variable que indica la página activa
        'decks': decks
    }
    return render(request, "pages/tienda.html", context)


def aboutus(request):
    context = {
        'active_page': 'aboutus',  # Variable que indica la página activa
    }
    return render(request, context)


def login(request):
    context = {
        'active_page': 'tienda'
    }
    return render(request, context)


def serve_product_image(request, filename):
    return serve(request, filename, document_root=settings.MEDIA_ROOT)
