from django.db import models

class Usuario(models.Model):
  idUsuario = models.AutoField(db_column="idUsiario", primary_key=True)
  runUsuario = models.CharField(db_column='runUsuario', max_length=10)
  primerNombre = models.CharField(max_length=20, blank=False, null=False)
  segundoNombre = models.CharField(max_length=20, blank=True, null=True)
  apPaterno = models.CharField(max_length=25, blank=False, null=False)
  apMaterno = models.CharField(max_length=25, blank=True, null=True)
  def __str__(self):
    return str(self.nombre + ' ' + self.primerNombre + ' ' + self.apPaterno + ' - '
               + self.run)
# Create your models here.
