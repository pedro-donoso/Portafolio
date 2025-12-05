from django.shortcuts import render

from .models import Perfil, Experiencia, Certificado, Habilidad, Proyecto


def perfil_view(request):
    perfil = Perfil.objects.first()
    context = {
        'perfil': perfil,
    }
    return render(request, 'core/perfil.html', context)


def experiencia_view(request):
    experiencias = Experiencia.objects.all().order_by('-fecha_inicio', '-id')
    context = {
        'experiencias': experiencias,
    }
    return render(request, 'core/experiencia.html', context)


def certificados_view(request):
    certificados = Certificado.objects.all().order_by('orden', '-fecha')
    context = {
        'certificados': certificados,
    }
    return render(request, 'core/certificados.html', context)


def habilidades_view(request):
    habilidades = Habilidad.objects.all().order_by('categoria', 'orden', 'nombre')
    context = {
        'habilidades': habilidades,
    }
    return render(request, 'core/habilidades.html', context)


def proyectos_view(request):
    proyectos = Proyecto.objects.filter(destacado=True).order_by('orden', '-fecha')
    context = {
        'proyectos': proyectos,
    }
    return render(request, 'core/proyectos.html', context)
