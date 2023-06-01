from django.db import models
# Modelo usuario
class Usuario(models.Model):
  idUsuario = models.AutoField(db_column="idUsuario", primary_key=True)
  runUsuario = models.CharField(db_column='runUsuario', max_length=10)
  primerNombre = models.CharField(max_length=20, blank=False, null=False)
  segundoNombre = models.CharField(max_length=20, blank=True, null=True)
  apPaterno = models.CharField(max_length=25, blank=False, null=False)
  apMaterno = models.CharField(max_length=25, blank=True, null=True)
  def __str__(self):
    return str(self.nombre + ' ' + self.primerNombre + ' ' + self.apPaterno + ' - '
               + self.run)
  
  #Modelo Deck 
class Deck(models.Model):
  idDeck = models.AutoField(db_column='idDeck', primary_key=True)
  nombreDeck = models.CharField(max_length=30, blank=False, null=False)
  precioDeck = models.IntegerField(blank=False, null=True)
  descripcion = models.CharField(max_length=500, blank=False, null=False)
  imagen_url = models.CharField(blank=False, null=False)
# Create your models here.
