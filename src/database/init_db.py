import sqlite3
import os

def inicializar_bd():
    ruta_bd = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../cancha_padel.db'))
    
    # Eliminamos la base de datos vieja si existe para evitar conflictos de columnas
    if os.path.exists(ruta_bd):
        os.remove(ruta_bd)
        print("Eliminando base de datos antigua obsoleta...")

    conexion = sqlite3.connect(ruta_bd)
    cursor = conexion.cursor()

    # Tabla Usuarios completa
    cursor.execute('''
        CREATE TABLE usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT
        )
    ''')

    # Tabla Reservas completa con claves foráneas
    cursor.execute('''
        CREATE TABLE reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            cancha_id INTEGER NOT NULL,
            fecha TEXT NOT NULL,
            hora TEXT NOT NULL,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
            UNIQUE(cancha_id, fecha, hora)
        )
    ''')

    conexion.commit()
    conexion.close()
    print("¡Base de datos 'cancha_padel.db' inicializada de cero con todas sus columnas!")

if __name__ == '__main__':
    inicializar_bd()