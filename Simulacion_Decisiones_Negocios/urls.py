# Simulacion_Decisiones_Negocios/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mi_app.urls')), 
]