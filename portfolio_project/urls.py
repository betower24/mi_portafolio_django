# portfolio_project/urls.py
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    # ------------------------------------
    # Conecta las URLs de nuestra aplicación 'main' a la ruta raíz
    path('', include('main.urls')),
    # ------------------------------------
]

# IMPORTANTE: Configuración para servir archivos MEDIA (imágenes de proyectos) 
# y STATIC (CSS/JS) en el entorno de desarrollo (DEBUG=True).
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)