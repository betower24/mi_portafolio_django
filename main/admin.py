# main/admin.py
from django.contrib import admin
from .models import Project, Certification # ¡Importa Certification!

# Esto registra el modelo Project (ya lo tienes)
admin.site.register(Project) 

# ¡Registra el nuevo modelo!
admin.site.register(Certification)