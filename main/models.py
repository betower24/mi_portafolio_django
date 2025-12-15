# main/models.py
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título del Proyecto")
    description = models.TextField(verbose_name="Descripción Detallada")
    technology = models.CharField(max_length=200, verbose_name="Tecnologías Usadas")
    # Guarda la imagen en la carpeta media/project_images/
    image = models.ImageField(upload_to='project_images/', verbose_name="Captura/Imagen") 
    github_link = models.URLField(max_length=200, blank=True, null=True, verbose_name="Enlace a GitHub")
    live_link = models.URLField(max_length=200, blank=True, null=True, verbose_name="Enlace del Proyecto en Vivo")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at'] # Ordenar del más nuevo al más antiguo

    def __str__(self):
        return self.title

# ------------------------------------
# NUEVO MODELO DE CERTIFICACIONES
# ------------------------------------
class Certification(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nombre de la Certificación")
    # Guarda la imagen del diploma en media/certificates/
    image = models.ImageField(upload_to='certificates/', verbose_name="Imagen del Certificado") 
    date_issued = models.DateField(blank=True, null=True, verbose_name="Fecha de Emisión")
    institution = models.CharField(max_length=100, blank=True, null=True, verbose_name="Institución")

    class Meta:
        ordering = ['-date_issued'] # Ordenar del más reciente al más antiguo
        verbose_name = "Certificación"
        verbose_name_plural = "Certificaciones"

    def __str__(self):
        return self.title