from django.db import models

# Create your models here.


class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    runUsuario = models.CharField(max_length=10)
    primerNombre = models.CharField(max_length=20, blank=False, null=False)
    segundoNombre = models.CharField(max_length=20, blank=True, null=True)
    apPaterno = models.CharField(max_length=25, blank=False, null=False)
    apMaterno = models.CharField(max_length=25, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return str(self.primerNombre + " " + self.apPaterno)


class Deck(models.Model):
    idDeck = models.AutoField(primary_key=True)
    nombreDeck = models.CharField(max_length=30, blank=False, null=True)
    precioDeck = models.IntegerField(blank=False, null=True)
    descripcion = models.CharField(max_length=500, blank=False, null=True)
    imagen = models.ImageField(
        upload_to='imgs/', blank=False, null=False, default='default_image.jpg')

    def __str__(self):
        return str(self.nombreDeck + ' ' + str(self.precioDeck))
