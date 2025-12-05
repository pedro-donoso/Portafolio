from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('perfil/', views.perfil_view, name='perfil'),
    path('experiencia/', views.experiencia_view, name='experiencia'),
    path('certificados/', views.certificados_view, name='certificados'),
    path('habilidades/', views.habilidades_view, name='habilidades'),
    path('proyectos/', views.proyectos_view, name='proyectos'),
]
