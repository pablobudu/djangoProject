from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("tienda", views.tienda, name="tienda"),
    path('media/imgs/<path:filename>/',
         views.serve_product_image, name='serve_product_image'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
