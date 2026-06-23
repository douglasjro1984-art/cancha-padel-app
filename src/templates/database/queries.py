import sqlite3

DATABASE_NAME = "cancha_padel.db"

def verificar_disponibilidad(cancha_id, fecha, hora):
    """Devuelve True si la cancha está libre, o False si ya está reservada."""
    conexion = sqlite3.connect(DATABASE_NAME)
    cursor = conexion.cursor()
    
    cursor.execute('''
        SELECT COUNT(*) FROM reservas 
        WHERE cancha_id = ? AND fecha = ? AND hora = ?
    ''', (cancha_id, fecha, hora))
    
    existe = cursor.fetchone()[0]
    conexion.close()
    
    return existe == 0  # True si está libre (cero filas encontradas)


def registrar_usuario(nombre, telefono=""):
    """Inserta un usuario y devuelve su ID generado."""
    conexion = sqlite3.connect(DATABASE_NAME)
    cursor = conexion.cursor()
    
    cursor.execute('''
        INSERT INTO usuarios (nombre, telefono) 
        VALUES (?, ?)
    ''', (nombre, telefono))
    
    usuario_id = cursor.lastrowid  # Captura el ID autoincremental
    conexion.commit()
    conexion.close()
    
    return usuario_id


def guardar_reserva(usuario_id, cancha_id, fecha, hora):
    """Inserta la reserva final en la base de datos."""
    conexion = sqlite3.connect(DATABASE_NAME)
    cursor = conexion.cursor()
    
    try:
        cursor.execute('''
            INSERT INTO reservas (usuario_id, cancha_id, fecha, hora) 
            VALUES (?, ?, ?, ?)
        ''', (usuario_id, cancha_id, fecha, hora))
        conexion.commit()
        exito = True
    except sqlite3.IntegrityError:
        # Falla si se intenta duplicar por la restricción UNIQUE
        exito = False
    finally:
        conexion.close()
        
    return exito