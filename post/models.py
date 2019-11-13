from django.db import models
from django.utils import timezone


class Programador(models.Model):
    nombre = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    correo =models.CharField(max_length=200)
    bio =  models.TextField()
    alma_mater = models.CharField(max_length=200)
    avatar = models.ImageField(null=True, upload_to='albums/images/')

    def __str__(self):
        #llamar el nombre desde nombre(auth.user)
        return self.correo

class Proyecto(models.Model):
    autor = models.ForeignKey('Programador', on_delete=models.CASCADE)
    estado_post = models.CharField(max_length=200)
    link_descarga = models.CharField(max_length=200)
    lenguaje = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.titulo   