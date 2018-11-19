from django.db import models
from django.contrib import admin
from django.utils import timezone

# Create your models here.
class Grado(models.Model):

    nombre  =   models.CharField(max_length=30)
    seccion = models.CharField(max_length=30)

    def __str__(self):

        return self.nombre

class Materia(models.Model):
    nombre    = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class Control (models.Model):
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
