from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.views.static import serve
from .models import Deck
# Create your views here.
# El index no requiere de ninguna información adicional: es una página estática.


def index(request):
    return render(request, "pages/index.html")


def tienda(request):
    return render(request, "pages/tienda.html")


def serve_product_image(request, filename):
    return serve(request, filename, document_root=settings.MEDIA_ROOT)


def tienda(request):
    decks = Deck.objects.all()
    return render(request, 'pages/tienda.html', {'decks': decks})
