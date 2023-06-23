from django.db import models

# Create your models here.


class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    runUsuario = models.CharField(max_length=10)
    primerNombre = models.CharField(max_length=20, blank=False, null=False)
    segundoNombre = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
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
        upload_to='imgs/', blank=False, null=False)

    def __str__(self):
        return str(self.nombreDeck + ' ' + str(self.precioDeck))


class Carrito(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    decks = models.ManyToManyField(Deck, through='DeckCarrito')

    def __str__(self):
        return f"Carrito de {self.usuario.username}"


class DeckCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.deck.nombreDeck}"
