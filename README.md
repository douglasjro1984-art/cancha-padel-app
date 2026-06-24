# 🎾 Cancha Pádel App - Documentación del Proyecto

Aplicación monolítica local desarrollada en Python y Flask para la gestión automatizada de reservas de canchas de pádel.

---

## 📅 SPRINT 1: Maquetación, Estructura Inicial y Base de Datos (Entregado)

En la primera etapa del proyecto se definieron las bases del diseño visual, la arquitectura de carpetas y el modelado inicial de los datos.

### Hitos Alcanzados:
* **Estructura del Proyecto:** Creación de los directorios raíz, configuración de carpetas para archivos estáticos (`static/css`) y de servidor (`src/`).
* **Diseño e Interfaz de Usuario (UI):** Creación de la vista principal `reservas.html` utilizando HTML5 semántico. Implementación de una hoja de estilos `estilos.css` con diseño deportivo optimizado para *Dark Mode*.
* **Modelado de Datos Inicial:** Diseño conceptual de las tablas esenciales para la persistencia local:
    * `usuarios`: Registro de nombres y datos de contacto de los jugadores.
    * `reservas`: Gestión de canchas, fechas y horarios asignados.
* **Resultados:** Interfaz estática funcional que sirve como maqueta para la interacción del usuario.

---

## 📅 SPRINT 2: Lógica de Control, Validaciones y Conexión DB (Actual)

En este sprint se transformó la maqueta estática en una aplicación dinámica y funcional en `localhost`, blindando el sistema contra datos erróneos.

### Características del Módulo:
* **Arquitectura Desacoplada:** Separación limpia de responsabilidades entre el servidor (`src/app.py`), las consultas SQL (`src/database/queries.py`) y la interfaz gráfica.
* **Reglas de Negocio en Backend:** * Validación obligatoria de campos vacíos en el formulario.
    * Control temporal: Bloqueo absoluto de reservas para fechas del pasado.
    * Control de franja horaria: Reservas permitidas únicamente dentro del horario comercial del club (**08:00 a 23:00 hs**).
* **Persistencia e Integración Segura:** Inserción real de datos en la base local (SQLite3) incluyendo el campo `telefono`. Uso de la restricción `UNIQUE` en la base de datos para impedir turnos duplicados.
* **Sistema de Alertas Dinámicas:** Inyección de mensajes informativos (`flash` de Flask) de éxito (verdes) o error (rojas) integrados al diseño visual.

---
## 🛠️ Guía Paso a Paso para Ejecutar la Aplicación

Seguí estas instrucciones detalladas desde tu terminal para poner en marcha el proyecto en tu máquina local.

### Paso 1: Clonar y posicionarse en el proyecto
Abrí tu terminal (PowerShell o CMD) y asegurate de estar parado dentro de la carpeta raíz del proyecto:
```powershell
https://github.com/douglasjro1984-art/cancha-padel-app.git

## 📁 Estructura Actual del Directorio

```text
cancha-padel-app/
├── src/
│   ├── database/
│   │   ├── init_db.py       # Inicializador y limpiador de tablas SQL
│   │   └── queries.py       # Consultas e inserciones de la base de datos
│   ├── templates/
│   │   └── reservas.html    # Interfaz de usuario (Formulario y Alertas)
│   └── app.py               # Servidor y lógica de control de Flask
├── static/
│   └── css/
│       └── estilos.css      # Estilos visuales integrados (Dark Mode)
├── cancha_padel.db          # Base de datos local (SQLite3)
├── requirements.txt         # Congelamiento del entorno de desarrollo
└── run.py                   # Lanzador global del proyecto