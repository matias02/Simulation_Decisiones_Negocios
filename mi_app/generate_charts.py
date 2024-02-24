# En el archivo generate_charts.py

import matplotlib.pyplot as plt
import json
import os

# Cargar datos del archivo JSON
with open('dashboard_data.json', 'r') as file:
    data = json.load(file)

# Asegúrate de que existe un directorio para los gráficos
os.makedirs('static/charts', exist_ok=True)

# Modifica cada función para guardar los gráficos como imágenes
def save_market_share(data):
    # ... código para generar el gráfico ...
    plt.savefig('static/charts/market_share.png')

# Repite para las otras funciones
# ...

# Llama a las funciones para guardar los gráficos
save_market_share(data)
# ...
