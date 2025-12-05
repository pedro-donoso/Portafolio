from django.shortcuts import render

from .models import Perfil, Experiencia, Certificado, Habilidad, Proyecto


def home_view(request):
    perfil = Perfil.objects.first()
    experiencias = Experiencia.objects.all().order_by('-fecha_inicio', '-id')
    certificados = Certificado.objects.all().order_by('orden', '-fecha')
    habilidades = Habilidad.objects.all().order_by('categoria', 'orden', 'nombre')
    proyectos = Proyecto.objects.filter(destacado=True).order_by('orden', '-fecha')

    context = {
        'perfil': perfil,
        'experiencias': experiencias,
        'certificados': certificados,
        'habilidades': habilidades,
        'proyectos': proyectos,
    }
    return render(request, 'core/home.html', context)



