from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tienda", views.tienda, name="tienda"),
    path("aboutus", views.aboutus, name="aboutus"),
    path("login", views.login, name="login"),

]
