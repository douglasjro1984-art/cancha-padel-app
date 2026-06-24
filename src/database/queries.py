import sqlite3
import os

def conectar_bd():
    """Establece la conexión absoluta con el archivo de la base de datos."""
    ruta_bd = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../cancha_padel.db'))
    return sqlite3.connect(ruta_bd)

def verificar_disponibilidad(cancha_id, fecha, hora):
    """Comprueba si ya existe una reserva idéntica para esa cancha y horario."""
    conexion = conectar_bd()
    cursor = conexion.cursor()
    
    cursor.execute('''
        SELECT 1 FROM reservas 
        WHERE cancha_id = ? AND fecha = ? AND hora = ?
    ''', (cancha_id, fecha, hora))
    
    resultado = cursor.fetchone()
    conexion.close()
    return resultado is None  # Devuelve True si está disponible

def registrar_usuario(nombre, telefono=""):
    """Registra al jugador y devuelve su ID asignado."""
    conexion = conectar_bd()
    cursor = conexion.cursor()
    
    cursor.execute('''
        INSERT INTO usuarios (nombre, telefono) 
        VALUES (?, ?)
    ''', (nombre, telefono))
    
    usuario_id = cursor.lastrowid
    conexion.commit()
    conexion.close()
    return usuario_id

def guardar_reserva(usuario_id, cancha_id, fecha, hora):
    """Asienta la reserva definitiva vinculando el usuario y el turno."""
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        
        cursor.execute('''
            INSERT INTO reservas (usuario_id, cancha_id, fecha, hora) 
            VALUES (?, ?, ?, ?)
        ''', (usuario_id, cancha_id, fecha, hora))
        
        conexion.commit()
        conexion.close()
        return True
    except sqlite3.IntegrityError:
        # En caso de que se intente violar la restricción UNIQUE en localhost
        return False