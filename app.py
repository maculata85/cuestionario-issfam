# app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash

import random
from base_de_preguntas import BASE_DE_PREGUNTAS

app = Flask(__name__)
app.secret_key = 'clave_secreta_cambia_esto' # ¡IMPORTANTE! Cambia esto por una clave secreta fuerte y única en producción

NUM_PREGUNTAS_EXAMEN = 15

DIFICULTADES = {
    'facil': 3,
    'intermedio': 2,
    'dificil': 1,
    'dios': 0, # Modo Dios: 0 vidas
    'todos': 2
}

def preparar_examen(dificultad):
    """
    Filtra y selecciona las preguntas para el examen según la dificultad.
    """
    if dificultad == 'todos':
        preguntas = BASE_DE_PREGUNTAS[:] # Copia completa si es "todos"
    else:
        preguntas = [p for p in BASE_DE_PREGUNTAS if p['dificultad'] == dificultad]

    random.shuffle(preguntas)
    return preguntas[:min(NUM_PREGUNTAS_EXAMEN, len(preguntas))]

@app.route('/')
def inicio():
    """
    Ruta para la página de inicio, donde se selecciona la dificultad.
    """
    return render_template('inicio.html')

@app.route('/examen', methods=['POST'])
def examen():
    """
    Ruta para iniciar el examen, procesa la selección de dificultad y prepara la sesión.
    """
    dificultad = request.form['dificultad']
    preguntas = preparar_examen(dificultad)
    vidas = DIFICULTADES[dificultad]

    # Inicializa las variables de sesión para el nuevo examen
    session['preguntas'] = preguntas
    session['respuestas'] = []
    session['vidas'] = vidas
    session['dificultad'] = dificultad
    session['indice_pregunta_actual'] = 0 # Almacena el índice de la pregunta actual

    # Redirige a la primera pregunta
    return redirect(url_for('mostrar_pregunta'))

@app.route('/pregunta', methods=['GET', 'POST'])
def mostrar_pregunta():
    """
    Ruta para mostrar una pregunta y procesar su respuesta.
    """
    preguntas = session.get('preguntas')
    respuestas = session.get('respuestas', [])
    vidas = session.get('vidas')
    dificultad_actual = session.get('dificultad')
    indice_pregunta_actual = session.get('indice_pregunta_actual', 0)

    # --- Validación inicial de sesión para robustez ---
    if preguntas is None or vidas is None or dificultad_actual is None:
        flash('La sesión del examen ha expirado o no se ha iniciado. Por favor, comienza de nuevo.', 'warning')
        return redirect(url_for('inicio'))

    # --- Lógica de procesamiento de respuesta (si la solicitud es POST) ---
    if request.method == 'POST':
        seleccion = request.form.get('opcion')

        if seleccion is None:
            flash('Por favor, selecciona una opción antes de responder.', 'warning')
            return redirect(url_for('mostrar_pregunta'))

        pregunta_respondida_obj = preguntas[indice_pregunta_actual]
        correcta = pregunta_respondida_obj['opciones'][pregunta_respondida_obj['respuesta_correcta']]

        if seleccion != correcta:
            vidas -= 1
            session['vidas'] = vidas
            flash(f'¡Incorrecto! La respuesta correcta era: {correcta}', 'error')
        else:
            flash('¡Correcto!', 'success')

        respuestas.append({
            'pregunta': pregunta_respondida_obj['pregunta'],
            'seleccion': seleccion,
            'correcta': correcta,
            'tema': pregunta_respondida_obj['tema'],
            'acertada': seleccion == correcta
        })
        session['respuestas'] = respuestas

        # --- Lógica de avance a la siguiente pregunta o fin del examen ---
        siguiente_indice = indice_pregunta_actual + 1
        session['indice_pregunta_actual'] = siguiente_indice # Actualizar el índice en la sesión

        # VERIFICACIÓN DE FIN DE EXAMEN DESPUÉS DE PROCESAR LA RESPUESTA
        # Y AVANZAR AL SIGUIENTE ÍNDICE.
        # Si las vidas son NEGATIVAS (ej. Modo Dios se equivocó en la primera)
        # o ya no hay más preguntas.
        if vidas < 0 or siguiente_indice >= len(preguntas):
            return redirect(url_for('resultado'))
        else:
            return redirect(url_for('mostrar_pregunta'))

    # --- Lógica para mostrar la pregunta actual (si la solicitud es GET) ---
    # VERIFICACIÓN DE FIN DE EXAMEN AL CARGAR LA PÁGINA VÍA GET (ej. recargar o navegar directamente)
    #
    # Redirigir a 'resultado' si:
    # 1. Ya no hay más preguntas que mostrar (se llegó al final).
    # 2. Las vidas son 0 o menos Y NO ES EL MODO DIOS O YA SE HA RESPONDIDO AL MENOS UNA PREGUNTA.
    #    Esto permite que el Modo Dios con 0 vidas inicie la primera pregunta.
    if indice_pregunta_actual >= len(preguntas) or \
       (vidas <= 0 and dificultad_actual != 'dios' and indice_pregunta_actual > 0) or \
       (vidas <= 0 and dificultad_actual == 'dios' and indice_pregunta_actual > 0): # redundante pero explicativo
        return redirect(url_for('resultado'))

    # Si se llegó a 0 vidas en modo normal (no Dios) en la primera pregunta (indice 0),
    # también se debe redirigir a resultados.
    if vidas <= 0 and dificultad_actual != 'dios' and indice_pregunta_actual == 0:
        return redirect(url_for('resultado'))

    # Preparar la pregunta para mostrar
    pregunta_a_mostrar = preguntas[indice_pregunta_actual]
    opciones = pregunta_a_mostrar['opciones'][:]
    random.shuffle(opciones)

    return render_template('examen.html',
                           num=indice_pregunta_actual,
                           total=len(preguntas),
                           pregunta=pregunta_a_mostrar['pregunta'],
                           opciones=opciones,
                           tema=pregunta_a_mostrar['tema'],
                           vidas=vidas,
                           dificultad_actual=dificultad_actual,
                           DIFICULTADES=DIFICULTADES)

@app.route('/resultado')
def resultado():
    """
    Ruta para mostrar los resultados finales del examen.
    """
    respuestas = session.get('respuestas', [])
    vidas = session.get('vidas', 0)
    total = len(respuestas)
    correctas = sum(1 for r in respuestas if r['acertada'])
    temas = sorted(set(r['tema'] for r in respuestas if not r['acertada']))
    porcentaje = (correctas / total) * 100 if total > 0 else 0

    # Limpiar la sesión al finalizar el examen para que no arrastre datos viejos
    session.pop('preguntas', None)
    session.pop('respuestas', None)
    session.pop('vidas', None)
    session.pop('dificultad', None)
    session.pop('indice_pregunta_actual', None)

    return render_template('resultado.html', correctas=correctas, total=total,
                           vidas=vidas, porcentaje=porcentaje, temas=temas)

if __name__ == '__main__':
    app.run(debug=True)