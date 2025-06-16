# app.py
from flask import Flask, render_template, request, redirect, url_for, session
import random
from base_de_preguntas import BASE_DE_PREGUNTAS

app = Flask(__name__)
app.secret_key = 'clave_secreta_cambia_esto'

NUM_PREGUNTAS_EXAMEN = 15

DIFICULTADES = {
    'facil': 3,
    'intermedio': 2,
    'dificil': 1,
    'dios': 0,
    'todos': 2
}

def preparar_examen(dificultad):
    if dificultad == 'todos':
        preguntas = BASE_DE_PREGUNTAS[:]
    else:
        preguntas = [p for p in BASE_DE_PREGUNTAS if p['dificultad'] == dificultad]

    random.shuffle(preguntas)
    return preguntas[:min(NUM_PREGUNTAS_EXAMEN, len(preguntas))]

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/examen', methods=['POST'])
def examen():
    dificultad = request.form['dificultad']
    preguntas = preparar_examen(dificultad)
    vidas = DIFICULTADES[dificultad]

    session['preguntas'] = preguntas
    session['respuestas'] = []
    session['vidas'] = vidas
    session['dificultad'] = dificultad
    return redirect(url_for('mostrar_pregunta', num=0))

@app.route('/pregunta/<int:num>', methods=['GET', 'POST'])
def mostrar_pregunta(num):
    preguntas = session.get('preguntas')
    respuestas = session.get('respuestas', [])
    vidas = session.get('vidas')

    if request.method == 'POST':
        seleccion = request.form['opcion']
        correcta = preguntas[num - 1]['opciones'][preguntas[num - 1]['respuesta_correcta']]
        if seleccion != correcta:
            vidas -= 1
            session['vidas'] = vidas
        respuestas.append({
            'pregunta': preguntas[num - 1]['pregunta'],
            'seleccion': seleccion,
            'correcta': correcta,
            'tema': preguntas[num - 1]['tema'],
            'acertada': seleccion == correcta
        })
        session['respuestas'] = respuestas

    if vidas == 0 or num >= len(preguntas):
        return redirect(url_for('resultado'))

    opciones = preguntas[num]['opciones'][:]
    random.shuffle(opciones)
    return render_template('examen.html', num=num, total=len(preguntas),
                           pregunta=preguntas[num]['pregunta'],
                           opciones=opciones, tema=preguntas[num]['tema'], vidas=vidas)

@app.route('/resultado')
def resultado():
    respuestas = session.get('respuestas', [])
    vidas = session.get('vidas', 0)
    total = len(respuestas)
    correctas = sum(1 for r in respuestas if r['acertada'])
    temas = sorted(set(r['tema'] for r in respuestas if not r['acertada']))
    porcentaje = (correctas / total) * 100 if total > 0 else 0

    return render_template('resultado.html', correctas=correctas, total=total,
                           vidas=vidas, porcentaje=porcentaje, temas=temas)

if __name__ == '__main__':
    app.run(debug=True)


# templates/inicio.html
'''
<!DOCTYPE html>
<html>
<head><title>Inicio</title></head>
<body>
  <h2>Cuestionario de la Ley del ISSFAM</h2>
  <form method="POST" action="/examen">
    <label>Elige dificultad:</label><br>
    <select name="dificultad">
      <option value="facil">Fácil</option>
      <option value="intermedio">Intermedio</option>
      <option value="dificil">Difícil</option>
      <option value="dios">Dios</option>
      <option value="todos">Todos</option>
    </select><br><br>
    <button type="submit">Iniciar Examen</button>
  </form>
</body>
</html>
'''


# templates/examen.html
'''
<!DOCTYPE html>
<html>
<head><title>Pregunta {{ num+1 }}</title></head>
<body>
  <h2>Pregunta {{ num+1 }} de {{ total }}</h2>
  <p><strong>Tema:</strong> {{ tema }}</p>
  <p>{{ pregunta }}</p>
  <form method="POST">
    {% for opcion in opciones %}
      <label><input type="radio" name="opcion" value="{{ opcion }}" required> {{ opcion }}</label><br>
    {% endfor %}
    <br><button type="submit">Responder</button>
  </form>
  <p>Vidas restantes: {{ vidas }}</p>
</body>
</html>
'''


# templates/resultado.html
'''
<!DOCTYPE html>
<html>
<head><title>Resultado</title></head>
<body>
  <h2>Resultados del Examen</h2>
  <p>Respuestas correctas: {{ correctas }} de {{ total }}</p>
  <p>Porcentaje: {{ porcentaje|round(2) }}%</p>
  <p>Vidas restantes: {{ vidas }}</p>

  {% if temas %}
    <h3>Temas a repasar:</h3>
    <ul>
      {% for tema in temas %}
        <li>{{ tema }}</li>
      {% endfor %}
    </ul>
  {% else %}
    <p>¡Felicidades! No tienes temas que repasar.</p>
  {% endif %}

  <a href="/">Volver a empezar</a>
</body>
</html>
'''
