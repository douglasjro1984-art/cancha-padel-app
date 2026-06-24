import sys
import os

# Registramos la raíz y 'src' de manera absoluta
ruta_raiz = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(ruta_raiz, 'src'))

# Importación explícita desde el paquete src
from src.app import app

if __name__ == '__main__':
    app.run(debug=True, port=5001)