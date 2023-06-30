from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Carrito

@receiver(post_save, sender=get_user_model())
def crear_carrito_usuario(sender, instance, created, **kwargs):
    if created:
        Carrito.objects.create(usuario=instance)
