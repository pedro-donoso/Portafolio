from django.db import models


class Perfil(models.Model):
    nombre = models.CharField(max_length=100)
    titulo = models.CharField(max_length=150, blank=True)
    resumen = models.TextField()
    email = models.EmailField(blank=True)
    ciudad = models.CharField(max_length=100, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    foto = models.ImageField(upload_to='perfil/', blank=True, null=True)


def __str__(self):
    return self.nombre


class Experiencia(models.Model):
    empresa = models.CharField(max_length=150)
    puesto = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    actual = models.BooleanField(default=False)
    orden = models.PositiveIntegerField(default=0)


def __str__(self):
    return f"{self.puesto} - {self.empresa}"
