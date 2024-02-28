from django.shortcuts import render
from django.conf import settings
import subprocess
import os

def dashboard_view(request):
    # Construye la ruta completa al script
    script_path = os.path.join(settings.BASE_DIR, 'mi_app', 'generate_charts.py')
    
    # Ejecuta el script para generar los gráficos
    subprocess.run(['python', script_path], check=True)
    
    # Renderiza la plantilla normalmente
    return render(request, 'mi_app/dashboard.html')