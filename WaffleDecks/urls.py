from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tienda", views.tienda, name="tienda"),
    path("aboutus", views.aboutus, name="aboutus"),
    path('accounts/signup/', views.signup, name='signup'),
    path('mostrar_carrito/<int:carrito_id>/',
         views.mostrar_carrito, name='mostrar_carrito'),
    path('agregar_al_carrito/<int:deck_id>/',
         views.agregar_al_carrito, name='agregar_al_carrito'),
]
