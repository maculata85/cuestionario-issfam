# -*- coding: utf-8 -*-
"""
Este archivo contiene la base de datos completa con 350 preguntas y respuestas 
para el cuestionario sobre la Ley del ISSFAM.
"""

BASE_DE_PREGUNTAS = [
    # Bloque de Preguntas 1 (1-50)
    {
        "pregunta": "¿Qué tipo de organismo es el Instituto de Seguridad Social para las Fuerzas Armadas Mexicanas (ISSFAM) según el Artículo 1?",
        "opciones": ["Una secretaría de estado", "Un organismo público descentralizado federal", "Una empresa privada con fines sociales"],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Disposiciones Generales"
    },
    {
        "pregunta": "¿Según el Artículo 4, quiénes son considerados \"Militares\"?",
        "opciones": ["Solo el personal del Ejército y Fuerza Aérea", "Únicamente los Generales y Almirantes", "Los miembros del Ejército, de la Fuerza Aérea y de la Armada de México"],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Definiciones Clave"
    },
    {
        "pregunta": "De acuerdo con el Artículo 18, ¿cuál de las siguientes es una de las prestaciones que otorga el ISSFAM?",
        "opciones": ["Haber de retiro", "Seguro de desempleo", "Subsidio para transporte público"],
        "respuesta_correcta": 0, "dificultad": "facil", "tema": "Tipos de Prestaciones"
    },
    {
        "pregunta": "El Artículo 21 define \"Retiro\" como la facultad que tiene el Estado para...",
        "opciones": ["Premiar a los militares por su servicio", "Enviar a los militares a misiones en el extranjero", "Separar del activo a los militares al ocurrir alguna de las causales previstas en esta Ley"],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Retiro y Compensación"
    },
    {
        "pregunta": "¿Cuál es la edad límite para permanecer en el activo para un General de División, según la tabla del Artículo 25?",
        "opciones": ["60 años", "63 años", "65 años"],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Causas de Retiro"
    },
    {
        "pregunta": "El Artículo 5, define que el órgano de Gobierno del Instituto es la...",
        "opciones": ["Dirección General", "Asamblea de Militares Retirados", "Junta Directiva"],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Estructura del Instituto"
    },
    {
        "pregunta": "¿Qué es un \"Derechohabiente\" según el Artículo 4, Fracción VI?",
        "opciones": ["Cualquier ciudadano mexicano", "Familiares en línea directa (esposa, esposo, hijos, etc.) que tienen derecho a los beneficios de la Ley", "Una persona designada para recibir un beneficio económico por voluntad del militar"],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Definiciones Clave"
    },
    {
        "pregunta": "El Artículo 60 define el Seguro de Vida Militar como una prestación que proporciona un beneficio económico por...",
        "opciones": ["El fallecimiento del militar, cualquiera que sea la causa de la muerte", "Accidentes ocurridos únicamente en actos del servicio", "La jubilación del militar después de 40 años de servicio"],
        "respuesta_correcta": 0, "dificultad": "facil", "tema": "Seguros"
    },
    {
        "pregunta": "¿Quién administra el Fondo de la Vivienda para los miembros del activo de las Fuerzas Armadas según el Artículo 2, Fracción IV?",
        "opciones": ["La Secretaría de Hacienda y Crédito Público", "El Instituto (ISSFAM)", "El Banco de México"],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Funciones del Instituto"
    },
    {
        "pregunta": "¿Según el Artículo 38, quiénes son considerados familiares de los militares para efectos de pensión?",
        "opciones": ["Únicamente la viuda y los hijos menores de edad", "La viuda o viudo, concubina o concubinario, hijos, padres y en algunos casos hermanos", "Solamente los padres si dependían económicamente del militar"],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Pensiones y Familiares"
    },
    {
        "pregunta": "De acuerdo al Artículo 8, ¿quién designa al comisario público propietario y suplente del órgano de vigilancia del Instituto?",
        "opciones": ["La Junta Directiva", "El Director General del Instituto", "La Secretaría de la Función Pública"],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Estructura del Instituto"
    },
    {
        "pregunta": "¿Qué es la \"Pensión\" según el Artículo 21?",
        "opciones": ["Un pago único que se da al retirarse", "La prestación económica vitalicia a la que tienen derecho los familiares de los militares", "Un sinónimo de \"Haber de retiro\""],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Retiro y Compensación"
    },
    {
        "pregunta": "El Artículo 13 indica que son atribuciones del Director General...",
        "opciones": ["Representar al Instituto", "Decidir las inversiones del Instituto", "Designar a los miembros de la Junta Directiva"],
        "respuesta_correcta": 0, "dificultad": "facil", "tema": "Estructura del Instituto"
    },
    {
        "pregunta": "¿Cuál es una de las causas de retiro forzoso mencionadas en el Artículo 24?",
        "opciones": ["Tener un segundo empleo", "Llegar a la edad límite que fija el artículo 25", "Solicitar un préstamo hipotecario"],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Causas de Retiro"
    },
    {
        "pregunta": "El Artículo 59 establece que para constituir el fondo de ahorro, los Generales, Jefes y Oficiales deben aportar una cuota quincenal del:",
        "opciones": ["10% de sus haberes", "6% de sus haberes", "1% de sus haberes"],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Fondos y Ahorro"
    },
    {
        "pregunta": "El patrimonio del Instituto, según el Artículo 3, se constituye por varios conceptos. ¿Cuál de los siguientes NO es uno de ellos?",
        "opciones": ["Cuotas de los militares y aportaciones del Gobierno Federal", "Los fondos del seguro de vida militar y de la vivienda militar", "Donaciones de gobiernos extranjeros"],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Patrimonio del Instituto"
    },
    {
        "pregunta": "El Artículo 5 establece que la Junta Directiva se integra por nueve miembros. ¿Cómo se distribuye su designación?",
        "opciones": ["Nueve miembros designados por la Presidencia de la República", "Cinco por la SEDENA y cuatro por SEMAR", "Tres por la Secretaría de la Defensa Nacional, tres por la de Marina y tres por la de Hacienda y Crédito Público"],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Estructura del Instituto"
    },
    {
        "pregunta": "¿En qué caso un militar retirado puede volver al activo, según el Artículo 30?",
        "opciones": ["Si lo solicita voluntariamente después de 5 años de retiro", "Cuando las necesidades de la Nación lo exijan, mediante acuerdo suscrito por el Presidente de la República", "Automáticamente si recupera su salud, sin necesidad de un nuevo acuerdo"],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Retiro y Compensación"
    },
    {
        "pregunta": "Un militar con 25 años de servicios solicita su retiro voluntario. Según la tabla del Artículo 35, ¿qué porcentaje de haber de retiro le corresponde?",
        "opciones": ["60%", "75%", "100%"],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Cálculo de Beneficios"
    },
    {
        "pregunta": "Para que una concubina tenga derecho a pensión según el Art. 38, Frac. II, debe haber vida marital por un tiempo mínimo consecutivo anterior a la muerte del militar, ¿cuál es ese tiempo?",
        "opciones": ["Un año", "Tres años", "Cinco años consecutivos, o bien, haber procreado hijos"],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Pensiones y Familiares"
    },
    {
        "pregunta": "El Artículo 51 establece causas por las que se pierden los derechos a percibir beneficios de retiro. ¿Cuál es una de ellas?",
        "opciones": ["Cambiar de domicilio sin notificar", "Adquirir otra nacionalidad estando en activo", "Criticar públicamente a las Fuerzas Armadas"],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Pérdida de Derechos"
    },
    {
        "pregunta": "Según el Artículo 63, Fracción I, la suma asegurada del Seguro de Vida Militar por fallecimiento de un militar en activo equivale a:",
        "opciones": ["24 meses de haberes y sobrehaberes", "40 meses de haberes y sobrehaberes o del sueldo base de servidor público", "Un monto fijo establecido por la Junta Directiva cada año"],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Seguros"
    },
    {
        "pregunta": "¿Qué es la \"Compensación\" de acuerdo a la definición del Artículo 21?",
        "opciones": ["Una pensión mensual reducida para militares con menos de 20 años de servicio", "La prestación económica que se paga en una sola exhibición a militares (o sus familiares) que no alcanzan haber de retiro", "Un bono anual para todos los militares en situación de retiro"],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Retiro y Compensación"
    },
    {
        "pregunta": "¿Qué sucede con la parte de la pensión de un copartícipe cuyos derechos se extinguen, según el Artículo 41?",
        "opciones": ["Esa parte se reintegra al erario federal", "Se guarda en un fondo especial del Instituto", "Acrecentará proporcionalmente la de los demás beneficiarios"],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Pensiones y Familiares"
    },
    {
        "pregunta": "El Artículo 27 establece un ascenso al grado inmediato para efectos de retiro. Para un militar con 30 años de servicio, ¿cuántos años en el grado debe tener como mínimo para obtener este beneficio?",
        "opciones": ["3 años", "5 años", "10 años"],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Cálculo de Beneficios"
    },
    {
        "pregunta": "El Artículo 100, Fracción II, establece que el sistema de financiamiento de vivienda permite obtener crédito para varios fines, ¿cuál de los siguientes NO está incluido?",
        "opciones": ["La adquisición en propiedad de habitaciones", "La construcción, reparación, ampliación o mejoramiento de sus habitaciones", "La compra de un local comercial para el militar"],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Vivienda"
    },
    {
        "pregunta": "¿Qué familiares tienen derecho a la prestación de \"ayuda para gastos de sepelio\" en caso de su defunción, para un General, según el Artículo 57?",
        "opciones": ["Únicamente el cónyuge y los hijos", "El cónyuge, concubina, concubinario, padre, madre o algún hijo", "Cualquier familiar en línea directa hasta segundo grado"],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Otras Prestaciones"
    },
    {
        "pregunta": "¿Según el Artículo 39, pueden los padres concurrir con el cónyuge o los hijos para recibir una pensión?",
        "opciones": ["No, los familiares de la fracción I y II excluyen a los padres en todos los casos", "Sí, siempre que demuestren su dependencia económica con el militar", "Solo si el militar no tuvo hijos"],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Pensiones y Familiares"
    },
    {
        "pregunta": "El Artículo 52, Fracción IV, indica que el derecho a pensión para el cónyuge supérstite se pierde si...",
        "opciones": ["Consigue un nuevo empleo", "Contrae matrimonio o vive en concubinato", "Cambia de residencia a otro estado"],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Pérdida de Derechos"
    },
    {
        "pregunta": "De acuerdo con el Artículo 87, ¿en cuál de los siguientes casos NO se otorga la suma asegurada del Seguro Colectivo de Retiro?",
        "opciones": ["Militares que fallecen en actos del servicio, sin importar sus años de servicio", "Militares que solicitan su retiro con 20 o más años de servicio", "Militares que causan baja por haberla solicitado, sin importar el tiempo de servicios"],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Seguros"
    },
    {
        "pregunta": "El Artículo 111 establece un seguro que cubre los créditos de vivienda. ¿En qué casos libera al militar o a sus beneficiarios de las obligaciones del crédito?",
        "opciones": ["En caso de retiro voluntario después de 30 años de servicio", "Para los casos de inutilización permanente y total para el servicio activo, así como para los casos de muerte", "Si el militar es ascendido al grado inmediato superior"],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Vivienda"
    },
    {
        "pregunta": "El Artículo 36 señala que los militares con 5 o más años de servicio, sin llegar a veinte, tienen derecho a compensación. ¿Cuál de las siguientes es una causa válida para recibirla?",
        "opciones": ["Solicitarla voluntariamente para emprender un negocio", "Haberse incapacitado en actos fuera de servicio", "Ser ascendido al grado inmediato"],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Retiro y Compensación"
    },
    {
        "pregunta": "El Artículo 12, Fracción VI, establece que la Junta Directiva puede autorizar créditos con cargo al Fondo de la Vivienda a plazos de hasta:",
        "opciones": ["10 años", "20 años", "30 años"],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Estructura y Facultades"
    },
    {
        "pregunta": "¿En qué consiste la prestación \"Pagas de defunción\" descrita en el Artículo 55?",
        "opciones": ["El pago de la pensión completa por un año", "El equivalente a cuatro meses del haber y del sobrehaber del militar fallecido para gastos de sepelio", "La cobertura total de los gastos funerarios por parte del Instituto, sin límite de monto"],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Otras Prestaciones"
    },
    {
        "pregunta": "Un militar fallece en activo. Sus familiares tienen derecho a pensión. Según el Art. 31, Fracción IV, ¿cómo se integra la base para el cálculo de dicha pensión?",
        "opciones": ["Se toma el 100% del haber del grado y se le suma un 60% de dicho haber.", "Se calcula únicamente con el 100% del haber del grado que ostentaba, sin incluir primas ni asignaciones.", "Se toma como base el porcentaje del haber del grado que le hubiere correspondido en caso de retiro y se le adiciona el 80% de dicho haber, más primas y asignaciones que estuviera percibiendo."],
        "respuesta_correcta": 2, "dificultad": "dificil", "tema": "Cálculo de Beneficios"
    },
    {
        "pregunta": "Si un militar con 19 años de servicio fallece en un accidente automovilístico fuera de actos del servicio, ¿qué beneficio corresponde a sus familiares según los Artículos 36 y 40?",
        "opciones": ["Un haber de retiro equivalente al 95% del sueldo.", "Una pensión calculada con base en los años de servicio.", "Una compensación, ya que tenía menos de 20 años de servicio."],
        "respuesta_correcta": 2, "dificultad": "dificil", "tema": "Aplicación de la Ley (Retiro/Compensación)"
    },
    {
        "pregunta": "Según el Artículo 30, si un militar que recibió compensación en su primer retiro vuelve al activo, ¿qué obligación tiene respecto al monto cobrado?",
        "opciones": ["No tiene ninguna obligación de reintegrar el monto.", "Debe reintegrar solo el 50% del monto, mediante un pago único.", "Debe reintegrarlo totalmente mediante descuentos quincenales de un 25% en los haberes del activo."],
        "respuesta_correcta": 2, "dificultad": "dificil", "tema": "Retiro y Compensación"
    },
    {
        "pregunta": "Un hijo de militar, de 24 años, soltero, solicita continuar con el servicio médico. ¿Qué requisito INDISPENSABLE, además de la dependencia económica, debe comprobar anualmente según el Artículo 142, Fracción III?",
        "opciones": ["Estar buscando activamente empleo.", "Que se encuentra estudiando en instituciones oficiales o con reconocimiento de validez oficial.", "Haber iniciado el trámite para ingresar a las Fuerzas Armadas."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Servicio Médico"
    },
    {
        "pregunta": "El Artículo 33, Fracción III, otorga el 100% del haber de la jerarquía a militares incapacitados en actos del servicio. ¿Bajo qué condiciones un militar con incapacidad de SEGUNDA categoría alcanza este beneficio?",
        "opciones": ["Automáticamente al ser clasificado en segunda categoría.", "Si tiene 14 o más años de servicio.", "Si tiene menos de 10 años de servicio."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Cálculo de Beneficios por Incapacidad"
    },
    {
        "pregunta": "Dos personas reclaman pensión como cónyuges supérstites de un mismo militar, ambas con actas de matrimonio. Según el Artículo 43, ¿cómo procede el Instituto?",
        "opciones": ["Otorga la pensión a la persona que presentó primero la solicitud.", "Divide la pensión entre ambas personas hasta que un juez decida.", "Suspende el trámite del beneficio para el cónyuge hasta que se defina judicialmente la situación, pero puede continuar con los derechos de hijos y padres."],
        "respuesta_correcta": 2, "dificultad": "dificil", "tema": "Procedimientos y Controversias"
    },
    {
        "pregunta": "El Artículo 47 establece una condición para que los hijos adoptivos tengan derecho a los beneficios de esta Ley. ¿Cuál es?",
        "opciones": ["Que la adopción se haya hecho al menos 5 años antes del retiro del militar.", "Que la adopción se haya hecho por el militar antes de haber cumplido 45 años de edad.", "Que el hijo adoptivo sea menor de 10 años al momento de la adopción."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Requisitos de Familiares"
    },
    {
        "pregunta": "¿Cuál es la diferencia fundamental entre un \"Derechohabiente\" (Art. 4, Fracción VI) y un \"Beneficiario\" (Art. 4, Fracción VII)?",
        "opciones": ["Son términos sinónimos y se usan indistintamente en la ley.", "El \"Derechohabiente\" adquiere el derecho por parentesco y ley (pensión, servicio médico), mientras que el \"Beneficiario\" adquiere un derecho económico por voluntad expresa del militar (seguro de vida).", "El \"Beneficiario\" siempre tiene preferencia sobre el \"Derechohabiente\" para todas las prestaciones."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Análisis de Definiciones"
    },
    {
        "pregunta": "De acuerdo con el Artículo 91, ¿a quiénes se les devolverán sus aportaciones al Seguro Colectivo de Retiro MÁS un 20% de lo aportado?",
        "opciones": ["A militares que causen baja por mala conducta.", "A militares que causen baja definitiva por haber permanecido prófugos de la justicia.", "Al personal de tropa del Ejército que cause baja por haber cumplido su contrato de servicios."],
        "respuesta_correcta": 2, "dificultad": "dificil", "tema": "Seguros"
    },
    {
        "pregunta": "El Artículo 110 establece que los créditos de vivienda se darán por vencidos anticipadamente si el deudor incurre en ciertas acciones. ¿Cuál de las siguientes es una de ellas?",
        "opciones": ["Si el militar solicita un cambio de adscripción a otra ciudad.", "Si el deudor, sin el consentimiento del Instituto, enajena la vivienda o grava el inmueble.", "Si el militar recibe un ascenso y un aumento de sueldo."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Vivienda"
    },
    {
        "pregunta": "Un militar con 28 años de servicio y 6 años en el grado de Teniente Coronel pasa a situación de retiro. De acuerdo al Art. 27, ¿cómo se ve afectado su grado para efectos de retiro?",
        "opciones": ["Permanece como Teniente Coronel, ya que no cumple los años de servicio.", "Asciende al grado inmediato (Coronel) para efectos de retiro, pues cumple con los 28 años de servicio y un mínimo de 6 años en el grado.", "Asciende dos grados por su buen historial de servicio."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Aplicación de la Ley (Retiro)"
    },
    {
        "pregunta": "¿Qué sucede, según el artículo 173, si un militar fallece por una enfermedad 4 años después de haber realizado un servicio que presuntamente la causó?",
        "opciones": ["Se presume automáticamente la relación de causalidad entre el servicio y la muerte.", "La relación de causalidad debe probarse, ya que la presunción solo aplica si la muerte ocurre antes de transcurridos tres años de los hechos.", "El caso se desestima automáticamente por haber excedido el plazo."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Procedimientos y Causalidad"
    },
    {
        "pregunta": "Un militar está procesado en el fuero de guerra. ¿Puede tramitar su retiro voluntario según el Artículo 185?",
        "opciones": ["Sí, puede tramitarlo si renuncia a su defensa legal.", "No, no podrá tramitarse en tanto no se resuelva su responsabilidad penal por sentencia firme.", "Sí, pero su haber de retiro será retenido hasta que termine el juicio."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Procedimientos y Restricciones"
    },
    {
        "pregunta": "El artículo 212 establece la compatibilidad de pensiones. ¿Qué sucede si un militar retirado percibe indebidamente un haber de retiro y dos pensiones militares simultáneamente?",
        "opciones": ["Se le permite mantener los tres beneficios si su sueldo era bajo.", "Se le cancela el pago del o de los beneficios concedidos con posterioridad y debe reintegrar lo cobrado indebidamente mediante descuentos.", "Recibe una amonestación pero conserva todos los beneficios."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "De acuerdo con el Artículo 65, si a un militar se le paga la suma asegurada del seguro de vida por incapacidad, ¿qué sucede al momento de su fallecimiento?",
        "opciones": ["Sus beneficiarios reciben el 50% de la suma asegurada.", "El pago por incapacidad excluye el pago por fallecimiento.", "Sus beneficiarios reciben nuevamente el 100% de la suma asegurada."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Seguros"
    },
    {
        "pregunta": "Según el Artículo 192, cuando los familiares de un militar fallecido solicitan un beneficio, ¿qué instancia es la primera en resolver sobre la personalidad militar, jerarquía y situación del fallecido?",
        "opciones": ["El Instituto (ISSFAM) directamente.", "La Secretaría de Hacienda y Crédito Público (SHCP).", "La Dirección encargada de tramitar los retiros de la Secretaría de la Defensa Nacional o de Marina, según corresponda."],
        "respuesta_correcta": 2, "dificultad": "dificil", "tema": "Procedimientos"
    },
    # Bloque de Preguntas 2 (51-100)
    {
        "pregunta": "Según el Artículo 62, ¿quiénes tienen derecho al Seguro de Vida Militar?",
        "opciones": ["Solo los Generales y Jefes en activo.", "El personal militar en activo y en situación de retiro con derecho a haber de retiro.", "Únicamente el personal de tropa con más de 10 años de servicio."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Seguro de Vida Militar"
    },
    {
        "pregunta": "¿Qué es el régimen potestativo del seguro de vida militar, según el Artículo 69?",
        "opciones": ["Un seguro obligatorio para todos los familiares del militar.", "Un seguro al que pueden acogerse voluntariamente los militares con licencia especial o que causen baja con compensación.", "Un seguro para vehículos propiedad de los militares."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Seguro de Vida Militar"
    },
    {
        "pregunta": "Conforme al Artículo 77, si un militar muere sin haber designado beneficiarios para su seguro de vida, ¿quién tiene la primera prioridad para recibir el pago?",
        "opciones": ["Los hermanos.", "Los padres (madre y padre).", "El cónyuge o, si no lo hubiere, la concubina o concubinario, en concurrencia con los hijos."],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Seguro de Vida Militar"
    },
    {
        "pregunta": "¿A quién protege el seguro colectivo de retiro, de acuerdo con el Artículo 86?",
        "opciones": ["A los familiares de los militares.", "A los integrantes del Ejército, Fuerza Aérea y Armada en servicio activo que perciban haber y sobrehaber.", "A todos los ciudadanos que realizan su Servicio Militar Nacional."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Seguro Colectivo de Retiro"
    },
    {
        "pregunta": "El Artículo 100 establece que el ISSFAM debe administrar un fondo para atender las necesidades de habitación. ¿Cómo se llama este fondo?",
        "opciones": ["Fondo de Ahorro para la Vivienda.", "Fondo de la vivienda militar.", "Programa Nacional de Vivienda para Militares."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Vivienda"
    },
    {
        "pregunta": "¿Cuál es la aportación que el Gobierno Federal proporciona para integrar el fondo de la vivienda, según el Artículo 101, Fracción I?",
        "opciones": ["Un 10% sobre los haberes de los militares.", "Un 5% sobre los haberes y ciertas asignaciones de los militares en activo.", "Una cuota fija anual determinada por la SHCP."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Vivienda"
    },
    {
        "pregunta": "De acuerdo con el Artículo 156, ¿con qué documentos se acredita principalmente el estado civil y parentesco de los familiares de un militar?",
        "opciones": ["Con cartas de recomendación de un superior.", "Con las actas y constancias que expide el Registro Civil.", "Con una declaración jurada ante notario público."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Acreditación de Derechos"
    },
    {
        "pregunta": "¿Cómo debe probarse la dependencia económica según el Artículo 159?",
        "opciones": ["Únicamente con los recibos de nómina del militar.", "Con una carta redactada por el familiar.", "Con información testimonial rendida bajo protesta de decir verdad ante la SEDENA o SEMAR."],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Acreditación de Derechos"
    },
    {
        "pregunta": "El Artículo 88 menciona causas por las que un militar NO tendrá derecho al seguro colectivo de retiro. ¿Cuál es una de ellas?",
        "opciones": ["Retirarse por llegar a la edad límite.", "Incapacitarse en actos del servicio.", "Por mala conducta."],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Seguro Colectivo de Retiro"
    },
    {
        "pregunta": "¿Cuál es el interés que devengan los créditos a los militares otorgados con cargo al fondo de la vivienda, según el Artículo 113?",
        "opciones": ["Un interés del 10% anual.", "Un interés del 4% anual sobre saldos insolutos.", "No devengan ningún interés."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Vivienda"
    },
    {
        "pregunta": "Según el Artículo 170, ¿cómo se acredita la muerte de un militar por causas ajenas al servicio?",
        "opciones": ["Con el parte informativo de su Comandante.", "Con el testimonio de dos compañeros de armas.", "Únicamente con la copia certificada del acta de defunción expedida por el Registro Civil."],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Acreditación de Derechos"
    },
    {
        "pregunta": "El Artículo 73 establece que los militares pueden designar beneficiarios para su seguro de vida libremente. ¿Cómo debe formularse dicha designación?",
        "opciones": ["Verbalmente frente a su superior directo.", "En el documento de afiliación o en escrito por triplicado dirigido al Instituto.", "A través de un correo electrónico a la Dirección de Recursos Humanos."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Seguro de Vida Militar"
    },
    {
        "pregunta": "¿Qué sucede con los depósitos del fondo de la vivienda si un militar fallece, según el Artículo 112?",
        "opciones": ["Se transfieren automáticamente al patrimonio del Instituto.", "Se entregan a sus beneficiarios o causahabientes.", "Se utilizan para pagar las pensiones de otros militares."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Vivienda"
    },
    {
        "pregunta": "El Artículo 177 establece que las Secretarías de la Defensa Nacional y de Marina deben informar al Instituto sobre diversas situaciones de su personal. ¿Cuál es el plazo para hacerlo?",
        "opciones": ["90 días.", "30 días.", "No mayor de 15 días."],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Procedimientos"
    },
    {
        "pregunta": "¿Puede un militar desistirse de su solicitud de retiro voluntario, según el Artículo 190?",
        "opciones": ["No, una vez solicitada es irrevocable.", "Sí, puede hacerlo hasta antes de que se le comunique la aprobación del beneficio.", "Solo si paga una penalización."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Procedimientos"
    },
    {
        "pregunta": "Un militar con licencia especial desea acogerse al seguro de vida potestativo. Según el Artículo 69, ¿dentro de qué plazo debe manifestar su deseo al Instituto?",
        "opciones": ["Dentro de los seis meses siguientes al inicio de la licencia.", "En cualquier momento durante la licencia.", "Dentro de los treinta días siguientes a la fecha en que inicie la licencia."],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Seguro de Vida Militar"
    },
    {
        "pregunta": "El Artículo 63, Fracción III, establece que la suma asegurada para el personal de Defensas Rurales se calcula con base en el haber y sobrehaber de un:",
        "opciones": ["Sargento Primero.", "Soldado o su equivalente en la Armada.", "Teniente."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Seguro de Vida Militar"
    },
    {
        "pregunta": "Según el Artículo 89, ¿cómo se calcula la cuantía de la suma asegurada del Seguro Colectivo de Retiro?",
        "opciones": ["Es un monto fijo de 50 meses de haber para todos los casos.", "Es el resultado de multiplicar el haber y sobrehaber mensual mínimo por un factor basado en los años de servicio.", "Es el total de las aportaciones realizadas por el militar más un interés del 5%."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Seguro Colectivo de Retiro"
    },
    {
        "pregunta": "Un militar con 35 años de servicio pasa a situación de retiro. ¿Qué factor en meses se utiliza para calcular su Seguro Colectivo de Retiro según la tabla del Artículo 89?",
        "opciones": ["30 meses.", "32 meses.", "35 meses."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Seguro Colectivo de Retiro"
    },
    {
        "pregunta": "El Artículo 91 establece la devolución de aportaciones del seguro colectivo de retiro. ¿Qué se les devuelve a los militares que causan baja por mala conducta?",
        "opciones": ["Todas sus aportaciones más un 20%.", "Únicamente las cantidades que por concepto de sus aportaciones hubieren realizado.", "No se les devuelve nada."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Seguro Colectivo de Retiro"
    },
    {
        "pregunta": "De acuerdo con el Artículo 103, cuando un militar recibe un crédito de vivienda, ¿qué sucede con los depósitos acumulados a su favor en el Fondo de la Vivienda?",
        "opciones": ["Se le entregan en efectivo al militar.", "Se aplican de inmediato como pago inicial del crédito concedido.", "Quedan congelados hasta que se liquide el crédito."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Vivienda"
    },
    {
        "pregunta": "¿Qué opción se contempla en el Artículo 108 para los cónyuges militares que son ambos beneficiarios de esta ley en materia de créditos de vivienda?",
        "opciones": ["Solo uno de ellos puede solicitar el crédito.", "Deben elegir cuál de los dos renuncia a su derecho.", "Se les podrán otorgar los créditos de forma individual o mancomunadamente."],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Vivienda"
    },
    {
        "pregunta": "El Artículo 160 establece que la relación de concubinato debe ser acreditada necesariamente con un documento específico. ¿Cuál es?",
        "opciones": ["Un acta notarial de vida en común.", "Una información testimonial de tres testigos.", "La designación que el militar haya hecho de esa persona como concubina o concubinario ante el Instituto o la Secretaría correspondiente."],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Acreditación de Derechos"
    },
    {
        "pregunta": "Según el Artículo 162, ¿cuándo se considerará como muerto a un militar desaparecido en una acción de armas?",
        "opciones": ["Inmediatamente después de la desaparición.", "Después de que la Secretaría correspondiente haga la declaración, pasados sesenta días de la desaparición.", "Después de un año y un día de la desaparición."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Acreditación de Derechos"
    },
    {
        "pregunta": "Si un militar se incapacita en actos del servicio en primera categoría, ¿qué sucede con el pago de su Seguro de Vida Militar según los Artículos 60 y 63?",
        "opciones": ["Debe esperar a fallecer para que sus beneficiarios lo cobren.", "Se le entrega la suma asegurada directamente a él en vida.", "Recibe solo la mitad de la suma asegurada."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Seguro de Vida Militar"
    },
    {
        "pregunta": "¿Cuál es el plazo de prescripción para que los beneficiarios designados reclamen el cobro del seguro de vida militar, según el Artículo 81?",
        "opciones": ["Un año.", "Dos años.", "Cinco años."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Seguro de Vida Militar"
    },
    {
        "pregunta": "El Artículo 122 permite la venta de casas habitación a plazos con dos tipos de garantía. ¿Cuáles son?",
        "opciones": ["Garantía prendaria o fianza.", "Garantía hipotecaria o con reserva de dominio.", "Garantía personal o aval de un superior."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Vivienda"
    },
    {
        "pregunta": "¿Qué plazo de espera puede conceder la Junta Directiva a un militar que no puede cubrir los abonos de su crédito hipotecario, según el Artículo 130?",
        "opciones": ["Un mes.", "Seis meses.", "Un año."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Vivienda"
    },
    {
        "pregunta": "El Artículo 175 establece varios medios para comprobar la edad de un militar para efectos de retiro. Si no se cuenta con el acta de nacimiento, ¿cuál es la siguiente opción?",
        "opciones": ["La declaración de dos testigos.", "La copia certificada de la fe de bautismo.", "Un dictamen médico que estime la edad."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Acreditación de Derechos"
    },
    {
        "pregunta": "¿Qué debe contener el extracto de antecedentes formulado para definir los derechos de los retirados, según el Artículo 180?",
        "opciones": ["Únicamente nombre, grado y tiempo de servicios.", "Nombre, edad, grado, matrícula, antigüedad, corporaciones, tiempo de servicios y Clave Única de Registro de Población.", "Historial de combate, condecoraciones y nombre de sus familiares."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Procedimientos"
    },
    {
        "pregunta": "De acuerdo con el Artículo 188, una vez que la Secretaría notifica la procedencia de retiro y el cómputo de servicios, ¿de qué plazo dispone el militar para manifestar su conformidad o inconformidad?",
        "opciones": ["5 días hábiles.", "15 días hábiles.", "30 días naturales."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Procedimientos"
    },
    {
        "pregunta": "El Artículo 98 establece que a un militar retirado que vuelva al activo se le considerará, para efectos del seguro colectivo de retiro, como...",
        "opciones": ["Un continuador de su servicio anterior.", "Exento de este seguro.", "De nuevo ingreso."],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Seguro Colectivo de Retiro"
    },
    {
        "pregunta": "Según el Artículo 116, ¿en qué plazo prescriben los derechos de los militares o sus beneficiarios sobre los depósitos constituidos en el fondo de la vivienda?",
        "opciones": ["Dos años.", "Diez años.", "Cinco años."],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Vivienda"
    },
    {
        "pregunta": "Conforme al Artículo 196, ¿qué debe hacer el Instituto si advierte que la Dirección de la Secretaría omitió formalidades de procedimiento que pudieran dar lugar a reclamaciones?",
        "opciones": ["Corregir el error por su cuenta y continuar el trámite.", "Devolverá la documentación a dicha Dirección para que se proceda legalmente.", "Ignorar la omisión y emitir la resolución."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Procedimientos"
    },
    {
        "pregunta": "Un militar fallece en acción de armas y se le otorga a su familia una pensión. Según el Artículo 40, esta pensión se calcula con el 100% del haber de retiro y el 100% del sobrehaber. ¿Qué disposición adicional se aplica si el monto resultante es bajo?",
        "opciones": ["No hay disposición adicional, se paga el monto calculado.", "La pensión en ningún momento será inferior al equivalente a 180 días de salario mínimo vigente en el Distrito Federal.", "Se le añade un bono único del 25% sobre el total calculado."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Cálculo de Beneficios"
    },
    {
        "pregunta": "¿Cuál es la diferencia en el tratamiento de la suma asegurada del Seguro Colectivo de Retiro para un militar que se incapacita en 1ra categoría EN actos del servicio, versus uno que se incapacita en 1ra categoría FUERA de actos del servicio con 22 años de servicio? (Artículos 87 y 89)",
        "opciones": ["Ambos reciben el mismo monto basado en sus años de servicio.", "El incapacitado EN servicio recibe 50 meses de haber, mientras que el incapacitado FUERA de servicio recibe el factor correspondiente a 22 años (18 meses).", "El incapacitado FUERA de servicio no tiene derecho al seguro, solo a la devolución de aportaciones."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Seguro Colectivo de Retiro"
    },
    {
        "pregunta": "Un militar que obtuvo un crédito de vivienda fallece. Sus herederos solicitan la aplicación del seguro de liberación de adeudo 3 años después del fallecimiento. Según el Artículo 111, ¿procede la aplicación del seguro?",
        "opciones": ["Sí, el seguro se puede aplicar en cualquier momento.", "No, porque el derecho para solicitar la aplicación del seguro prescribe a los dos años a partir de la fecha del fallecimiento.", "Solo procede si pagan una multa por la solicitud tardía."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Vivienda"
    },
    {
        "pregunta": "El Artículo 168 establece que el fallecimiento o incapacidad como consecuencia de atenciones médico-quirúrgicas (responsabilidad médica) debe probarse de una forma específica. ¿Cuál es?",
        "opciones": ["Con el dictamen pericial de dos médicos militares.", "Con la sentencia ejecutoriada dictada por los tribunales militares en la que se declare la responsabilidad médica.", "Con el testimonio del director del hospital y el parte de novedades."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Acreditación de Derechos"
    },
    {
        "pregunta": "Un militar con 12 años de servicio se incapacita en actos del servicio y su incapacidad se clasifica en SEGUNDA categoría. Según el Artículo 34, ¿qué porcentaje de haber de retiro le corresponde?",
        "opciones": ["80%", "100%", "90%"],
        "respuesta_correcta": 2, "dificultad": "dificil", "tema": "Cálculo de Beneficios por Incapacidad"
    },
    {
        "pregunta": "¿Cuál es la diferencia en la obligación de reintegrar beneficios si un militar retirado con HABER DE RETIRO vuelve al activo por curación definitiva, versus uno que vuelve al activo por acuerdo presidencial? (Artículo 30)",
        "opciones": ["En ambos casos debe reintegrar todo lo cobrado.", "Por curación definitiva se deja insubsistente el haber sin obligación de reintegrar, mientras que por acuerdo presidencial solo se suspende el pago del haber.", "Por acuerdo presidencial no reintegra nada, pero por curación debe reintegrar el 50%."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Retiro y Compensación"
    },
    {
        "pregunta": "Un militar designa a su madre como beneficiaria de su seguro de vida. Años después, contrae matrimonio y no actualiza la designación. Al fallecer, ¿quién cobra el seguro según la prelación del Artículo 77?",
        "opciones": ["La esposa, porque tiene preferencia legal sobre la madre.", "La madre, porque la designación de beneficiarios es libre y una designación posterior es la única que revoca la anterior (Art. 74).", "La esposa y la madre cobran el 50% cada una."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Seguro de Vida Militar"
    },
    {
        "pregunta": "¿Qué institución tiene la facultad de sancionar los acuerdos de la Junta Directiva que conceden o niegan haberes de retiro para que puedan ser ejecutados, según el Artículo 200?",
        "opciones": ["La Secretaría de la Defensa Nacional o de Marina.", "La Suprema Corte de Justicia de la Nación.", "La Secretaría de Hacienda y Crédito Público."],
        "respuesta_correcta": 2, "dificultad": "dificil", "tema": "Procedimientos"
    },
    {
        "pregunta": "El Artículo 181 establece que para el cómputo de servicios, la fracción de tiempo que exceda de cierto límite se computará como un año completo. ¿Cuál es ese límite?",
        "opciones": ["La fracción que exceda de tres meses.", "La fracción que exceda de seis meses.", "Cualquier fracción, sin importar su duración."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Procedimientos"
    },
    {
        "pregunta": "De acuerdo con el Artículo 185, Fracción IV, ¿en qué caso no se puede tramitar una solicitud de retiro voluntario relacionada con la capacitación del militar?",
        "opciones": ["Si el militar está a la mitad de un curso de capacitación.", "Cuando por disposición legal o compromiso, deba prestar determinado tiempo de servicios después de haber terminado un curso.", "Si el militar ha tomado más de tres cursos en su carrera."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Procedimientos y Restricciones"
    },
    {
        "pregunta": "¿Qué recurso puede interponer un interesado contra una resolución provisional de la Junta Directiva del Instituto, según el Artículo 198?",
        "opciones": ["Juicio de amparo directo.", "Recurso de reconsideración.", "Apelación ante la Secretaría de la Defensa Nacional."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Procedimientos"
    },
    {
        "pregunta": "El Artículo 214 establece la competencia para las controversias sobre la aplicación de la ley. ¿A qué tribunales corresponde conocer de ellas?",
        "opciones": ["Exclusivamente a los Tribunales Militares.", "A los Tribunales Federales, con excepción de los asuntos que por su naturaleza sean competencia de los Tribunales Locales.", "A las Juntas de Conciliación y Arbitraje."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "¿Bajo qué circunstancias el ISSFAM puede intervenir en la administración o mantenimiento de conjuntos habitacionales construidos con recursos del fondo de la vivienda, según el Artículo 117?",
        "opciones": ["Cuando los habitantes lo soliciten por mayoría.", "El Instituto no podrá intervenir en dichos conceptos.", "Solo si el conjunto habitacional presenta un déficit financiero."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Vivienda"
    },
    {
        "pregunta": "Un militar con 28 años de servicio fallece en un accidente durante sus vacaciones. Su cónyuge solicita la pensión. ¿Con qué porcentaje se calcula dicha pensión según la tabla del Artículo 35?",
        "opciones": ["75%", "100%", "90%"],
        "respuesta_correcta": 2, "dificultad": "dificil", "tema": "Aplicación de la Ley (Pensiones)"
    },
    {
        "pregunta": "¿Qué sucede con los derechos de un militar que deja de percibir su haber de retiro ya otorgado y no hace gestiones de cobro en un lapso de tres años, según el Artículo 51, Fracción IV?",
        "opciones": ["El dinero se acumula y puede cobrarlo todo junto después.", "Se pierden los derechos a percibir dicho beneficio.", "Se le aplica una sanción del 10% sobre el monto acumulado."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Pérdida de Derechos"
    },
    {
        "pregunta": "Si el Instituto paga el seguro de vida a un beneficiario y posteriormente aparece otro con una designación más reciente que no había sido recibida por el Instituto, ¿qué responsabilidad tiene el ISSFAM según el Artículo 74?",
        "opciones": ["Debe pagarle también al segundo beneficiario y luego intentar recuperar el primer pago.", "El pago realizado al último beneficiario de que se tenga conocimiento se considera válido y libera de responsabilidad al Instituto.", "Debe pagar la mitad a cada uno."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Seguro de Vida Militar"
    },
    # Bloque de Preguntas 3 (101-150)
    {
        "pregunta": "Según el Artículo 132, ¿qué establece el Instituto para la venta a bajo precio de artículos de consumo necesario?",
        "opciones": ["Supermercados de lujo.", "Tiendas, granjas y centros de servicio.", "Convenios con tiendas departamentales para descuentos."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Prestaciones Sociales"
    },
    {
        "pregunta": "¿Cuál es el propósito de los \"centros de bienestar infantil\" mencionados en el Artículo 136?",
        "opciones": ["Atender a los niños mayores de 45 días y menores de 7 años, hijos de militares.", "Ofrecer campamentos de verano para adolescentes.", "Dar clases de regularización para hijos de militares en primaria."],
        "respuesta_correcta": 0, "dificultad": "facil", "tema": "Prestaciones Sociales"
    },
    {
        "pregunta": "El Artículo 138 Bis menciona tres tipos de becas educativas. ¿Cuál de las siguientes es una de ellas?",
        "opciones": ["Beca deportiva.", "Beca de manutención.", "Beca de transporte."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Becas"
    },
    {
        "pregunta": "¿Qué es la \"Atención Médica Quirúrgica\" según la definición del Artículo 142?",
        "opciones": ["Un sistema exclusivo para cirugías de emergencia.", "Un sistema por el cual se trata de conservar y preservar la salud de las personas.", "Un programa de descuentos en farmacias."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Servicio Médico Integral"
    },
    {
        "pregunta": "De acuerdo con el Artículo 142, ¿qué familiares de militares tienen derecho al servicio médico integral?",
        "opciones": ["Primos y sobrinos.", "El cónyuge, concubina/o, hijos y padres, bajo ciertas condiciones.", "Únicamente el militar, sin incluir a sus familiares."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Servicio Médico Integral"
    },
    {
        "pregunta": "El Artículo 145 establece que la atención médico-quirúrgica incluye, además de la asistencia hospitalaria y farmacéutica, los servicios de...",
        "opciones": ["Nutriólogo y entrenador personal.", "Terapias alternativas y acupuntura.", "Obstetricia, prótesis, ortopedia y rehabilitación."],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Servicio Médico Integral"
    },
    {
        "pregunta": "¿A quiénes se otorga el servicio materno infantil, según el Artículo 149?",
        "opciones": ["A cualquier mujer familiar de un militar.", "A personal militar femenino, esposa, concubina e hijas menores de edad del militar.", "Exclusivamente al personal militar femenino."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Servicio Médico Integral"
    },
    {
        "pregunta": "El Artículo 152 establece una licencia para el personal militar femenino por parto. ¿De cuánto tiempo es la licencia posterior al parto?",
        "opciones": ["Un mes.", "Dos meses.", "Tres meses."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Servicio Médico Integral"
    },
    {
        "pregunta": "¿Qué prestación recibe el personal de tropa al nacimiento de un hijo, de acuerdo con el Artículo 151?",
        "opciones": ["Un bono económico.", "Una canastilla.", "Días de vacaciones adicionales."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Prestaciones Sociales"
    },
    {
        "pregunta": "El Artículo 226 contiene tablas para la determinación de las categorías y grados de accidentes o enfermedades. ¿Para qué se usan estas tablas?",
        "opciones": ["Para determinar el monto de las becas.", "Para dar origen a retiro por incapacidad.", "Para asignar el tipo de vivienda."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "Según el Artículo 144, ¿qué se considera para que un familiar pueda gozar del servicio médico?",
        "opciones": ["Que viva en el mismo domicilio que el militar.", "Que esté en situación de dependencia económica respecto del militar.", "Que tenga la misma nacionalidad que el militar."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Servicio Médico Integral"
    },
    {
        "pregunta": "El Artículo 157 indica cómo se prueba la imposibilidad física para trabajar. ¿Cómo se realiza?",
        "opciones": ["Con una carta del interesado explicando su condición.", "Con dictamen pericial de dos médicos militares o navales especialistas.", "Con el testimonio de sus familiares directos."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Acreditación de Derechos"
    },
    {
        "pregunta": "¿Cuál es la finalidad de los servicios turísticos mencionados en el Artículo 134?",
        "opciones": ["Generar ganancias para el Instituto.", "Proporcionar hospedaje a militares en tránsito y servicios turísticos de bajo costo a los beneficiarios.", "Competir con cadenas hoteleras internacionales."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Prestaciones Sociales"
    },
    {
        "pregunta": "¿Qué tipo de padecimientos se incluyen en la \"Primera Categoría\" de incapacidad del Artículo 226?",
        "opciones": ["Enfermedades leves y de corta duración.", "Padecimientos que causan incapacidades graves y permanentes, como la pérdida de ambos ojos o una extremidad.", "Lesiones deportivas menores."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El Artículo 209 establece que los cadetes y alumnos de planteles militares que no perciben haber, para efectos de la ley, serán considerados como:",
        "opciones": ["Soldados.", "Cabos.", "Sargentos primeros."],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "¿Para qué nivel de estudios se otorgan las becas de manutención y escolar, según el Artículo 138 Bis?",
        "opciones": ["Únicamente para nivel superior (licenciatura).", "Para nivel medio superior y superior.", "Para primaria y secundaria."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Becas"
    },
    {
        "pregunta": "De acuerdo con el Artículo 142, un hijo mayor de edad puede conservar el derecho al servicio médico hasta los 25 años si cumple ciertos requisitos. ¿Cuál de los siguientes NO es uno de ellos?",
        "opciones": ["Encontrarse estudiando en instituciones con validez oficial.", "No haber contraído matrimonio o vivir en concubinato.", "Estar realizando su servicio militar."],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Servicio Médico Integral"
    },
    {
        "pregunta": "El Artículo 146 establece excepciones para ordenar la hospitalización de un militar o familiar sin su consentimiento. ¿Cuál es una de esas circunstancias?",
        "opciones": ["Por recomendación de un familiar.", "Cuando la enfermedad es contagiosa o el estado del paciente demanda observación constante.", "Para realizar un chequeo médico de rutina."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Servicio Médico Integral"
    },
    {
        "pregunta": "¿Qué sucede si un militar con una enfermedad que lo incapacita temporalmente no se sujeta al tratamiento médico adecuado, según el Artículo 148?",
        "opciones": ["Se le da de baja automáticamente del servicio activo.", "No se le expedirá el certificado de incapacidad correspondiente.", "Se le obliga a pagar el costo del tratamiento."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Servicio Médico Integral"
    },
    {
        "pregunta": "La \"Beca especial\" del Artículo 138 Bis está destinada a un grupo específico de hijos de militares. ¿Cuál es?",
        "opciones": ["Hijos con promedio de excelencia académica.", "Hijos que padezcan un grado de discapacidad física o mental.", "Hijos que estudien en el extranjero."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Becas"
    },
    {
        "pregunta": "Según el Artículo 150, la ayuda en la lactancia (ministración de leche) se proporciona durante un periodo máximo de:",
        "opciones": ["Tres meses a partir del nacimiento.", "Doce meses a partir del nacimiento.", "Seis meses a partir del nacimiento."],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Servicio Médico Integral"
    },
    {
        "pregunta": "El Artículo 226, en la Primera Categoría de incapacidad, menciona la \"hemianopsia bilateral permanente\". ¿A qué tipo de padecimiento se refiere?",
        "opciones": ["Una afección cardíaca.", "Una alteración de la visión (pérdida de la mitad del campo visual).", "Una enfermedad renal."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Qué padecimiento relacionado con la diabetes mellitus se considera de Primera Categoría de incapacidad según el Artículo 226?",
        "opciones": ["Diabetes mellitus tipo 2 sin complicaciones.", "Diabetes mellitus tipo 1.", "Prediabetes."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El Artículo 212 establece la compatibilidad entre pensiones y haberes de retiro. ¿Qué combinación es compatible?",
        "opciones": ["Tres pensiones militares simultáneamente.", "Un haber de retiro con una pensión militar.", "Un haber de retiro con otro haber de retiro."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "¿Qué establece el Artículo 215 sobre los funcionarios que intervengan en la tramitación de prestaciones y alteren datos o documentos?",
        "opciones": ["Serán sancionados con una multa económica.", "Serán consignados de acuerdo con el Código de Justicia Militar o el Código Penal Federal.", "Recibirán una suspensión temporal de su cargo."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "Según el Artículo 221, el Gobierno Federal destina anualmente una cantidad para ciertas prestaciones. ¿Cuál es ese porcentaje y sobre qué base se calcula?",
        "opciones": ["10% del presupuesto total de la SEDENA.", "15% de los haberes, haberes de retiro y pensiones.", "20% de las cuotas de los militares."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Patrimonio y Aportaciones"
    },
    {
        "pregunta": "¿Qué tipo de información debe difundir el Instituto según el Artículo 2, Fracción XII?",
        "opciones": ["Propaganda política.", "Resultados deportivos de las Fuerzas Armadas.", "Conocimientos y orientaciones sobre prácticas de previsión social."],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Funciones del Instituto"
    },
    {
        "pregunta": "El Artículo 152 fue reformado para adicionar tiempo a la licencia posterior al parto en un caso específico. ¿Cuál es ese caso?",
        "opciones": ["Si el parto fue múltiple (gemelos o más).", "Si los hijos nacieron con cualquier tipo de discapacidad o requieren atención médica hospitalaria.", "Si la madre es oficial de alto rango."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Servicio Médico Integral"
    },
    {
        "pregunta": "¿Qué establece el Artículo 149 Bis sobre el derecho al servicio materno infantil para la cónyuge o concubina tras el fallecimiento del militar?",
        "opciones": ["El derecho se pierde inmediatamente al fallecer el militar.", "El derecho continúa indefinidamente.", "El derecho se conserva si se acredita que el nacimiento fue dentro de los 300 días a partir del deceso del militar."],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Servicio Médico Integral"
    },
    {
        "pregunta": "Según el Artículo 226, la \"obesidad de 40 o más de Índice de Masa Corporal\" se clasifica como una incapacidad de:",
        "opciones": ["Tercera Categoría.", "Segunda Categoría.", "Primera Categoría."],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "Un hijo de militar de 26 años está cursando una maestría, no está casado y depende económicamente de su padre. ¿Puede conservar el derecho al servicio médico según el Artículo 142?",
        "opciones": ["No, porque el límite de edad son 25 años sin excepción.", "Sí, excepcionalmente y a juicio del Instituto, se puede extender el beneficio hasta los 30 años si está realizando estudios superiores a licenciatura y demuestra los demás requisitos.", "No, porque el beneficio solo cubre hasta el nivel de licenciatura."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Servicio Médico Integral"
    },
    {
        "pregunta": "¿Cuál es la diferencia clave entre una hipoacusia de Primera Categoría y una de Segunda Categoría según la tabla del Artículo 226?",
        "opciones": ["La de Primera Categoría es en ambos oídos y la de Segunda es en uno solo.", "La de Primera Categoría es una hipoacusia profunda bilateral, mientras que la de Segunda puede ser una hipoacusia media bilateral o profunda de un oído y superficial del otro.", "No hay diferencia, ambas se tratan igual para efectos de retiro."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "Un militar sufre de \"asma bronquial rebelde al tratamiento\" (Art. 226). ¿En qué categoría de incapacidad se clasifica este padecimiento?",
        "opciones": ["Primera Categoría.", "Segunda Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El Artículo 144 establece que no se considera que hay dependencia económica para gozar del servicio médico cuando el familiar percibe una pensión militar. ¿Qué implicación tiene esto?",
        "opciones": ["Significa que la esposa pensionada de un militar retirado no puede recibir servicio médico.", "Significa que un hijo pensionado no puede ser derechohabiente al servicio médico de su padre militar retirado, pues ya tiene su propio beneficio.", "No tiene ninguna implicación práctica, es una formalidad."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Servicio Médico Integral"
    },
    {
        "pregunta": "¿Qué distinción hace el Artículo 226 Bis para la \"infección por el virus de la inmunodeficiencia humana\" como causa para cambio de Arma o Servicio?",
        "opciones": ["El simple hecho de ser seropositivo es causa de retiro inmediato.", "La infección confirmada es causa de cambio de Arma o Servicio cuando su control y tratamiento médico limite el desempeño de los actos del servicio.", "Se considera incapacidad de Primera Categoría en todos los casos."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El Artículo 211 establece que los derechos otorgados en contravención a la ley son nulos. ¿Quién debe ejercitar la acción de nulidad y en qué plazo?",
        "opciones": ["El militar afectado, en un plazo de un año.", "La Secretaría de la Función Pública, sin límite de tiempo.", "Exclusivamente el Instituto, dentro de los cinco años siguientes a la fecha en que se hayan otorgado los derechos."],
        "respuesta_correcta": 2, "dificultad": "dificil", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "Un militar sufre de \"Trastornos neuróticos severos y rebeldes a tratamiento\". ¿En qué categoría de incapacidad se clasifica este padecimiento mental según el Artículo 226?",
        "opciones": ["Primera Categoría.", "Segunda Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Cuál es la diferencia en la clasificación de la obesidad según el Índice de Masa Corporal (IMC) entre la Primera, Segunda y Tercera Categoría en el Artículo 226?",
        "opciones": ["Primera: IMC > 35; Segunda: IMC > 30; Tercera: IMC > 28.", "Primera: IMC ≥ 40; Segunda: IMC de 35 a 39.9; Tercera: IMC de 30 a 34.9.", "La obesidad no se clasifica en tres categorías, solo en una."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Qué establece el Artículo 218 sobre la relación laboral entre el Instituto y su personal?",
        "opciones": ["Se rigen por un contrato colectivo especial negociado cada año.", "Se rigen por la Ley Federal del Trabajo.", "Se rigen por la Ley Federal de los Trabajadores al Servicio del Estado."],
        "respuesta_correcta": 2, "dificultad": "dificil", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "Un militar retirado vive en una \"casa hogar\" del Instituto (Art. 135). ¿Qué debe pagar por este servicio?",
        "opciones": ["Nada, es una prestación gratuita.", "Una cuota mensual que satisfaga los gastos de administración y asistencia.", "Un porcentaje de su haber de retiro, fijado por la SHCP."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Prestaciones Sociales"
    },
    {
        "pregunta": "¿En qué caso el Artículo 147 requiere el consentimiento de los padres o representantes legales para la hospitalización?",
        "opciones": ["En todos los casos, sin importar la edad del paciente.", "Tratándose de menores de edad, discapacitados mental o sensorialmente, y personas adultas mayores con ciertas discapacidades.", "Solo para cirugías programadas, no para urgencias."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Servicio Médico Integral"
    },
    {
        "pregunta": "Un militar presenta \"hipertensión arterial con hipertrofia ventricular izquierda sin insuficiencia cardiaca\". ¿En qué categoría de incapacidad del Artículo 226 se clasifica?",
        "opciones": ["Segunda Categoría.", "Tercera Categoría.", "Lista de padecimientos para cambio de Arma o Servicio."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El Artículo 222 establece que el presupuesto de gastos del Instituto se cubre con su patrimonio, pero añade una obligación para el Gobierno Federal. ¿Cuál es?",
        "opciones": ["No tiene ninguna obligación adicional.", "La obligación de cubrir en cualquier tiempo el faltante que impida al Instituto el pago de las prestaciones.", "La obligación de auditar al Instituto anualmente."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "¿Cuál es la diferencia entre la \"Beca de manutención\" y la \"Beca escolar\" según el Artículo 138 Bis?",
        "opciones": ["No hay diferencia, son la misma beca.", "La de manutención es una cuota mensual, mientras que la escolar tiene por objeto cubrir los gastos inherentes de la educación (inscripción, etc.).", "La de manutención es para nivel medio superior y la escolar es para nivel superior."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Becas"
    },
    {
        "pregunta": "Según el Artículo 224, ¿está el Instituto obligado a constituir depósitos o fianzas legales, por ejemplo, en un juicio de amparo?",
        "opciones": ["Sí, como cualquier otra entidad paraestatal.", "No, porque se presume de acreditada solvencia.", "Solo si el monto del juicio supera el 1% de su patrimonio."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "La \"pérdida anatómica o funcional permanente de una mano\" ¿en qué categoría de incapacidad se clasifica según el Artículo 226?",
        "opciones": ["Primera Categoría.", "Segunda Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 0, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "Un militar sufre de \"vértigo de carácter recurrente\" (Art. 226). ¿En qué categoría de incapacidad se clasifica?",
        "opciones": ["Primera Categoría (si es permanente).", "Segunda Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 2, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El Artículo 139 establece \"centros de capacitación, desarrollo y superación\" para un grupo específico. ¿Quiénes son los destinatarios?",
        "opciones": ["Los militares en activo para mejorar sus habilidades de combate.", "Los derechohabientes de militares.", "El personal administrativo del Instituto."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Prestaciones Sociales"
    },
    {
        "pregunta": "¿Bajo qué circunstancias el Artículo 225 exige que el Director General obtenga autorización de la Junta Directiva para un acto judicial?",
        "opciones": ["Para presentar cualquier demanda.", "Para desistir de continuar una acción judicial que afecte el patrimonio del Instituto.", "Para contratar abogados externos."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "Diferencie la clasificación de una \"gastrectomía\" (resección del estómago) según el Artículo 226.",
        "opciones": ["Gastrectomía total es Primera Categoría, mientras que gastrectomía subtotal está en la lista de padecimientos para cambio de Arma o Servicio.", "Cualquier tipo de gastrectomía es siempre de Primera Categoría.", "No se menciona la gastrectomía en las tablas de incapacidad."],
        "respuesta_correcta": 0, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    # Bloque de Preguntas 4 (151-200)
    {
        "pregunta": "Según el Artículo 226, la \"pérdida anatómica o funcional, total e irreparable, de ambos globos oculares\" ¿a qué categoría de incapacidad pertenece?",
        "opciones": ["Segunda Categoría.", "Primera Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "La \"pérdida anatómica o funcional permanente de una mano; o de un pie\" se clasifica como:",
        "opciones": ["Segunda Categoría.", "Tercera Categoría.", "Primera Categoría."],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿En qué categoría de incapacidad se encuentra la \"epilepsia y otras formas de crisis convulsivas\"?",
        "opciones": ["Primera Categoría.", "Segunda Categoría.", "Lista para cambio de Arma o Servicio."],
        "respuesta_correcta": 0, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El padecimiento \"asma bronquial rebelde al tratamiento\" ¿en qué categoría se clasifica?",
        "opciones": ["Primera Categoría.", "Segunda Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "La \"pérdida anatómica o funcional permanente del pulgar de la mano dominante\" ¿a qué categoría pertenece?",
        "opciones": ["Tercera Categoría.", "Primera Categoría.", "Segunda Categoría."],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "Un militar presenta \"hipertensión arterial no complicada\". ¿Dónde se clasifica este padecimiento según el Artículo 226 Bis?",
        "opciones": ["Primera Categoría.", "Lista de padecimientos que ameritan cambio de Arma o Servicio.", "Segunda Categoría."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "Las \"neuralgias permanentes\" que producen incapacidad funcional, ¿en qué categoría se encuentran?",
        "opciones": ["Tercera Categoría.", "Primera Categoría.", "Segunda Categoría."],
        "respuesta_correcta": 0, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Qué establece el Artículo 218 sobre la relación entre el Instituto y sus trabajadores?",
        "opciones": ["Se rigen por un reglamento interno especial.", "Se rigen por la Ley Federal de los Trabajadores al Servicio del Estado.", "Se rigen por la Ley Federal del Trabajo."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "El Artículo 219 indica que los trabajadores del Instituto quedarán bajo el régimen de una ley específica. ¿Cuál es?",
        "opciones": ["La Ley del Seguro Social (IMSS).", "La Ley del Instituto de Seguridad y Servicios Sociales de los Trabajadores del Estado (ISSSTE).", "La propia Ley del ISSFAM."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "El \"Síndrome de Inmunodeficiencia Adquirida (SIDA)\" con infecciones oportunistas o neoplasias malignas que impliquen pérdida de la funcionalidad, ¿en qué categoría se clasifica?",
        "opciones": ["Segunda Categoría.", "Tercera Categoría.", "Primera Categoría."],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "La \"pérdida anatómica o funcional de un pulmón\", ¿a qué categoría de incapacidad corresponde?",
        "opciones": ["Primera Categoría.", "Segunda Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 0, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Qué establece el Artículo Segundo Transitorio de la ley de 2003 sobre la ley anterior de 1976?",
        "opciones": ["Que la ley de 1976 sigue vigente en su totalidad.", "Que se abroga la ley de 1976, dejando a salvo los derechos ya adquiridos.", "Que ambas leyes se aplican simultáneamente."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Artículos Transitorios"
    },
    {
        "pregunta": "Según el Artículo 227, ¿la contabilidad del Instituto está sujeta a revisión de las autoridades federales?",
        "opciones": ["No, el Instituto es autónomo en su contabilidad.", "Sí, mediante una auditoría de carácter permanente.", "Solo si se sospecha de un fraude."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "Las \"monoplejia, paraplejia, hemiplejia y/o cuadriplejias definitivas\" son causa de retiro por incapacidad de:",
        "opciones": ["Segunda Categoría.", "Tercera Categoría.", "Primera Categoría."],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "La \"gastrectomía total\" (extirpación total del estómago) ¿en qué categoría de incapacidad se clasifica?",
        "opciones": ["Primera Categoría.", "Segunda Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 0, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "Un militar sufre un accidente que le provoca \"la anquilosis total unilateral de la articulación temporomandibular que no es quirúrgicamente corregible\". ¿En qué categoría se clasifica?",
        "opciones": ["Segunda Categoría.", "Tercera Categoría.", "Primera Categoría."],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "Un militar padece de \"insuficiencia renal crónica con reserva funcional entre 20 y 50%\". ¿A qué categoría de incapacidad corresponde?",
        "opciones": ["Primera Categoría (reserva menor del 20%).", "Segunda Categoría.", "Tercera Categoría (reserva mayor del 50%)."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "La \"diabetes mellitus tipo 2 con dos o más complicaciones crónicas moderadas\" se clasifica como incapacidad de:",
        "opciones": ["Tercera Categoría (con una sola complicación).", "Primera Categoría (tipo 1).", "Segunda Categoría."],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿En qué categoría se clasifica la \"pérdida anatómica o funcional permanente de todos los dedos de un pie\"?",
        "opciones": ["Primera Categoría.", "Segunda Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "Un militar presenta \"queratocono bilateral\". ¿A qué categoría de incapacidad corresponde este padecimiento ocular?",
        "opciones": ["Segunda Categoría.", "Tercera Categoría.", "Primera Categoría."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El padecimiento \"parálisis facial completa, unilateral o bilateral, rebelde al tratamiento\" se encuentra en la:",
        "opciones": ["Tercera Categoría.", "Segunda Categoría.", "Primera Categoría."],
        "respuesta_correcta": 0, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "La \"infección por el virus de la inmunodeficiencia humana confirmada... cuyo control y tratamiento médico limite el desempeño de los actos del servicio\" ¿dónde se clasifica?",
        "opciones": ["Primera Categoría (SIDA).", "Segunda Categoría.", "Lista de padecimientos para cambio de Arma o Servicio (Artículo 226 Bis)."],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Qué establece el Artículo 210 sobre los derechos que se otorguen en contravención a lo dispuesto por la ley?",
        "opciones": ["Son válidos si el militar actuó de buena fe.", "Son nulos.", "Deben ser revisados por un juez para determinar su validez."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "¿Qué institución financiera empleará el Instituto de forma preferente como su agente financiero, según el Artículo 228?",
        "opciones": ["El Banco de México.", "Cualquier banco comercial con la mejor oferta.", "El Banco Nacional del Ejército, Fuerza Aérea y Armada, SNC."],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "¿Cuál era el propósito de la reforma al Artículo 27 publicada el 4 de febrero de 2011?",
        "opciones": ["Aumentar la edad de retiro.", "Modificar la tabla de años de servicio y años en el grado para el ascenso con fines de retiro.", "Reducir el número de prestaciones."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Artículos Transitorios y Reformas"
    },
    {
        "pregunta": "El padecimiento \"cirrosis hepática de cualquier etiología\" ¿en qué categoría de incapacidad se encuentra?",
        "opciones": ["Primera Categoría.", "Segunda Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 0, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "Un militar padece \"rigidez o anquilosis de un tobillo, que mantiene su posición funcional\". ¿Cómo se clasifica?",
        "opciones": ["Segunda Categoría (si son ambos tobillos).", "Primera Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "La \"farmacodependencia (a drogas e inhalantes), consumo perjudicial rebelde a tratamiento y adicción\" ¿en qué categoría se clasifica?",
        "opciones": ["Primera Categoría.", "Segunda Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "La \"pérdida parcial o incompleta de 2 o más dedos de una mano\" se encuentra en la lista de padecimientos para:",
        "opciones": ["Cambio de Arma o Servicio.", "Incapacidad de Tercera Categoría.", "Incapacidad de Segunda Categoría."],
        "respuesta_correcta": 0, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Qué establece el Artículo Sexto Transitorio de la ley de 2003 sobre los militares retirados antes de su vigencia?",
        "opciones": ["Que sus haberes de retiro permanecerían sin cambios.", "Que se les sustituiría la \"ayuda para militares retirados\" por la cantidad determinada conforme al nuevo Artículo 31 y los tabuladores actuales.", "Que debían volver al servicio activo para ajustar sus beneficios."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Artículos Transitorios"
    },
    {
        "pregunta": "Diferencie la clasificación de una alteración visual central irreparable entre Primera y Segunda Categoría.",
        "opciones": ["Primera Categoría es visión 20/100 y Segunda es 20/70.", "Primera Categoría es visión a lo sumo 20/200, mientras que Segunda está comprendida entre 20/100 a 20/70.", "Ambas se refieren a ceguera total, pero en diferentes condiciones."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "Un militar padece \"insuficiencia cardiaca crónica con fracción de expulsión por ecocardiografía menor del 50%\". ¿Cómo se clasifica?",
        "opciones": ["Primera Categoría.", "Segunda Categoría, si es rebelde a tratamiento.", "Tercera Categoría, si no presenta síntomas."],
        "respuesta_correcta": 0, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Cuál es la diferencia entre \"deficiencia mental\" (Primera Categoría) y \"trastornos de la personalidad severos\" (Segunda Categoría)?",
        "opciones": ["No hay diferencia, ambos son trastornos psicóticos.", "La deficiencia mental se mide con un coeficiente intelectual (menor a 80%), mientras que los trastornos de la personalidad son del comportamiento y rebeldes a tratamiento.", "La deficiencia mental es de Tercera Categoría."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "Un militar presenta un acortamiento de 4 centímetros en una pierna no susceptible de corrección. ¿En qué categoría de incapacidad se clasifica según el Artículo 226?",
        "opciones": ["Primera Categoría (si es de más de 5 cm).", "Segunda Categoría.", "Tercera Categoría (si es de 3 a 5 cm)."],
        "respuesta_correcta": 2, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Cuál es la distinción clave que hace el Artículo 226 para clasificar una lesión de cadera o rodilla que amerita artroplastias (prótesis) en Primera Categoría versus Tercera Categoría?",
        "opciones": ["Primera Categoría: dos o más artroplastias CON deformidad notoria y claudicación. Tercera Categoría: hasta 2 artroplastias SIN deformidad ni claudicación.", "El número de artroplastias no importa, solo el dolor que cause.", "Todas las artroplastias se clasifican en Segunda Categoría."],
        "respuesta_correcta": 0, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "Un militar presenta \"escleroma respiratorio en etapa granulomatosa, que no responda al tratamiento\". ¿Cómo se clasifica este padecimiento?",
        "opciones": ["Primera Categoría (si deja secuelas cicatriciales severas).", "Segunda Categoría.", "Tercera Categoría (si está en etapa catarral)."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El DECRETO de reforma del 27 de enero de 2015 realizó un cambio significativo en el Artículo 226. ¿Cuál fue?",
        "opciones": ["Aumentó el número de categorías de incapacidad.", "Derogó la lista de padecimientos que ameritaban cambio de Arma o Servicio y creó el Artículo 226 Bis con una nueva lista.", "Eliminó todos los padecimientos mentales de las tablas."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Artículos Transitorios y Reformas"
    },
    {
        "pregunta": "¿Qué tipo de trastorno del humor (afectivo) es considerado causa de retiro en Primera Categoría?",
        "opciones": ["Trastornos moderados recurrentes (Segunda Categoría).", "Trastornos depresivos graves y rebeldes a tratamiento.", "Cualquier tipo de trastorno del humor."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "Diferencie la clasificación de una \"insuficiencia respiratoria irreversible\" entre Primera, Segunda y Tercera categoría, basándose en el porcentaje de la espirometría.",
        "opciones": ["No se usa el porcentaje, solo el diagnóstico del médico.", "1ra: 50% o más; 2da: entre 40 y 50%; 3ra: entre 20% y 40%.", "1ra: más del 60%; 2da: entre 50 y 60%; 3ra: menos del 50%."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Cuál de los siguientes padecimientos oculares NO pertenece a la Tercera Categoría de incapacidad?",
        "opciones": ["El glaucoma en cualquiera de sus variantes, rebelde al tratamiento.", "El nistagmus permanente, rebelde al tratamiento.", "Las cuadrantanopsias permanentes."],
        "respuesta_correcta": 0, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "Un militar padece \"linfedema severo\". ¿En qué categoría de incapacidad se clasifica?",
        "opciones": ["Primera Categoría.", "Segunda Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Cuál de las siguientes pérdidas anatómicas de dedos se considera de Primera Categoría?",
        "opciones": ["De dos dedos de la mano dominante que incluyan el pulgar.", "Del pulgar de la mano dominante (Segunda Categoría).", "Del cuarto y quinto dedos de la mano dominante (Tercera Categoría)."],
        "respuesta_correcta": 0, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Qué establece el Artículo 226 Bis sobre el desprendimiento de retina tratado?",
        "opciones": ["Es causa de retiro en Segunda Categoría.", "Amerita cambio de Arma o Servicio cuando a juicio del médico limite la actividad física.", "No se considera una incapacidad si el tratamiento fue exitoso."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "Un militar presenta \"lesiones valvulares con cardiomegalia, insuficiencia cardiaca y/o arritmias crónicas, aun tratadas quirúrgicamente\". ¿Cómo se clasifica?",
        "opciones": ["Primera Categoría.", "Segunda Categoría.", "Tercera Categoría (si son sin cardiomegalia)."],
        "respuesta_correcta": 0, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Qué tipo de alteración visual periférica se considera de Primera Categoría?",
        "opciones": ["Visión periférica que conserva entre 10 y 20% de la normal (Segunda Categoría).", "Visión periférica restringida a lo sumo al 10% de su extensión normal (visión tubular).", "Visión periférica que conserva entre 20 y 40% de la normal (Tercera Categoría)."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El padecimiento \"miastenia gravis\", ¿en qué categoría de incapacidad se clasifica?",
        "opciones": ["Primera Categoría.", "Segunda Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 0, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "La \"tuberculosis de la columna vertebral deformante y/o con parálisis no susceptible de tratamiento\", ¿a qué categoría pertenece?",
        "opciones": ["Segunda Categoría.", "Tercera Categoría.", "Primera Categoría."],
        "respuesta_correcta": 2, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El DECRETO del 7 de mayo de 2019 adicionó dos párrafos a un artículo específico. ¿Cuál fue el artículo y el propósito de la adición?",
        "opciones": ["Al Artículo 31, para cambiar el cálculo del haber de retiro.", "Al Artículo 152, para ampliar la licencia por parto en caso de hijos con discapacidad o que requieran hospitalización.", "Al Artículo 108, para permitir créditos de vivienda mancomunados."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Artículos Transitorios y Reformas"
    },
    {
        "pregunta": "Un militar padece \"síndrome de absorción intestinal deficiente, sin respuesta al tratamiento\". ¿Cómo se clasifica?",
        "opciones": ["Primera Categoría.", "Segunda Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 0, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "Diferencie entre una \"hernia o eventración\" de Tercera Categoría y una de Primera Categoría.",
        "opciones": ["Ambas son de Tercera Categoría.", "No existe esa distinción en las tablas.", "La de Tercera Categoría no responde a tratamiento quirúrgico, y la de Primera Categoría es la misma condición pero se entiende que es una errata, ya que también aparece en Primera Categoría sin mayor distinción."],
        "respuesta_correcta": 2, "dificultad": "dificil", "tema": "Tablas de Incapacidad (Análisis Crítico)"
    },
    # Bloque de Preguntas 5 (201-250)
    {
        "pregunta": "Según el Artículo 204, ¿cómo se notifica a los militares en servicio activo durante un trámite de retiro?",
        "opciones": ["Por correo electrónico.", "A través de una publicación en el Diario Oficial.", "Personalmente o por conducto del Comandante o Jefe de su corporación."],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Procedimientos"
    },
    {
        "pregunta": "El Artículo 207 establece que, salvo incapacidad declarada judicialmente, los militares deben promover los trámites de retiro y beneficio de forma:",
        "opciones": ["Por medio de un familiar.", "Personalmente.", "A través de un representante sindical."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Procedimientos"
    },
    {
        "pregunta": "De acuerdo con el Artículo 214, las controversias sobre la aplicación de esta Ley son competencia de los:",
        "opciones": ["Tribunales Militares exclusivamente.", "Tribunales Federales.", "Juntas de Conciliación y Arbitraje."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "¿Qué establece el Artículo 224 sobre la solvencia del Instituto?",
        "opciones": ["Que debe demostrar su solvencia con un capital mínimo.", "Que se presume de acreditada solvencia y no está obligado a constituir depósitos ni fianzas legales.", "Que su solvencia es garantizada por un banco privado."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "La \"pérdida de la lengua con pérdida de funciones\" ¿en qué categoría de incapacidad se clasifica? (Artículo 226)",
        "opciones": ["Segunda Categoría.", "Primera Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El padecimiento \"rinitis atrófica que no responda al tratamiento\" ¿en qué categoría se encuentra? (Artículo 226)",
        "opciones": ["Tercera Categoría.", "Segunda Categoría.", "Primera Categoría."],
        "respuesta_correcta": 0, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Qué padecimiento es \"La enfermedad alcohólica (consumo perjudicial rebelde a tratamiento y adicción)\"? (Artículo 226)",
        "opciones": ["Una incapacidad de Primera Categoría.", "Una incapacidad de Segunda Categoría.", "Una incapacidad de Tercera Categoría."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El Artículo 216 indica que si durante un trámite se descubre la comisión de un delito, el Instituto debe:",
        "opciones": ["Suspender el trámite inmediatamente.", "Ignorar el delito y continuar con el trámite.", "Denunciar los hechos al Ministerio Público que corresponda."],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "Según el Artículo 228, el Instituto empleará los servicios del Banco Nacional del Ejército, Fuerza Aérea y Armada de forma:",
        "opciones": ["Exclusiva y obligatoria.", "Preferente.", "Opcional y esporádica."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "La \"pérdida del maxilar superior\" que no puede ser reemplazada con prótesis, ¿qué categoría de incapacidad es? (Artículo 226)",
        "opciones": ["Tercera Categoría.", "Segunda Categoría.", "Primera Categoría."],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Qué establece el Artículo 226 Bis sobre la \"gastrectomía subtotal\"?",
        "opciones": ["Es una incapacidad de Segunda Categoría.", "Amerita cambio de Arma o Servicio.", "Es una incapacidad de Primera Categoría."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El Artículo 206 establece que los términos señalados para los trámites son:",
        "opciones": ["Prorrogables a solicitud del interesado.", "Improrrogables, con algunas excepciones judiciales.", "Computados en días naturales."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Procedimientos"
    },
    {
        "pregunta": "La \"gota que incapacita frecuentemente al individuo\" se clasifica como: (Artículo 226)",
        "opciones": ["Primera Categoría.", "Segunda Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 0, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Qué tipo de información deben proporcionar los militares al Instituto y al Banco, según el Artículo 177?",
        "opciones": ["Solo su información médica.", "Únicamente su rango y salario.", "Los datos que soliciten en relación con las funciones que les señala esta Ley."],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Procedimientos"
    },
    {
        "pregunta": "El padecimiento \"afasia permanente\" (pérdida de la capacidad de producir o comprender lenguaje) es una incapacidad de: (Artículo 226)",
        "opciones": ["Tercera Categoría.", "Segunda Categoría.", "Primera Categoría."],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El Artículo 181 indica cómo se computa el tiempo de servicios. ¿Cómo se considera una fracción de tiempo que excede los seis meses?",
        "opciones": ["Se ignora hasta cumplir el siguiente año.", "Se computa como un año completo para efectos del cálculo del beneficio.", "Se computa como medio año."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Procedimientos"
    },
    {
        "pregunta": "¿Qué sucede, según el Artículo 189, si la Dirección de la Secretaría considera procedente un retiro pero el Presidente o la propia Secretaría estiman necesarios los servicios del militar?",
        "opciones": ["El trámite de retiro continúa de forma obligatoria.", "Pueden ejercitar su derecho de retención en el activo, interrumpiendo el trámite de retiro.", "El militar puede decidir si se retira o se queda."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Procedimientos"
    },
    {
        "pregunta": "Conforme al Artículo 197, mientras se realizan los trámites finales del beneficio por fallecimiento, ¿qué pago provisional puede cubrir el Instituto a los familiares?",
        "opciones": ["El 100% del haber de retiro del militar.", "El 50% del haber o haber de retiro que percibía el militar.", "Ningún pago hasta que la SHCP sancione la resolución."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Procedimientos"
    },
    {
        "pregunta": "El Artículo 200 establece que los acuerdos de la Junta Directiva sobre beneficios deben ser remitidos a una Secretaría para su sanción. ¿Cuál es?",
        "opciones": ["Secretaría de la Defensa Nacional.", "Secretaría de la Función Pública.", "Secretaría de Hacienda y Crédito Público."],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Procedimientos"
    },
    {
        "pregunta": "¿Qué establece el Artículo 213 sobre la modificación o insubsistencia de los derechos fijados en esta Ley?",
        "opciones": ["Pueden ser modificados por el Director General en cualquier momento.", "Solo pueden modificarse por la Junta Directiva del Instituto en los casos y con los requisitos señalados en la ley, o por sentencia ejecutoriada.", "Cualquier superior militar puede solicitar su modificación."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "Un militar presenta \"sarcoidosis con manifestaciones sistémicas\". ¿En qué categoría de incapacidad se clasifica? (Artículo 226)",
        "opciones": ["Segunda Categoría.", "Tercera Categoría.", "Primera Categoría."],
        "respuesta_correcta": 0, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El padecimiento \"hemocromatosis\" (exceso de hierro en el cuerpo), ¿a qué categoría de incapacidad pertenece? (Artículo 226)",
        "opciones": ["Primera Categoría.", "Segunda Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 0, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "Un militar padece \"síndrome nefrítico crónico, sin insuficiencia renal\". ¿Cómo se clasifica? (Artículo 226)",
        "opciones": ["Primera Categoría.", "Tercera Categoría.", "Segunda Categoría."],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "La \"pérdida de la falange distal de uno o de ambos pulgares\", ¿dónde se clasifica según el Artículo 226 Bis?",
        "opciones": ["Amerita cambio de Arma o Servicio.", "Es una incapacidad de Tercera Categoría.", "No se considera una incapacidad."],
        "respuesta_correcta": 0, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El Artículo Quinto Transitorio (2003) se refiere a los militares que se acogieron al seguro de vida potestativo antes de 1995. ¿Qué suma asegurada les correspondía por muerte natural?",
        "opciones": ["$15,000.00 pesos.", "$7,500.00 pesos.", "$22,500.00 pesos."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Artículos Transitorios"
    },
    {
        "pregunta": "El Artículo 191 establece una regla sobre los cómputos de tiempo de servicios. ¿Qué eficacia tienen los cómputos anteriores dentro de un nuevo trámite de retiro?",
        "opciones": ["Tienen plena eficacia y no pueden ser modificados.", "Carecen de eficacia probatoria, no invalidando los actos ajenos al trámite actual.", "Deben ser validados nuevamente por un superior."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Procedimientos"
    },
    {
        "pregunta": "Si un militar en trámite de retiro pasa a gozar de licencia ilimitada, ¿qué sucede con el procedimiento según el Artículo 205?",
        "opciones": ["Se suspende hasta que regrese al servicio activo.", "Se cancela y debe iniciarlo de nuevo.", "No se suspende el procedimiento."],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Procedimientos"
    },
    {
        "pregunta": "El padecimiento \"esclerosis sistémica progresiva\" se encuentra en la: (Artículo 226)",
        "opciones": ["Primera Categoría.", "Segunda Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 0, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Qué establece el Artículo 186 sobre los militares con licencia ilimitada que desean solicitar su retiro?",
        "opciones": ["Deben reingresar al activo para poder solicitarlo.", "Formularán su solicitud directamente ante la Secretaría que corresponda.", "Pierden su derecho a solicitar el retiro."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Procedimientos"
    },
    {
        "pregunta": "Las \"dermatosis crónicas rebeldes al tratamiento o de forma recidivante\" ameritan: (Artículo 226 Bis)",
        "opciones": ["Incapacidad de Segunda Categoría.", "Cambio de Arma o Servicio.", "Incapacidad de Tercera Categoría."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Cuál es la diferencia de clasificación entre una \"vejiga neurogénica no rehabilitable\" y una \"vejiga neurogénica rehabilitada con secuelas\"? (Artículo 226)",
        "opciones": ["Ambas son de Primera Categoría.", "La no rehabilitable es de Primera Categoría, mientras que la rehabilitada con secuelas es de Segunda Categoría.", "La no rehabilitable es de Segunda Categoría y la rehabilitada es de Tercera."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "Un militar con 33 años de servicio se retiró en 2007. El Artículo Transitorio PRIMERO, inciso b) de la reforma de 2008 estableció un incremento gradual de su haber de retiro. ¿Qué porcentaje adicional se le aplicó en el año 2009?",
        "opciones": ["16.50%", "66.00%", "33.00%"],
        "respuesta_correcta": 2, "dificultad": "dificil", "tema": "Artículos Transitorios"
    },
    {
        "pregunta": "El Artículo 198 establece el recurso de reconsideración. ¿Sobre qué temas se rechazaría de plano dicho recurso?",
        "opciones": ["Sobre el monto del beneficio calculado por el Instituto.", "Sobre lo ya resuelto por la Dirección de la Secretaría respectiva (personalidad militar, jerarquía, causa de retiro, etc.).", "Sobre cualquier aspecto de la resolución provisional."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Procedimientos"
    },
    {
        "pregunta": "¿Qué diferencia existe entre la clasificación de \"movimientos involuntarios anormales\" (temblor, corea) de la Primera Categoría y el \"vértigo de carácter recurrente\" de la Tercera Categoría? (Artículo 226)",
        "opciones": ["Los de Primera Categoría imposibilitan la marcha o la prehensión, mientras que el de Tercera es solo recurrente.", "Ambos se clasifican igual si son rebeldes a tratamiento.", "El vértigo es siempre de Primera Categoría si es permanente."],
        "respuesta_correcta": 0, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El Artículo 195 contempla la rectificación de una resolución definitiva. ¿Bajo qué circunstancias específicas procede?",
        "opciones": ["Si el militar no está de acuerdo con el monto de su pensión.", "Si existen pruebas supervenientes que acrediten que la incapacidad o fallecimiento fue consecuencia de actos de responsabilidad médica (Art. 168).", "En cualquier momento si el militar presenta nuevas pruebas de cualquier tipo."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Procedimientos"
    },
    {
        "pregunta": "El Artículo 226 Bis fue adicionado por el Decreto del 27 de enero de 2015. ¿Qué le sucedió a la lista de padecimientos que antes estaba al final del Artículo 226 y que cumplía la misma función?",
        "opciones": ["Se mantuvo y ahora existen dos listas.", "Fue derogada por el mismo decreto.", "Se fusionó con la Tercera Categoría."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Artículos Transitorios y Reformas"
    },
    {
        "pregunta": "¿Qué distinción hace la ley entre \"espondilitis anquilosante\" (Primera Categoría) y \"artritis de cualquier etiología\" (Tercera Categoría)? (Artículo 226)",
        "opciones": ["La espondilitis es resistente a tratamiento, mientras que la artritis de Tercera Categoría produce una incapacidad funcional específica (entre 20% y 40%).", "Son el mismo padecimiento, pero se clasifica según la edad del militar.", "La espondilitis afecta la columna y la artritis solo las manos."],
        "respuesta_correcta": 0, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "Según el Artículo Transitorio TERCERO de la reforma de 2012, ¿de dónde se obtendrían los recursos para cubrir los incrementos de haberes de retiro de ese año?",
        "opciones": ["De un fondo de emergencia del Gobierno Federal.", "Del presupuesto de las Secretarías de la Defensa Nacional y de Marina.", "De las cuotas de los militares en activo."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Artículos Transitorios"
    },
    {
        "pregunta": "El Artículo 208 establece que las notificaciones pueden hacerse por correo certificado. ¿Qué sucede si el correo devuelve el oficio o no se recibe el acuse, y la notificación personal no es posible?",
        "opciones": ["Se publica en el Diario Oficial de la Federación.", "Se tiene por notificado al interesado.", "Se suspenderá el procedimiento hasta que el interesado se haga presente."],
        "respuesta_correcta": 2, "dificultad": "dificil", "tema": "Procedimientos"
    },
    {
        "pregunta": "Compare la clasificación de una \"insuficiencia coronaria crónica\" en Tercera Categoría y una de Primera Categoría (Artículo 226).",
        "opciones": ["En Tercera Categoría es tratada con isquemia residual ligera, mientras que en Primera es no susceptible de revascularización y/o rebelde a tratamiento.", "La de Tercera Categoría es asintomática y la de Primera es sintomática.", "No hay diferencia, depende del criterio del médico."],
        "respuesta_correcta": 0, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El Artículo 200 establece un plazo para que el militar o sus beneficiarios soliciten la modificación de un acuerdo de beneficio si se generaron nuevos derechos después de la sanción. ¿Cuál es ese plazo?",
        "opciones": ["Cinco años.", "Un año.", "Dos años."],
        "respuesta_correcta": 2, "dificultad": "dificil", "tema": "Procedimientos"
    },
    {
        "pregunta": "¿Qué establece el Artículo 182 sobre la cuantía del beneficio de retiro?",
        "opciones": ["La Junta Directiva la fija considerando el cómputo de servicios a la fecha de la solicitud.", "La Junta Directiva la fija ampliando hasta la fecha de su acuerdo el cómputo del tiempo de servicios.", "El monto es fijado por la SHCP basándose en el último sueldo."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Procedimientos"
    },
    {
        "pregunta": "Un militar presenta \"lesiones cicatriciales no corregibles, que dan lugar a deformaciones notables o dificultan la movilidad\". ¿En qué categoría se clasifica? (Artículo 226)",
        "opciones": ["Primera Categoría.", "Segunda Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 0, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Qué diferencia existe en el tratamiento de \"trastornos del humor (afectivos)\" entre la Primera y Segunda Categoría? (Artículo 226)",
        "opciones": ["En Primera Categoría son graves y rebeldes a tratamiento, mientras que en Segunda son moderados recurrentes o persistentes y rebeldes a tratamiento.", "En Primera Categoría incluyen psicosis y en Segunda no.", "Solo se mencionan en la Primera Categoría."],
        "respuesta_correcta": 0, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "La adición al Artículo 108 (Decreto del 24 de mayo de 2017) permite mancomunar créditos de vivienda con cónyuges beneficiarios de otras instituciones. ¿Cuál de las siguientes instituciones NO se menciona?",
        "opciones": ["INFONAVIT e ISSSTE.", "La Comisión Nacional de Vivienda.", "Bancos comerciales privados."],
        "respuesta_correcta": 2, "dificultad": "dificil", "tema": "Artículos Transitorios y Reformas"
    },
    {
        "pregunta": "El Artículo 211 establece un plazo para que el Instituto ejercite la acción de nulidad sobre un derecho mal otorgado. ¿Qué sucede si el Instituto no actúa en ese plazo?",
        "opciones": ["El derecho puede ser anulado por otra instancia.", "El derecho se considera firme y ya no puede ser anulado por esta vía.", "El plazo se renueva automáticamente por otros cinco años."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "El Artículo 226 Bis incluye \"obesidad con un índice de masa corporal entre 28 a 29.9\" como causa para cambio de Arma o Servicio. ¿Cómo se diferencia de la obesidad de Tercera Categoría?",
        "opciones": ["Es la misma, pero depende si el militar desea cambiar de Arma.", "La de Tercera Categoría corresponde a un IMC de 30 a 34.9, siendo un grado mayor.", "La del Artículo 226 Bis requiere complicaciones adicionales."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Qué establece el Artículo 194 sobre el expediente si la declaración de la Secretaría es ADVERSA al solicitante (niega el retiro o la personalidad militar)?",
        "opciones": ["Se remite de todas formas al Instituto para una segunda opinión.", "Se notifica al interesado y se da aviso al Instituto y a la SHCP, pero el incidente no se remite al Instituto.", "Se archiva sin notificar a ninguna otra instancia."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Procedimientos"
    },
    {
        "pregunta": "Un militar presenta \"neurofibromatosis (enfermedad de Von Recklinghausen), con alteraciones y manifestaciones neurológicas\". ¿Cómo se clasifica? (Artículo 226)",
        "opciones": ["Segunda Categoría.", "Tercera Categoría.", "Primera Categoría."],
        "respuesta_correcta": 0, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El Artículo Transitorio SEGUNDO del Decreto del 3 de abril de 2012 establece un calendario de aplicación para el incremento de haberes de retiro. ¿Para qué grupo de militares aplicaba esta tabla?",
        "opciones": ["Militares con 30 o más años de servicio.", "Militares que pasaran a retiro con 20 hasta 29 años de servicios efectivos.", "Todos los pensionistas sin excepción."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Artículos Transitorios"
    },
    # Bloque de Preguntas 6 (251-300)
    {
        "pregunta": "El Artículo 198 menciona el \"recurso de reconsideración\". ¿Contra qué se interpone este recurso?",
        "opciones": ["Contra una orden de un superior.", "Contra la resolución provisional de la Junta Directiva.", "Contra la sanción de la Secretaría de Hacienda."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Procedimientos"
    },
    {
        "pregunta": "Según el Artículo 211, ¿quién es el único facultado para ejercitar la acción de nulidad sobre un derecho mal otorgado?",
        "opciones": ["La Secretaría de la Función Pública.", "El militar afectado.", "El Instituto (ISSFAM)."],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "La \"pérdida anatómica o funcional permanente del pulgar de la mano no dominante\" ¿en qué categoría se clasifica? (Artículo 226)",
        "opciones": ["Tercera Categoría.", "Segunda Categoría.", "Primera Categoría."],
        "respuesta_correcta": 0, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Qué establece el Artículo 50 sobre la baja del Ejército, Fuerza Aérea y Armada de México?",
        "opciones": ["Que siempre genera derecho a una compensación.", "Que, salvo excepciones como la muerte, extingue todo derecho a reclamar beneficios generados durante el servicio.", "Que obliga al Instituto a buscar un nuevo empleo para el militar."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Pérdida de Derechos"
    },
    {
        "pregunta": "El padecimiento \"litiasis renal unilateral recidivante\" (cálculos renales recurrentes en un riñón) amerita: (Artículo 226 Bis)",
        "opciones": ["Incapacidad de Segunda Categoría.", "Cambio de Arma o Servicio.", "Incapacidad de Tercera Categoría."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Qué es un \"Beneficiario\" según la definición del Artículo 4?",
        "opciones": ["Es sinónimo de \"Derechohabiente\".", "La persona en cuyo favor se ha designado un beneficio económico por voluntad expresa del militar.", "Cualquier familiar que dependa económicamente del militar."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Definiciones Clave"
    },
    {
        "pregunta": "El \"vértigo de cualquier etiología, permanente y rebelde a tratamiento\" ¿en qué categoría se clasifica? (Artículo 226)",
        "opciones": ["Primera Categoría.", "Segunda Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 0, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "Según el Artículo 32, ¿los haberes de retiro, compensaciones y pensiones están sujetos a impuestos?",
        "opciones": ["Sí, al Impuesto Sobre la Renta.", "No, quedan exentos de todo impuesto.", "Solo si superan 10 salarios mínimos."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Cálculo de Beneficios"
    },
    {
        "pregunta": "La \"parálisis del velo del paladar\" se encuentra clasificada en la: (Artículo 226)",
        "opciones": ["Primera Categoría.", "Segunda Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El Artículo 53 establece que la renuncia de derechos para percibir beneficios económicos...",
        "opciones": ["Es definitiva y extingue todos los derechos para el militar y sus familiares.", "Nunca será en perjuicio de terceros (los familiares conservan sus derechos).", "Es ilegal y no se puede realizar."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Pérdida de Derechos"
    },
    {
        "pregunta": "La \"hipotensión arterial\" que llega a producir estados sincopales y es rebelde a tratamiento, ¿en qué categoría se clasifica? (Artículo 226)",
        "opciones": ["Tercera Categoría.", "Segunda Categoría.", "Primera Categoría."],
        "respuesta_correcta": 0, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "De acuerdo con el Artículo 183, los certificados y dictámenes médicos deben estar suscritos por:",
        "opciones": ["Un solo médico militar de cualquier rango.", "Cuando menos por dos médicos militares o navales especialistas.", "Un médico civil y uno militar."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Procedimientos"
    },
    {
        "pregunta": "¿Qué establece el Artículo 199 sobre la resolución definitiva que dicta la Junta del Instituto en un recurso de reconsideración?",
        "opciones": ["Que debe ser idéntica a la resolución provisional.", "Que puede ratificar, modificar o revocar la resolución anterior.", "Que debe ser aprobada por el militar para ser válida."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Procedimientos"
    },
    {
        "pregunta": "El padecimiento \"acalasia que no responde al tratamiento\" (trastorno del esófago) es una incapacidad de: (Artículo 226)",
        "opciones": ["Tercera Categoría.", "Segunda Categoría.", "Primera Categoría."],
        "respuesta_correcta": 2, "dificultad": "facil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Qué es el \"Haber\" según la definición del Artículo 4?",
        "opciones": ["Todas las percepciones económicas del militar.", "La percepción base que se establece en el tabulador de la SHCP.", "Un bono por buen desempeño."],
        "respuesta_correcta": 1, "dificultad": "facil", "tema": "Definiciones Clave"
    },
    {
        "pregunta": "El Artículo 52 establece las causas de pérdida del derecho a pensión para los familiares. ¿Cuál es una causa aplicable al cónyuge supérstite, hijas y hermanas solteras?",
        "opciones": ["Cambiar de ciudad de residencia.", "Contraer matrimonio o vivir en concubinato.", "Aceptar un trabajo remunerado."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Pérdida de Derechos"
    },
    {
        "pregunta": "El Artículo 217 establece que el Instituto tomará medidas contra quienes aprovechen indebidamente los beneficios. ¿Qué tipo de acciones puede realizar?",
        "opciones": ["Únicamente sanciones administrativas.", "Ejercitará acciones ante los tribunales, presentará denuncias y formulará querellas.", "Publicar los nombres de los infractores."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "Un militar presenta \"osteomielitis crónica que produzca incapacidad funcional severa\". ¿En qué categoría de incapacidad se clasifica? (Artículo 226)",
        "opciones": ["Primera Categoría.", "Segunda Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Qué establece el Artículo 211 sobre el plazo para que el Instituto ejercite la acción de nulidad contra un derecho mal otorgado?",
        "opciones": ["No hay límite de tiempo.", "Dentro de los cinco años siguientes a la fecha en que se otorgaron los derechos.", "Dentro de un año a partir de que se descubre el error."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "El Artículo 188 establece un plazo de 15 días hábiles para que el militar manifieste su conformidad o inconformidad. ¿Qué sucede si deja transcurrir ese plazo en silencio?",
        "opciones": ["Se le concede una prórroga automática de 15 días más.", "Se considera como una aceptación tácita de la resolución.", "El trámite se cancela por falta de interés."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Procedimientos"
    },
    {
        "pregunta": "La \"pérdida anatómica o funcional permanente de tres dedos de la mano no dominante que no incluyan el pulgar\" se clasifica en la: (Artículo 226)",
        "opciones": ["Tercera Categoría.", "Segunda Categoría.", "Primera Categoría."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Qué institución tiene la obligación de practicar un examen médico anual a todos los militares, según el Artículo 178?",
        "opciones": ["El Instituto (ISSFAM).", "La Secretaría de Salud.", "Las Secretarías de la Defensa Nacional y de Marina."],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Procedimientos"
    },
    {
        "pregunta": "¿Qué se establece en el Artículo 54 sobre los plazos de prescripción para los menores de edad o incapacitados?",
        "opciones": ["Que los plazos corren igual para ellos.", "Que los términos de prescripción no proceden para ellos.", "Que los plazos se reducen a la mitad."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Pérdida de Derechos"
    },
    {
        "pregunta": "¿Cuál es una de las atribuciones generales de la Junta Directiva mencionada en el Artículo 12, Fracción XVI?",
        "opciones": ["Realizar actos y operaciones necesarios para la mejor administración del Instituto.", "Nombrar al Presidente de la República.", "Establecer las jerarquías militares."],
        "respuesta_correcta": 0, "dificultad": "intermedio", "tema": "Estructura y Facultades"
    },
    {
        "pregunta": "El padecimiento \"pancreatitis crónica y la litiasis pancreática, sin respuesta al tratamiento\" ¿a qué categoría pertenece? (Artículo 226)",
        "opciones": ["Tercera Categoría.", "Segunda Categoría.", "Primera Categoría."],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "Según el Artículo 196, ¿en qué se basará la Junta Directiva para otorgar o negar un beneficio?",
        "opciones": ["Únicamente en lo alegado por el promovente.", "En los hechos y circunstancias que aparezcan probados, hubieran sido o no alegados.", "En el historial de servicio del militar, sin considerar otras pruebas."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Procedimientos"
    },
    {
        "pregunta": "Las \"fístulas biliares y/o pancreáticas que se rehabiliten con tratamiento\" se clasifican como: (Artículo 226)",
        "opciones": ["Incapacidad de Primera Categoría (si no responden a tratamiento).", "Incapacidad de Segunda Categoría.", "Incapacidad de Tercera Categoría."],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "¿Qué establece el Artículo 223 sobre los bienes, derechos y fondos del Instituto?",
        "opciones": ["Que están sujetos a los mismos impuestos que las empresas privadas.", "Que gozarán de todas las franquicias que disfrute la Federación.", "Que pueden ser embargados por deudas del Instituto."],
        "respuesta_correcta": 1, "dificultad": "intermedio", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "El Artículo 209 establece una consideración para los miembros de los Cuerpos de Defensas Rurales incapacitados o fallecidos en actos del servicio. ¿Cómo se les considera para efectos de la ley?",
        "opciones": ["Como Sargentos Primeros.", "Como Cabos.", "Como Soldados."],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "El \"acortamiento de 3 a 5 centímetros de longitud entre ambos miembros pélvicos\" ¿en qué categoría de incapacidad se clasifica? (Artículo 226)",
        "opciones": ["Primera Categoría (si es de más de 5 cm).", "Segunda Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 2, "dificultad": "intermedio", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "Compare las causas de pérdida de derechos entre un haber de retiro (Art. 51) y una pensión para familiares (Art. 52). ¿Qué causa es exclusiva de la pensión y no del haber de retiro?",
        "opciones": ["Sentencia ejecutoriada que origine la pérdida del beneficio.", "Contraer matrimonio o vivir en concubinato (para el cónyuge supérstite, hijas, etc.).", "Dejar de percibir el beneficio por más de tres años."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Comparación de Artículos"
    },
    {
        "pregunta": "El Artículo 222 establece que el Gobierno Federal cubrirá el faltante que impida al Instituto el pago de prestaciones. ¿Qué condición o limitante se menciona en ese mismo artículo?",
        "opciones": ["Siempre y cuando el faltante no supere el 10% del presupuesto del Instituto.", "De acuerdo con las disponibilidades presupuestales del propio Gobierno Federal.", "Solo si el faltante es causado por un desastre natural."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "Diferencie la clasificación de \"lesiones valvulares\" cardíacas entre la Primera y Tercera Categoría. (Artículo 226)",
        "opciones": ["Primera Categoría: con cardiomegalia, insuficiencia cardiaca o arritmias crónicas. Tercera Categoría: sin cardiomegalia, insuficiencia cardiaca ni trastornos permanentes del ritmo.", "Ambas se clasifican igual, pero depende del resultado de la prueba de esfuerzo.", "La de Primera es congénita y la de Tercera es adquirida."],
        "respuesta_correcta": 0, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El Artículo 191 establece que los cómputos de tiempo de servicios que sirvieron de base a retiros anteriores tienen un trato especial en un nuevo trámite. ¿Cuál es?",
        "opciones": ["Se anulan y se realiza un nuevo cómputo desde cero.", "Se les reconocerá plena eficacia y no podrán ser modificados, sumándose su resultado al tiempo posterior al reingreso.", "Pierden el 50% de su valor en el nuevo cómputo."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Procedimientos"
    },
    {
        "pregunta": "¿Qué establece el Artículo 196 sobre la obligación de la Junta del Instituto respecto a las declaraciones definitivas emitidas por las Direcciones de SEDENA o SEMAR?",
        "opciones": ["La Junta puede revocar dichas declaraciones si no está de acuerdo.", "La Junta debe solicitar una tercera opinión a la SHCP.", "La Junta del Instituto, en sus resoluciones, acatará dichas declaraciones."],
        "respuesta_correcta": 2, "dificultad": "dificil", "tema": "Procedimientos"
    },
    {
        "pregunta": "El Artículo 212 prohíbe el disfrute simultáneo de ciertos beneficios. ¿Qué sucede con la persona que infringe esta disposición?",
        "opciones": ["Se le suspenden todos sus beneficios hasta que elija uno.", "Le será cancelado el pago del beneficio concedido con posterioridad y deberá reintegrar lo cobrado indebidamente.", "Recibe una sanción administrativa pero conserva los beneficios."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "Un militar presenta \"síndromes postflebíticos severos\" (complicación de trombosis venosa). ¿En qué categoría de incapacidad se clasifica? (Artículo 226)",
        "opciones": ["Tercera Categoría.", "Primera Categoría.", "Segunda Categoría."],
        "respuesta_correcta": 2, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El Artículo 52, Fracción V, establece una causa de pérdida de pensión muy específica para la cónyuge o concubina. ¿Cuál es?",
        "opciones": ["Tener descendencia en cualquier momento después del deceso del militar.", "Tener descendencia después de los trescientos días siguientes al fallecimiento del militar.", "No haber tenido descendencia con el militar."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Pérdida de Derechos"
    },
    {
        "pregunta": "Compare la clasificación de la pérdida de dedos de la mano dominante entre la Primera y Segunda Categoría. (Artículo 226)",
        "opciones": ["1ra: De dos dedos que incluyan el pulgar. 2da: Del pulgar únicamente.", "1ra: Del pulgar. 2da: Del índice y medio.", "No hay diferencia, cualquier pérdida de dedos es de Segunda Categoría."],
        "respuesta_correcta": 0, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El Artículo 215 sanciona a quienes alteren documentos o revelen falsedades en la tramitación. ¿Qué códigos o leyes se mencionan como base para la consignación?",
        "opciones": ["El Código Civil Federal y el Código de Comercio.", "La Ley Federal de Responsabilidades Administrativas únicamente.", "El Código de Justicia Militar o el Código Penal Federal."],
        "respuesta_correcta": 2, "dificultad": "dificil", "tema": "Prevenciones Generales"
    },
    {
        "pregunta": "¿Qué diferencia hay en el tratamiento de una \"colectomía\" (resección del colon) si es total o de más del 60% versus una resección menor? (Artículo 226)",
        "opciones": ["No se menciona la colectomía.", "La colectomía total o de más del 60% que curse con diarrea crónica intratable es de Primera Categoría. La ley no especifica clasificaciones para resecciones menores.", "Cualquier colectomía es de Segunda Categoría."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El Artículo 193 establece que si el militar manifiesta conformidad con la declaración provisional o deja transcurrir el plazo, esta se tendrá como definitiva. ¿Qué implicación legal tiene esto para el resto del trámite?",
        "opciones": ["El militar aún puede inconformarse en etapas posteriores.", "Los hechos y cómputos de esa declaración ya no podrán ser impugnados en el recurso de reconsideración ante el Instituto.", "La SHCP puede revocar esta declaración si lo considera necesario."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Procedimientos"
    },
    {
        "pregunta": "Un militar sufre una lesión y presenta \"rigidez o la anquilosis de ambos tobillos que dificulte o impida la estancia de pie o la marcha\". ¿Cómo se clasifica? (Artículo 226)",
        "opciones": ["Primera Categoría.", "Segunda Categoría.", "Tercera Categoría (si es solo un tobillo)."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El Artículo 32 permite reducciones al haber de retiro por dos conceptos específicos. ¿Cuáles son?",
        "opciones": ["Deudas con bancos privados o multas de tránsito.", "Adeudos contraídos con el Instituto por créditos hipotecarios o resolución judicial en caso de alimentos.", "Impuestos federales y estatales."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Cálculo de Beneficios"
    },
    {
        "pregunta": "El Artículo 185 prohíbe tramitar el retiro voluntario cuando un militar debe prestar tiempo de servicio por haber realizado un curso. ¿Esta prohibición aplica si el curso fue en el extranjero?",
        "opciones": ["No, solo aplica para cursos en establecimientos nacionales.", "Sí, la fracción IV especifica \"en algún establecimiento nacional o extranjero\".", "Solo si el curso en el extranjero fue pagado por el militar."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Procedimientos y Restricciones"
    },
    {
        "pregunta": "Compare la clasificación de una \"hepatitis crónica\" y una \"cirrosis hepática\". (Artículo 226)",
        "opciones": ["Ambas son de Primera Categoría.", "La hepatitis es de Segunda y la cirrosis es de Primera.", "La hepatitis es de Tercera y la cirrosis es de Segunda."],
        "respuesta_correcta": 0, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El Artículo 179 obliga a las direcciones de personal a comunicar los nombres de quienes cumplirán la edad límite. ¿Con cuánta anticipación mínima deben hacerlo?",
        "opciones": ["Un año.", "Seis meses.", "Un mes."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Procedimientos"
    },
    {
        "pregunta": "El Artículo 202 sobre las órdenes de baja del activo y alta en situación de retiro, ¿quién las gira?",
        "opciones": ["El Director General del Instituto.", "La Secretaría de origen (SEDENA/SEMAR) al recibir la notificación final del Instituto.", "La Secretaría de Hacienda y Crédito Público."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Procedimientos"
    },
    {
        "pregunta": "Un militar presenta \"trastornos de la articulación del lenguaje que lo hagan incomprensible\". ¿Cómo se clasifica? (Artículo 226)",
        "opciones": ["Primera Categoría (si es afasia).", "Segunda Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 2, "dificultad": "dificil", "tema": "Tablas de Incapacidad"
    },
    {
        "pregunta": "El Artículo 210 declara nulos los derechos otorgados en contravención a la ley. Si un militar recibe un beneficio de esta manera pero actuó de buena fe, ¿el beneficio es válido?",
        "opciones": ["Sí, la buena fe del militar valida el acto.", "No, la nulidad del acto no depende de la buena o mala fe del receptor.", "El beneficio es válido, pero debe reintegrar el 50%."],
        "respuesta_correcta": 1, "dificultad": "dificil", "tema": "Prevenciones Generales"
    },
    # Bloque de Preguntas 7 (301-350) - Nivel Dios
    {
        "pregunta": "Un militar con 25 años de servicio es retenido en el activo por acuerdo presidencial (Art. 26). Durante este periodo de retención, cumple los requisitos para ascender al grado inmediato para efectos de retiro según la tabla del Art. 27. Si posteriormente cesa la necesidad de sus servicios y pasa a retiro, ¿se considera el nuevo grado para el cálculo de su beneficio?",
        "opciones": ["No, el cálculo se hace con el grado que tenía al momento del acuerdo presidencial, ya que la retención congela su situación.", "Sí, porque la retención es una extensión del servicio activo y los derechos generados durante ella son válidos para el trámite de retiro final.", "Solo si la retención en el activo dura más de 5 años."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Análisis Combinado (Art. 26, 27, 189)"
    },
    {
        "pregunta": "Un militar fallece y su viuda, que también es militar en activo, solicita la pensión. Según el Artículo 144, \"no se considerará que hay dependencia económica, cuando el familiar perciba una pensión militar\". ¿Se le puede negar la pensión por viudez a la esposa militar activa basándose en este artículo?",
        "opciones": ["Sí, porque al ser militar activa percibe un haber, que es análogo a una pensión, y por tanto no hay dependencia económica.", "No, el Artículo 144 se refiere a la dependencia económica para gozar del SERVICIO MÉDICO, no para el derecho a la PENSIÓN, que se rige por el Artículo 38.", "Sí, se le niega la pensión pero se le otorga el doble de la suma del seguro de vida como compensación."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Interpretación y Ámbito de Aplicación (Art. 144 vs. Art. 38)"
    },
    {
        "pregunta": "Un militar es sentenciado y destituido de su empleo, causando baja de las Fuerzas Armadas (Art. 88, Frac. III). Sin embargo, antes de la sentencia, había designado beneficiarios para su Seguro Colectivo de Retiro. ¿Qué sucede con sus aportaciones según el Artículo 91, Fracción III?",
        "opciones": ["Las pierde totalmente por ser una baja por sentencia.", "Sus beneficiarios reciben el total de las aportaciones más un 20%.", "A él (o sus beneficiarios) se le devolverán únicamente las cantidades que por concepto de sus aportaciones hubiere realizado, sin el 20% adicional."],
        "respuesta_correcta": 2, "dificultad": "dios", "tema": "Aplicación de Excepciones (Art. 88 vs. Art. 91)"
    },
    {
        "pregunta": "La Junta Directiva del Instituto emite una resolución provisional negando un haber de retiro. El militar interpone un recurso de reconsideración (Art. 198) y la Junta, en su resolución definitiva, confirma la negativa. Esta resolución es sancionada por la SHCP. ¿Qué vía legal le queda al militar para impugnar esta decisión final?",
        "opciones": ["Ninguna, la resolución es final e inatacable.", "Puede interponer una queja ante el Órgano Interno de Control del Instituto.", "Puede demandar la nulidad de la resolución ante los Tribunales Federales, conforme al Artículo 214."],
        "respuesta_correcta": 2, "dificultad": "dios", "tema": "Secuencia Procesal y Jurisdiccional (Art. 199, 200, 214)"
    },
    {
        "pregunta": "Un militar con 18 años de servicio se incapacita en un accidente automovilístico fuera de actos de servicio, clasificándose en Primera Categoría. ¿Qué beneficios económicos le corresponden exactamente?",
        "opciones": ["Haber de retiro según el Art. 35 y Seguro Colectivo de Retiro según el Art. 87.", "Únicamente una compensación según los Artículos 36 y 37, y la devolución de sus aportaciones al Seguro Colectivo de Retiro más un 20% según el Art. 91.", "Haber de retiro por incapacidad fuera de servicio (Art. 35) y devolución de aportaciones del SCR (Art. 91), pero no la suma asegurada del SCR."],
        "respuesta_correcta": 2, "dificultad": "dios", "tema": "Análisis Combinado de Beneficios (Art. 35, 36, 87, 91)"
    },
    {
        "pregunta": "El Artículo 32 establece que los beneficios solo podrán reducirse por adeudos con el Instituto o por resolución judicial de alimentos. El Artículo 179 menciona un error en el pago. Si a un militar se le paga de más por error del Estado, ¿cómo se realiza el descuento para reintegrar lo pagado indebidamente?",
        "opciones": ["Se le exige el pago total en una sola exhibición.", "No se puede realizar el descuento, ya que no es un adeudo con el Instituto ni por alimentos.", "Se hará un descuento de hasta el 25% de su percepción periódica, ya que el Art. 179 sí lo permite como excepción."],
        "respuesta_correcta": 2, "dificultad": "dios", "tema": "Aplicación de Excepciones (Art. 32 vs. Art. 179)"
    },
    {
        "pregunta": "¿Cuál es la diferencia fundamental en el tratamiento de una \"Declaración de Procedencia de Retiro\" (Art. 188) y la \"resolución definitiva\" de la Junta Directiva (Art. 199)?",
        "opciones": ["Son el mismo documento, pero emitido por diferentes entidades.", "La Declaración es un acto de la Secretaría de origen que define la causa de retiro y el cómputo de servicios, mientras que la resolución de la Junta es la que constituye, modifica o extingue el derecho económico (la prestación).", "La Declaración es provisional y puede ser apelada, la resolución definitiva no."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Naturaleza de Actos Administrativos"
    },
    {
        "pregunta": "Un militar con crédito hipotecario del ISSFAM fallece. El seguro liquida el adeudo (Art. 111). Sus depósitos acumulados en el Fondo de la Vivienda, ¿qué tratamiento reciben según el Artículo 103, Fracción V?",
        "opciones": ["Se entregan íntegramente a sus beneficiarios, pues el seguro ya pagó la deuda.", "Se devuelven con la deducción de las cantidades que se hubieren aplicado al pago del crédito antes del fallecimiento.", "Se pierden y pasan a formar parte del patrimonio del Instituto."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Interacción de Beneficios (Vivienda y Seguros)"
    },
    {
        "pregunta": "Un militar es diagnosticado con \"insuficiencia coronaria crónica... con isquemia residual ligera\" (Tercera Categoría) y \"obesidad con IMC de 32\" (Tercera Categoría). Individualmente, no alcanzan una categoría superior. ¿Qué establece el numeral 53 de la Tercera Categoría que podría aplicar en este caso?",
        "opciones": ["El militar debe elegir el padecimiento más grave para su clasificación.", "Que la incapacidad de Tercera Categoría también se puede constituir con la suma de diversos grados de ella, si disminuyen la capacidad funcional entre el 20% y 40%.", "Que la suma de padecimientos de Tercera Categoría automáticamente lo clasifica en Segunda."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Análisis de las Tablas de Incapacidad"
    },
    {
        "pregunta": "El Artículo 212 prohíbe percibir más de dos pensiones militares. Si una persona es viuda de un militar (1ª pensión) e hija soltera pensionada de otro militar (2ª pensión), y posteriormente su hijo militar fallece, ¿podría reclamar una tercera pensión como madre dependiente?",
        "opciones": ["Sí, porque la dependencia económica como madre es un derecho aparte.", "No, porque el Artículo 212 es explícito al prohibir más de dos pensiones militares, y al reclamar la tercera estaría en infracción.", "Sí, pero debe renunciar a la pensión de menor cuantía."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Aplicación de Prohibiciones Legales"
    },
    {
        "pregunta": "Un militar retirado vuelve al activo por acuerdo presidencial. Durante este segundo periodo en activo, sufre una incapacidad en actos del servicio. ¿Cómo se tramita su nuevo retiro según el Artículo 30?",
        "opciones": ["Se reactiva su haber de retiro anterior con un ajuste por la nueva incapacidad.", "Al ocurrir una nueva causal de retiro, se tramitará éste de forma completamente nueva, dejando insubsistente el anterior.", "No se puede tramitar un nuevo retiro, simplemente vuelve a su situación anterior al desaparecer la necesidad de sus servicios."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Reingreso al Activo y Nuevos Derechos"
    },
    {
        "pregunta": "¿Cuál es la implicación de que el Artículo 95 establezca que, en caso de déficit en el Fondo del Seguro Colectivo de Retiro, éste se cubrirá con cargo al patrimonio del Instituto proveniente de las aportaciones del Gobierno Federal?",
        "opciones": ["Que las primas de los militares pueden aumentar automáticamente para cubrir el déficit.", "Que el SCR, a diferencia de un seguro privado, tiene un respaldo patrimonial del Estado, garantizando su solvencia más allá de sus propias primas.", "Que el pago de las sumas aseguradas puede suspenderse hasta que el fondo se recupere."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Análisis Financiero y Estructural"
    },
    {
        "pregunta": "Un militar solicita su retiro voluntario, pero la Nación entra en estado de guerra antes de que se apruebe su beneficio. ¿Qué sucede con su trámite según el Artículo 185?",
        "opciones": ["El trámite continúa normalmente, pero el pago se pospone hasta el fin de la guerra.", "No podrá tramitarse la solicitud, ya que es una de las causales de improcedencia.", "Se le otorga el retiro, pero se le obliga a reingresar inmediatamente por el estado de guerra."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Restricciones al Retiro Voluntario"
    },
    {
        "pregunta": "¿Qué diferencia sutil existe en la redacción de la pérdida de derechos a un beneficio por falta de cobro entre el Artículo 51 (Haber de Retiro) y el Artículo 52 (Pensión)?",
        "opciones": ["No hay ninguna diferencia, en ambos casos es por un lapso de tres años.", "El Art. 51 se refiere a \"dejar de percibir\", mientras que el Art. 52 distingue entre \"dejar de percibir\" (si ya estaba otorgada) y \"no hacer trámite alguno\" en 5 años tras la muerte.", "El plazo para el haber de retiro es de 3 años y para la pensión es de 5 años."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Comparación Precisa de Artículos"
    },
    {
        "pregunta": "La adición al Artículo 152 (Decreto 07-05-2019) permite transferir tiempo de la licencia prenatal a la postnatal. ¿Qué requisitos se deben cumplir para esto?",
        "opciones": ["Solo se necesita la solicitud expresa del personal militar femenino.", "Solicitud expresa, autorización escrita del médico responsable y tomando en cuenta la naturaleza del trabajo.", "Solicitud expresa y la autorización del Comandante de la Unidad."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Análisis de Reformas Específicas"
    },
    {
        "pregunta": "Un militar es diagnosticado con \"discromatopsia\" (incapacidad para discernir colores). ¿Bajo qué condición este padecimiento se clasifica en la Tercera Categoría de incapacidad según el Artículo 226?",
        "opciones": ["En todos los casos, la discromatopsia es de Tercera Categoría.", "Nunca se clasifica como incapacidad, ya que no afecta la función física.", "Siempre y cuando no exista un mecanismo compensador que permita la identificación correcta de los objetos."],
        "respuesta_correcta": 2, "dificultad": "dios", "tema": "Análisis de Condiciones en Tablas de Incapacidad"
    },
    {
        "pregunta": "Un militar retirado que cobra haber de retiro fallece. ¿La suma asegurada de su Seguro de Vida (Art. 63, Frac. II) se calcula sobre su último haber en activo o sobre el haber de retiro que percibía?",
        "opciones": ["Sobre su último haber en activo, ya que es mayor.", "Se calcula sobre el haber de retiro que estuviere percibiendo al momento de fallecer.", "Se promedian ambos montos para el cálculo."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Especificidad en Cálculo de Seguros"
    },
    {
        "pregunta": "El Artículo 226 Bis establece una lista de padecimientos para \"cambio de Arma o Servicio\". Si a un militar se le aplica un cambio por una de estas causas, ¿implica esto el inicio de un trámite de retiro?",
        "opciones": ["Sí, es el primer paso para el retiro por incapacidad.", "No, precisamente es una medida para evitar el retiro, reubicándolo en funciones compatibles con su padecimiento.", "Depende del criterio de la Junta Directiva del ISSFAM."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Interpretación del Propósito de la Norma"
    },
    {
        "pregunta": "Un militar con 42 años de servicio ostenta el grado máximo en una especialidad que es inferior al de General de División. Según el Artículo 28, ¿qué sucede al momento de su retiro?",
        "opciones": ["Se retira con el grado máximo que ostentaba, sin cambios.", "Asciende al grado inmediato para efectos de retiro, pues con 42 años de servicio solo necesita 3 años en el grado (Art. 27), y se asume que los cumple.", "El Artículo 28 no aplica para especialidades, solo para las Armas."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Aplicación Combinada (Art. 27 y 28)"
    },
    {
        "pregunta": "¿Cuál es el rol exacto del Subdirector General del Instituto en las sesiones de la Junta Directiva, según el Artículo 17?",
        "opciones": ["Asiste con voz pero sin voto, al igual que el Director General.", "Funge como Secretario de la Junta Directiva.", "Preside las sesiones en ausencia del Presidente y Vicepresidente."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Detalles de la Estructura Orgánica"
    },
    {
        "pregunta": "Un militar es diagnosticado con \"diabetes mellitus tipo 2 con una sola complicación crónica\". ¿Cómo se clasifica? (Artículo 226)",
        "opciones": ["Segunda Categoría (con dos o más complicaciones moderadas).", "Tercera Categoría.", "Lista para cambio de Arma o Servicio (sin complicación crónica)."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Diferenciación Precisa en Tablas de Incapacidad"
    },
    {
        "pregunta": "Si la Junta Directiva necesita autorizar un crédito hipotecario a 15 años, ¿qué artículo y fracción le da explícitamente esa facultad?",
        "opciones": ["Artículo 12, Fracción IV, que le da la facultad general de resolver sobre créditos.", "Artículo 12, Fracción VI, que le permite autorizar créditos de hasta 20 años para adquisición o construcción.", "Artículo 113, que establece los plazos de los créditos."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Especificidad de Facultades"
    },
    {
        "pregunta": "Un militar que se acogió al seguro de vida potestativo (Art. 69) fallece adeudando un semestre de la prima. ¿Qué sucede con la suma asegurada?",
        "opciones": ["El seguro se considera extinto y no se paga nada.", "Se paga la suma asegurada completa, perdonando el adeudo.", "Se descuenta la cuota adeudada del importe de la suma asegurada (Artículo 70)."],
        "respuesta_correcta": 2, "dificultad": "dios", "tema": "Condiciones del Régimen Potestativo"
    },
    {
        "pregunta": "¿Cuál es la diferencia fundamental entre el financiamiento de la prima del Seguro de Vida Militar (Art. 66) y la del Seguro Colectivo de Retiro (Art. 90)?",
        "opciones": ["Ambas son pagadas íntegramente por el Gobierno Federal.", "La del Seguro de Vida es cubierta por el Gobierno Federal, mientras que la del Seguro Colectivo de Retiro es mixta (una parte el gobierno y otra el militar).", "La del Seguro de Vida es pagada por el militar y la del SCR por el gobierno."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Comparación de Estructuras Financieras"
    },
    {
        "pregunta": "El Artículo 82 permite al Instituto usar hasta el 1.0% de los recursos del Fondo del Seguro de Vida para gastos de administración. El Artículo 96 permite usar hasta el 2.0% de las aportaciones anuales del Fondo del SCR para el mismo fin. ¿Qué implica esta diferencia?",
        "opciones": ["Que la administración del SCR es inherentemente más costosa para el Instituto.", "Que el legislador estableció límites de gasto administrativo diferentes para cada fondo, reflejando posiblemente su estructura y operación distintas.", "Es una errata en la ley, ambos deberían tener el mismo porcentaje."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Análisis Comparativo de Disposiciones Administrativas"
    },
    {
        "pregunta": "Un militar sufre una incapacidad en un acto del servicio clasificada en Tercera Categoría. La Secretaría de origen opta por retirarlo del activo. ¿Cómo se calcula su haber de retiro según el Artículo 35?",
        "opciones": ["Se le otorga una compensación, no un haber de retiro.", "Su cálculo se hará con base en lo dispuesto para los de SEGUNDA categoría de incapacidad.", "Se calcula usando los porcentajes de la tabla del Art. 35 para retiro voluntario."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Aplicación de Cláusulas Especiales"
    },
    {
        "pregunta": "Un militar con 22 años de servicio se retira voluntariamente. ¿Cuál es la diferencia en el porcentaje de su haber de retiro si se aplica la tabla del Art. 31 (retiro por edad límite o incapacidad en actos de servicio) versus la del Art. 35 (retiro voluntario)?",
        "opciones": ["Art. 31 le daría 52%, mientras que el Art. 35 le da 65%.", "Art. 31 le daría 65%, mientras que el Art. 35 le da 52%.", "Los porcentajes son idénticos en ambas tablas."],
        "respuesta_correcta": 0, "dificultad": "dios", "tema": "Comparación de Tablas de Beneficios"
    },
    {
        "pregunta": "¿Qué establece el Artículo 119 sobre los bienes inmuebles que el Instituto se adjudique o reciba en pago?",
        "opciones": ["Puede conservarlos indefinidamente como parte de su patrimonio.", "Debe venderlos en el término de seis meses.", "Debe destinarlos a vivienda para militares en activo."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Administración del Patrimonio"
    },
    {
        "pregunta": "Un militar es diagnosticado con \"trastornos vasoespásticos secundarios a un padecimiento sistémico, rebeldes al tratamiento\". ¿En qué categoría se clasifica? (Artículo 226)",
        "opciones": ["Primera Categoría.", "Segunda Categoría.", "Tercera Categoría."],
        "respuesta_correcta": 2, "dificultad": "dios", "tema": "Clasificación de Padecimientos Específicos"
    },
    {
        "pregunta": "El Artículo 40 establece que se considerará como \"consecuencia de actos del servicio\" el fallecimiento del militar durante el traslado de su domicilio al lugar de trabajo o viceversa. ¿Qué beneficio habilita esta consideración?",
        "opciones": ["Que la pensión para sus familiares sea del 100% del haber de retiro y sobrehaber, en lugar de un porcentaje menor.", "Únicamente el pago de un seguro de transporte adicional.", "La devolución total de sus aportaciones al fondo de ahorro."],
        "respuesta_correcta": 0, "dificultad": "dios", "tema": "Implicaciones de Definiciones Legales"
    },
    {
        "pregunta": "¿Puede la Junta Directiva del Instituto, según el Artículo 12, Fracción VIII, establecer o suprimir delegaciones del Instituto en los estados?",
        "opciones": ["No, eso es facultad exclusiva del Director General.", "Sí, es una de sus atribuciones explícitas.", "No, requiere autorización del Congreso de la Unión."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Facultades de la Junta Directiva"
    },
    {
        "pregunta": "El Artículo 97 establece un trato especial para los Secretarios de la Defensa Nacional y de Marina respecto al Seguro Colectivo de Retiro. ¿Cuál es?",
        "opciones": ["Están exentos de pagar las primas correspondientes.", "Reciben el doble de la suma asegurada.", "El beneficio les será pagado al concluir su encargo como Secretarios."],
        "respuesta_correcta": 2, "dificultad": "dios", "tema": "Disposiciones Especiales"
    },
    {
        "pregunta": "¿Cuál es la diferencia clave entre el derecho al servicio médico de un hijo soltero de 22 años estudiante (Art. 142) y el derecho a pensión de un hijo en las mismas condiciones (Art. 38)?",
        "opciones": ["No hay diferencia, los requisitos de edad y estudio son los mismos.", "Para la pensión, además de estudiar, debe acreditar anualmente dependencia económica mediante información testimonial. El artículo del servicio médico no lo especifica de esa forma.", "El servicio médico se extiende hasta los 25 años y la pensión solo hasta los 21."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Comparación de Requisitos entre Beneficios"
    },
    {
        "pregunta": "Un militar presenta \"síndrome de Zollinger Ellison, que no responde a tratamiento\". ¿En qué categoría de incapacidad se clasifica? (Artículo 226)",
        "opciones": ["Tercera Categoría.", "Segunda Categoría.", "Primera Categoría."],
        "respuesta_correcta": 2, "dificultad": "dios", "tema": "Clasificación de Padecimientos Específicos"
    },
    {
        "pregunta": "¿Qué establece el Artículo 83 sobre el incremento de los beneficios del seguro de vida militar?",
        "opciones": ["Solo pueden incrementarse si el Gobierno Federal aumenta sus aportaciones.", "El Instituto podrá incrementarlos con cargo a los recursos disponibles del propio fondo, previa autorización de la SHCP.", "Los beneficios son fijos y no pueden ser incrementados."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Administración de Fondos"
    },
    {
        "pregunta": "El Artículo 7, párrafo segundo, establece una regla de proporcionalidad en la designación de funcionarios y empleados por la Junta Directiva. ¿A qué se refiere?",
        "opciones": ["A la proporcionalidad de género.", "A procurar la proporcionalidad de acuerdo a los efectivos de cada Fuerza Armada (Ejército/Fuerza Aérea y Armada).", "A la proporcionalidad de acuerdo a la edad de los candidatos."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Detalles de la Estructura Orgánica"
    },
    {
        "pregunta": "Un militar con 28 años de servicio fallece en activo fuera de actos de servicio. ¿Cómo se calcula la pensión de sus familiares según la tabla del Art. 35?",
        "opciones": ["Se aplica el 90% sobre la base de cálculo.", "La tabla del Art. 35 es para el haber de retiro del militar vivo, no para la pensión por fallecimiento. Se debe usar el Art. 31.", "Se aplica el 58% de la tabla del Art. 31."],
        "respuesta_correcta": 0, "dificultad": "dios", "tema": "Aplicación Cruzada de Artículos y Tablas"
    },
    {
        "pregunta": "¿Cuál es el objeto de las \"casas hogar para retirados\" según el Artículo 135, a diferencia de las unidades habitacionales para ocupación temporal?",
        "opciones": ["Son para que los retirados las habiten por sí solos o con su cónyuge/concubinario, pagando una cuota para gastos de administración y asistencia.", "Son para venderlas a precios módicos a los retirados.", "Son centros de rehabilitación médica para retirados."],
        "respuesta_correcta": 0, "dificultad": "dios", "tema": "Diferenciación de Prestaciones Sociales"
    },
    {
        "pregunta": "Un militar presenta una \"diferencia de más de 5 centímetros de longitud en las extremidades pélvicas\". ¿Cómo se clasifica? (Artículo 226)",
        "opciones": ["Tercera Categoría (si es de 3 a 5 cm).", "Segunda Categoría.", "Primera Categoría."],
        "respuesta_correcta": 2, "dificultad": "dios", "tema": "Clasificación de Padecimientos Específicos"
    },
    {
        "pregunta": "El Artículo 123, Fracción IV, establece una regla para la rescisión de contrato de compra de una casa si la imposibilidad de pago ocurre dentro de los primeros 5 años. ¿Qué sucede en ese caso?",
        "opciones": ["El militar pierde todo lo que ha pagado.", "El inmueble se devuelve al Instituto, se le cobra una renta por el tiempo de ocupación y se le devuelve la diferencia de lo que hubiera abonado.", "El Instituto está obligado a rematar el inmueble y entregar el remanente al militar."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Condiciones de Contratos de Vivienda"
    },
    {
        "pregunta": "¿Cuál es la diferencia fundamental entre el tratamiento de una \"licencia ilimitada\" y una \"licencia especial\" para efectos del Seguro Colectivo de Retiro según el Artículo 90, Fracción V?",
        "opciones": ["La ilimitada permite seguir aportando, la especial no.", "Ambas situaciones permiten al militar aportar directamente al Instituto las primas para que el tiempo le sea considerado como de servicios prestados para este seguro.", "Con la licencia especial se pierden todos los derechos al seguro."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Condiciones Específicas de Seguros"
    },
    {
        "pregunta": "Un militar sufre de \"insuficiencia venosa crónica aun tratada quirúrgica y médicamente\". ¿En qué categoría se clasifica? (Artículo 226)",
        "opciones": ["Segunda Categoría.", "Tercera Categoría.", "Lista para cambio de Arma o Servicio."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Clasificación de Padecimientos Específicos"
    },
    {
        "pregunta": "El Artículo 81 establece plazos de prescripción diferentes para el cobro del seguro de vida. ¿Cuál es el plazo para los familiares señalados en el artículo 77 (prelación legal) en contraposición a los beneficiarios designados?",
        "opciones": ["Dos años para ambos.", "Dos años para los designados y tres años para los familiares de la prelación legal.", "Tres años para ambos."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Plazos y Prescripciones"
    },
    {
        "pregunta": "¿Qué establece el Artículo 118 sobre la liquidez del fondo de la vivienda?",
        "opciones": ["Que todo el fondo debe estar invertido a largo plazo.", "Que debe mantener en el Banco del Ejército, en depósito a la vista, solo las cantidades estrictamente necesarias para operaciones diarias, y el resto invertido en valores gubernamentales de inmediata realización.", "Que el 50% debe mantenerse en efectivo."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Administración de Fondos"
    },
    {
        "pregunta": "Un militar presenta \"esquizofrenia\". ¿En qué categoría de incapacidad se clasifica? (Artículo 226)",
        "opciones": ["Tercera Categoría si es controlable con medicamento.", "Segunda Categoría.", "Primera Categoría (como trastorno psicótico)."],
        "respuesta_correcta": 2, "dificultad": "dios", "tema": "Clasificación de Padecimientos Específicos"
    },
    {
        "pregunta": "¿Cuál es la diferencia en la integración del \"Fondo de Trabajo\" (Art. 58) y el \"Fondo de Ahorro\" (Art. 59)?",
        "opciones": ["Ambos son aportaciones mixtas del gobierno y el militar.", "El Fondo de Trabajo es una aportación del 11% solo del Gobierno Federal para tropa, mientras que el Fondo de Ahorro es una aportación mixta (6% el militar y 6% el gobierno) para Generales, Jefes y Oficiales.", "El Fondo de Trabajo es para Oficiales y el de Ahorro para Tropa."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Comparación de Fondos"
    },
    {
        "pregunta": "Un militar fallece. Sus familiares solicitan el beneficio de pensión 6 años después de la muerte, sin haber realizado ningún trámite previo. ¿Qué establece el Artículo 52, Fracción VII, al respecto?",
        "opciones": ["Tienen derecho a la pensión, pero solo se les paga de forma retroactiva por 3 años.", "Su derecho a percibir la pensión se ha perdido por no hacer trámite alguno durante los cinco años siguientes a la muerte del militar.", "El plazo de prescripción no aplica para pensiones."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Pérdida de Derechos"
    },
    {
        "pregunta": "El Artículo 80, Fracción IV, establece los documentos necesarios para el pago del seguro de vida por incapacidad. ¿Qué documento clave, además de la solicitud y la identificación, debe presentar el militar?",
        "opciones": ["Un dictamen de un médico privado.", "Una carta de recomendación de su comandante.", "La Orden de baja expedida por la Secretaría correspondiente y el Certificado de último pago."],
        "respuesta_correcta": 2, "dificultad": "dios", "tema": "Requisitos Documentales"
    },
    {
        "pregunta": "El Artículo 12, Fracción VII, fue reformado para permitir a la Junta Directiva aprobar y poner en vigor un documento crucial para la organización interna. ¿Cuál es?",
        "opciones": ["El Código de Justicia Militar.", "El Estatuto Orgánico.", "El Presupuesto de Egresos de la Federación."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Análisis de Reformas Específicas"
    },
    {
        "pregunta": "¿Cuál es la diferencia fundamental entre el trato de una \"compensación\" (Art. 30, inciso c) y un \"haber de retiro\" (Art. 30, inciso e) cuando un militar reingresa al activo por curación definitiva?",
        "opciones": ["En ambos casos, el militar debe reintegrar todo lo cobrado.", "La compensación debe ser reintegrada totalmente mediante descuentos, mientras que para el haber de retiro no existe la obligación de reintegrar las cantidades cobradas.", "El haber de retiro se reintegra y la compensación no."],
        "respuesta_correcta": 1, "dificultad": "dios", "tema": "Comparación Precisa de Artículos"
    }
]