# main/views.py
from django.shortcuts import render
from .models import Project, Certification # ¡Importa Certification!

def home(request):
    projects = Project.objects.all()
    # Recupera todas las certificaciones
    certifications = Certification.objects.all()
    
    context = {
        'projects': projects,
        'certifications': certifications, # <--- ¡AGREGADO!
        'my_name': 'José Alberto Fernandez Garcia ', 
        'title': 'Portafolio de Desarrollo Software'
    }
    return render(request, 'main/home.html', context)