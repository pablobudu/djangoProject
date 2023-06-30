from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Esta clase hereda del User de django (para autenticación), pero le agregamos campos adicionales que nos sirven para almacenarlos en la BD.


class CustomUser(AbstractUser):
    pass
    region = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)


class Deck(models.Model):
    idDeck = models.AutoField(primary_key=True)
    nombreDeck = models.CharField(max_length=30, blank=False, null=True)
    precioDeck = models.IntegerField(blank=False, null=True)
    descripcion = models.CharField(max_length=500, blank=False, null=True)
    imagen = models.ImageField(
        upload_to='imgs/', blank=False, null=False)

    def __str__(self):
        return str(self.nombreDeck + ' ' + str(self.precioDeck))


class Carrito(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    decks = models.ManyToManyField(Deck)

    def __str__(self):
        return f"Carrito de {self.usuario.username}"
