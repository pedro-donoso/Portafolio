from django.db import models


class Perfil(models.Model):
    nombre = models.CharField(max_length=100)
    titulo = models.CharField(max_length=150, blank=True)
    resumen = models.TextField(blank=True)
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


class Certificado(models.Model):
    nombre = models.CharField(max_length=200)
    entidad = models.CharField(max_length=150)
    fecha = models.DateField(blank=True, null=True)
    url_certificado = models.URLField(blank=True)
    descripcion = models.TextField(blank=True)
    orden = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre


class Habilidad(models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.PositiveIntegerField(default=0)
    categoria = models.CharField(max_length=100, blank=True)
    orden = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre


class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    url_demo = models.URLField(blank=True)
    url_codigo = models.URLField(blank=True)
    tecnologias = models.CharField(max_length=200, blank=True)
    fecha = models.DateField(blank=True, null=True)
    destacado = models.BooleanField(default=True)
    orden = models.PositiveIntegerField(default=0)

    imagen_static = models.CharField(
        max_length=200,
        blank=True,
        help_text="Ruta dentro de static/, por ejemplo: img/proyecto1.png",
    )


def __str__(self):
    return self.titulo
