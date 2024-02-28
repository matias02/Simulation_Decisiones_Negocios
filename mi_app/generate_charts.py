# generate_charts.py
import matplotlib.pyplot as plt
import json
import os

# Define la ruta del directorio de gráficos estáticos
STATIC_DIR = os.path.join('static', 'charts')
os.makedirs(STATIC_DIR, exist_ok=True)

# Carga los datos del archivo JSON
with open('dashboard_data.json', 'r') as file:
    data = json.load(file)

# Función para guardar el gráfico de Market Share
def save_market_share(data):
    labels = [f"Year {item['year']}" for item in data['market_share']]
    sizes = [item['value'] for item in data['market_share']]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.set_title('Market Share')
    plt.savefig(os.path.join(STATIC_DIR, 'market_share.png'))
    plt.close()

# Repite para las demás funciones de gráficos...

# Ejecuta las funciones para generar y guardar los gráficos
save_market_share(data)
# ... y así sucesivamente para las otras funciones de gráficos ...
