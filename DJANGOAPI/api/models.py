from django.db import models

# Create your models here.
class Genero (models.Model):
    genero_id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=255)
    class Meta :
        db_table = 'Genero'
        
class Usuarios(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=255)
    fk_generos = models.ForeignKey(Genero,on_delete=models.CASCADE,default=0)
    class Meta :
        db_table = 'usuarios'