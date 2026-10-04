# Cancha de pádel, reserva de turnos y alquiler de indumentaria

Aplicación web para gestionar una cancha de pádel: reserva de turnos y alquiler de indumentaria deportiva.

## Qué hace

- Reserva de turnos de la cancha.
- Alquiler de indumentaria deportiva.

## Autor

**Douglas Romero**, desarrollador backend junior.
[GitHub](https://github.com/douglasjro1984-art) · [LinkedIn](https://www.linkedin.com/in/douglas-romero-574576384)aplicacion-

padel-cancha/
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
