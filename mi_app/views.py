# views.py de mi_app

from django.shortcuts import render
import json

def dashboard_view(request):
    # Asegúrate de que la ruta al archivo JSON sea correcta
    with open('dashboard_data.json', 'r') as file:
        data = json.load(file)
    
    # Renderizar la plantilla, notar que se utiliza 'mi_app/dashboard.html'
    return render(request, 'mi_app/dashboard.html', {'data': data})
