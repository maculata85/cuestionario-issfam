import random
import os
import time
import traceback # Módulo para el diagnóstico de errores

# --- Carga de la base de preguntas ---
try:
    # Este bloque intenta importar la lista de preguntas desde el otro archivo.
    from base_de_preguntas import BASE_DE_PREGUNTAS
except ImportError:
    print("Error Fatal: No se encontró el archivo 'base_de_preguntas.py'.")
    print("Asegúrate de que ambos archivos ('cuestionario_final.py' y 'base_de_preguntas.py') estén en la misma carpeta.")
    input("Presiona Enter para salir.")
    exit()

NUM_PREGUNTAS_EXAMEN = 15

# --- Arte ASCII para los resultados ---
ARTE_EXCELENTE = """
      ___________
     '._==_==_=_.'
     .-\\:      /-.
    | (|:.     |) |
     '-|:.     |-'
       \\::.    /
        '::. .'
          ) (
        _.' '._
       `"""""""`
¡EXCELENTE! Eres un maestro en la materia.
"""

ARTE_REGULAR = """
      .---.
     /     \\
     \\.@-@./
     /`\\_/`\\
    //  _  \\\\
   | \\     )|
  /`-_`>  <`_-\\
  \\___)=(___/
Estudia un poco más los temas señalados. ¡Vas por buen camino!
"""

ARTE_MALO = """
     .-.
    (o.o)
     | |
     '-'
De plano estas bien perdido, ¡ponte a estudiar!
"""

def limpiar_pantalla():
    """Limpia la consola para una mejor experiencia de usuario."""
    os.system('cls' if os.name == 'nt' else 'clear')

def seleccionar_dificultad_y_vidas():
    """Pide al usuario que elija la dificultad y asigna las vidas correspondientes."""
    print("Elige un nivel de dificultad para tu examen:")
    print("1. Fácil (3 vidas 💚💚💚)")
    print("2. Intermedio (2 vidas 💛💛)")
    print("3. Difícil (1 vida ❤️)")
    print("4. Dios (0 vidas ☠️ - No hay margen de error)")
    print("5. Todos (2 vidas 💛💛)")
    
    opciones_map = {
        '1': ("facil", 3), '2': ("intermedio", 2),
        '3': ("dificil", 1), '4': ("dios", 0), '5': ("todos", 2)
    }
    
    while True:
        eleccion = input("Ingresa el número de tu elección (1-5): ")
        if eleccion in opciones_map:
            return opciones_map[eleccion]
        else:
            print("Opción no válida. Por favor, ingresa un número del 1 al 5.")

def preparar_examen(dificultad, total_preguntas):
    """Filtra y selecciona las preguntas para el examen."""
    if not total_preguntas:
        print("\n❌ Error: La base de datos de preguntas está vacía.")
        return None

    if dificultad == "todos":
        preguntas_filtradas = total_preguntas
    else:
        preguntas_filtradas = [p for p in total_preguntas if p.get('dificultad') == dificultad]

    if len(preguntas_filtradas) < 1:
        print(f"\n❌ Error: No se encontraron preguntas para el nivel '{dificultad}'.")
        return None
        
    if len(preguntas_filtradas) < NUM_PREGUNTAS_EXAMEN:
        print(f"\n⚠️ Advertencia: No hay suficientes preguntas ({len(preguntas_filtradas)}) para el nivel '{dificultad}'.")
        print(f"El examen se realizará con las {len(preguntas_filtradas)} preguntas disponibles.")

    num_a_seleccionar = min(NUM_PREGUNTAS_EXAMEN, len(preguntas_filtradas))
    random.shuffle(preguntas_filtradas)
    return preguntas_filtradas[:num_a_seleccionar]

def ejecutar_examen(preguntas, vidas_iniciales):
    """Lógica principal para correr el cuestionario. Siempre permite terminar."""
    puntaje = 0
    vidas = vidas_iniciales
    temas_a_repasar = set()
    
    for i, pregunta in enumerate(preguntas):
        limpiar_pantalla()
        
        # Lógica de visualización de vidas
        if vidas_iniciales > 0:
            vida_iconos = "❤️ " * vidas if vidas > 0 else "💔 ¡Última vida!"
            print(f"--- Pregunta {i + 1} de {len(preguntas)} --- | Vidas: {vida_iconos}")
        else:
            vida_iconos = "☠️"
            print(f"--- Pregunta {i + 1} de {len(preguntas)} --- | Vidas: {vida_iconos} (MODO DIOS)")

        print(f"Puntaje actual: {puntaje}\n")
        print(f"Tema: {pregunta['tema']}\n")
        print(f"P: {pregunta['pregunta']}\n")

        # Desordenar opciones y encontrar la correcta
        opciones = list(pregunta['opciones'])
        respuesta_correcta_texto = opciones[pregunta['respuesta_correcta']]
        random.shuffle(opciones)
        
        for j, opcion in enumerate(opciones):
            print(f"  {chr(65 + j)}) {opcion}")

        # Validar respuesta del usuario
        while True:
            respuesta_usuario = input("\nTu respuesta (A, B, C...): ").upper()
            if respuesta_usuario and respuesta_usuario in [chr(65 + k) for k in range(len(opciones))]:
                break
            else:
                print("Respuesta no válida. Inténtalo de nuevo.")
        
        indice_seleccionado = ord(respuesta_usuario) - 65
        opcion_seleccionada = opciones[indice_seleccionado]

        # Comprobar respuesta y actualizar estado
        if opcion_seleccionada == respuesta_correcta_texto:
            puntaje += 1
            print("\n¡Correcto! 👍")
        else:
            vidas -= 1
            temas_a_repasar.add(pregunta['tema'])
            print("\n¡Incorrecto! 👎")
            print(f"La respuesta correcta era: {respuesta_correcta_texto}")
        
        time.sleep(2)

    return puntaje, temas_a_repasar, vidas

def grafica_horizontal(correctas, total):
    """Genera una barra gráfica de texto para el resultado."""
    if total == 0: return ""
    
    porc_correctas = int((correctas / total) * 100)
    
    longitud_barra = 40
    bloques_correctos = int(longitud_barra * (porc_correctas / 100))
    
    barra = "🟩" * bloques_correctos + "🟥" * (longitud_barra - bloques_correctos)
    
    return f"Rendimiento [{barra}] {porc_correctas}%"

def mostrar_resultados(puntaje, total_preguntas, temas_a_repasar, vidas_finales, vidas_iniciales):
    """Muestra la calificación final, gráfica, arte ASCII y recomendaciones."""
    try:
        limpiar_pantalla()
        print("--- 🏁 Resultados Finales del Examen ---")
        
        if total_preguntas > 0:
            calificacion = (puntaje / total_preguntas) * 100
        else:
            calificacion = 0.0
        
        print("\n" + grafica_horizontal(puntaje, total_preguntas))
        print("-------------------------------------------")
        print(f"Respuestas correctas: {puntaje} de {total_preguntas}")
        if vidas_iniciales > 0:
            vidas_usadas = vidas_iniciales - max(0, vidas_finales)
            print(f"Vidas utilizadas: {vidas_usadas} de {vidas_iniciales}")
        print(f"Calificación: {calificacion:.2f} / 100.00")
        print("-------------------------------------------\n")

        if calificacion >= 90:
            print(ARTE_EXCELENTE)
        elif calificacion >= 60:
            print(ARTE_REGULAR)
        else:
            print(ARTE_MALO)

        if temas_a_repasar:
            print("\n💡 Sugerencias de Estudio:")
            print("Se recomienda repasar los siguientes temas donde cometiste errores:")
            for i, tema in enumerate(sorted(list(temas_a_repasar))):
                print(f"  {i+1}. {tema}")
        elif calificacion >= 90:
            print("\n¡Felicidades, no hay temas que repasar!")
        
    except Exception:
        print("\n\n          ¡ERROR INESPERADO AL GENERAR EL DIAGNÓSTICO!          ")
        print("===================================================================")
        print("Ha ocurrido un problema al intentar mostrar los resultados.")
        print("Por favor, copia TODO el siguiente mensaje de error y envíamelo para poder solucionarlo.")
        print("-------------------------------------------------------------------")
        traceback.print_exc()
        print("-------------------------------------------------------------------")

def main():
    """Función principal que orquesta el programa."""
    limpiar_pantalla()
    print("======================================================")
    print("   Bienvenido al Cuestionario de la Ley del ISSFAM    ")
    print("======================================================")
    
    dificultad, vidas_iniciales = seleccionar_dificultad_y_vidas()
    preguntas_del_examen = preparar_examen(dificultad, BASE_DE_PREGUNTAS)

    if preguntas_del_examen:
        total_preguntas_en_examen = len(preguntas_del_examen)
        print(f"\nIniciando examen nivel '{dificultad.capitalize()}' con {total_preguntas_en_examen} preguntas.")
        input("Presiona Enter para comenzar...")
        
        puntaje_final, temas_para_repasar, vidas_restantes = ejecutar_examen(preguntas_del_examen, vidas_iniciales)
        
        mostrar_resultados(puntaje_final, total_preguntas_en_examen, temas_para_repasar, vidas_restantes, vidas_iniciales)
    else:
        print("\nNo se pudo iniciar el examen. Verifica tu archivo 'base_de_preguntas.py'.")
    
    # Pausa final para que el usuario pueda leer los resultados.
    input("\n\nEl diagnóstico ha finalizado. Presiona Enter para cerrar la ventana...")


if __name__ == "__main__":
    main()