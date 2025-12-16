# portfolio_project/urls.py

from django.contrib import admin
from django.urls import path, include
# Importaciones necesarias para MEDIA/ESTÁTICOS
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta línea llama al archivo urls.py de tu aplicación 'main'
    path('', include('main.urls')), 
]

# CRÍTICO: Servir archivos media y estáticos manualmente cuando DEBUG=True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)