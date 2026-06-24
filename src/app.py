from flask import Flask, render_template, request, redirect, url_for, flash
from src.database.queries import verificar_disponibilidad, registrar_usuario, guardar_reserva

app = Flask(__name__, static_folder='../static', template_folder='templates')
app.secret_key = 'clave_secreta_padel_app'

@app.route('/')
def inicio():
    return redirect(url_for('pantalla_reservas'))

@app.route('/reservas', methods=['GET'])
def pantalla_reservas():
    return render_template('reservas.html')

@app.route('/reservas', methods=['POST'])
def procesar_reserva():
    nombre = request.form.get('nombre', '').strip()
    cancha_id = request.form.get('cancha_id')
    fecha = request.form.get('fecha')
    hora = request.form.get('hora')

    if not nombre or not cancha_id or not fecha or not hora:
        flash("Todos los campos son obligatorios.", "error")
        return redirect(url_for('pantalla_reservas'))

    # Validación de disponibilidad
    if not verificar_disponibilidad(cancha_id, fecha, hora):
        flash(f"La cancha elegida ya está ocupada para el {fecha} a las {hora} hs.", "error")
        return redirect(url_for('pantalla_reservas'))

    # Flujo de base de datos exitoso
    usuario_id = registrar_usuario(nombre)
    exito = guardar_reserva(usuario_id, cancha_id, fecha, hora)

    if exito:
        flash(f"¡Reserva confirmada con éxito para {nombre}! Turno asentado. 🎾", "success")
    else:
        flash("Hubo un problema interno al procesar tu reserva.", "error")
        
    return redirect(url_for('pantalla_reservas'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
    