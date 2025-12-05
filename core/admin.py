from django.contrib import admin

from .models import Perfil, Experiencia, Certificado, Habilidad, Proyecto

admin.site.register(Perfil)
admin.site.register(Experiencia)
admin.site.register(Certificado)
admin.site.register(Habilidad)
admin.site.register(Proyecto)


