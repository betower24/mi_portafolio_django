# portfolio_project/urls.py

from django.contrib import admin
from django.urls import path, include
# Importaciones necesarias para MEDIA/ESTÁTICOS
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), # Asumiendo que esta es tu URL raíz
]

# ESTO ES CRUCIAL PARA SERVIR MEDIA/STATICOS EN DEBUG (que puede ser forzado por Render)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)