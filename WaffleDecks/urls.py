from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("tienda", views.tienda, name="tienda"),
]
