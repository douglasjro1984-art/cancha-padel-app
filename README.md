aplicacion-padel-cancha/
│
├── src/                        # Código fuente de la aplicación
│   ├── __init__.py             # Inicializador del paquete Python
│   ├── app.py                  # Archivo principal que levanta el servidor (Backend)
│   │
│   ├── database/               # Módulo de la Base de Datos
│   │   ├── __init__.py
│   │   ├── conexion.py         # Lógica de conexión a la BD interna
│   │   └── queries.py          # Consultas SQL (Insertar, consultar disponibilidad)
│   │
│   ├── static/                 # Archivos estáticos que lee el navegador (Frontend)
│   │   ├── css/
│   │   │   └── estilos.css     # Estilos de la interfaz
│   │   └── js/
│   │       └── main.js         # JavaScript opcional para validaciones extras
│   │
│   └── templates/              # Vistas o pantallas del sistema (Frontend)
│       ├── base.html           # Estructura HTML base (Navbar, Footer)
│       ├── index.html          # Pantalla de inicio / Bienvenida
│       └── reservas.html       # Formulario para pedir los turnos
│
├── tests/                      # Espacio de trabajo del Tester
│   └── test_funcionales.py     # Scripts o anotaciones de pruebas del QA
│
├── .gitignore                  # Archivos que Git debe ignorar (Entornos virtuales, caché)
├── LEAME.md                    # Documentación del proyecto (Readme)
└── requirements.txt            # Dependencias y librerías de Python a instalar
