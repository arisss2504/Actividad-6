import streamlit as st
from gtts import gTTS
from io import BytesIO

# Configuración inicial de la página
st.set_page_config(page_title="Chatbot Colectivo del Grupo", page_icon="🤖")

st.title("🤖 Chatbot Colectivo - Grupo de Clase")
st.write("Este chatbot integra la información, gustos y personalidades de los 5 compañeros entrevistados.")

# ---------------------------------------------------------
# INFORMACIÓN EXTRAÍDA DE LAS TABLAS
# ---------------------------------------------------------
companeros = [
    {
        "nombre": "GABRIELA VILLADIEGO GUTIERREZ",
        "sexo": "FEMENINO",
        "edad": 18,
        "canciones": "REGGATON",
        "peliculas": "RAPIDOS Y FURIOSOS",
        "deportes": "NINGUNO",
        "materia": "ESPAÑOL",
        "comida": "ARROZ CON POLLO",
        "fortalezas": "NINGUNA",
        "debilidades": "EL AMOR"
    },
    {
        "nombre": "JOHAN SEBASTIAN CESPEDES MENDIVELSO",
        "sexo": "MASCULINO",
        "edad": 16,
        "canciones": "BLESSD",
        "peliculas": "SPIDERMAN",
        "deportes": "FUTBOL",
        "materia": "MATEMATICAS",
        "comida": "PIZZA",
        "fortalezas": "FUERZA",
        "debilidades": "EL AMOR"
    },
    {
        "nombre": "KLEIBER JOSE AZUAJE MARIN",
        "sexo": "MASCULINO",
        "edad": 16,
        "canciones": "PUNKROCK",
        "peliculas": "JURASSIC PARK 1993",
        "deportes": "VOLEIBOL",
        "materia": "FISICA",
        "comida": "LASAGÑA",
        "fortalezas": "INTELIGENCIA",
        "debilidades": "EL AMOR"
    },
    {
        "nombre": "JUAN JOSE CRUZ VARGAS",
        "sexo": "MASCULINO",
        "edad": 16,
        "canciones": "VARIADO",
        "peliculas": "RAPIDOS Y FURIOSOS",
        "deportes": "COMBATE CUERPO A CUERPO",
        "materia": "MATEMÁTICAS",
        "comida": "PASTA",
        "fortalezas": "INTELECTO Y CREATIVIDAD",
        "debilidades": "LA COMIDA"
    },
    {
        "nombre": "KEIMER JESUS GONZALES INES",
        "sexo": "MASCULINO",
        "edad": 17,
        "canciones": "VALLENATO",
        "peliculas": "ROCKY IV",
        "deportes": "BALONCESTO",
        "materia": "EDUCACIÓN FÍSICA",
        "comida": "PASTA",
        "fortalezas": "FUERZA",
        "debilidades": "NICOL"
    }
]

# ---------------------------------------------------------
# LÓGICA DE LA PERSONALIDAD COLECTIVA
# ---------------------------------------------------------
def obtener_respuesta(mensaje):
    msg = mensaje.lower()

    if any(w in msg for w in ["quienes", "integrantes", "compañeros", "nombres", "grupo"]):
        nombres = ", ".join([c["nombre"] for c in companeros])
        return f"Somos un grupo integrado por 5 compañeros: {nombres}."

    elif any(w in msg for w in ["comida", "comidas", "comer", "plato"]):
        return ("En el grupo nos encanta comer: la pasta es muy popular (Juan Jose y Keimer), "
                "también nos gusta el Arroz con Pollo (Gabriela), la Pizza (Johan) y la Lasaña (Kleiber). "
                "¡Cuidado con la comida, que es la debilidad de Juan Jose!")

    elif any(w in msg for w in ["musica", "cancion", "canciones", "escuchar", "cantante"]):
        return ("Escuchamos géneros variados: Reggaeton (Gabriela), Blessd (Johan), Punk Rock (Kleiber), "
                "Vallenato (Keimer) y música variada en general (Juan Jose).")

    elif any(w in msg for w in ["pelicula", "peliculas", "cine"]):
        return ("Nuestra película grupal favorita es 'Rápidos y Furiosos' (les gusta a Gabriela y Juan Jose). "
                "Además vemos Spiderman (Johan), Jurassic Park 1993 (Kleiber) y Rocky IV (Keimer).")

    elif any(w in msg for w in ["deporte", "deportes", "jugar"]):
        return ("Somos muy deportivos: jugamos Fútbol (Johan), Voleibol (Kleiber), "
                "Combate Cuerpo a Cuerpo (Juan Jose) y Baloncesto (Keimer). A Gabriela no le atraen los deportes.")

    elif any(w in msg for w in ["materia", "estudiar", "clase", "curso"]):
        return ("Nuestras materias favoritas son: Matemáticas (Johan y Juan Jose), "
                "Física (Kleiber), Español (Gabriela) y Educación Física (Keimer).")

    elif any(w in msg for w in ["debilidad", "debilidades"]):
        return ("Nuestra principal debilidad colectiva es 'El Amor' (coinciden Gabriela, Johan y Kleiber). "
                "Por otro lado, la debilidad de Juan Jose es la comida y la de Keimer es Nicol.")

    elif any(w in msg for w in ["fortaleza", "fortalezas"]):
        return ("Destacamos por la Fuerza (Johan y Keimer), la Inteligencia (Kleiber) "
                "y la combinación de Intelecto con Creatividad (Juan Jose).")

    elif any(w in msg for w in ["edad", "edades", "años"]):
        return ("El grupo tiene entre 16 y 18 años (promedio de 16.6 años). "
                "Gabriela tiene 18, Keimer 17, y Johan, Kleiber y Juan Jose tienen 16 años.")

    elif any(w in msg for w in ["hola", "buenas", "saludos", "inicio"]):
        return "¡Hola! Soy el chatbot que reúne la voz y personalidad colectiva de Gabriela, Johan, Kleiber, Juan Jose y Keimer. ¿Qué te gustaría preguntarnos?"

    else:
        return ("Represento la personalidad de Gabriela, Johan, Kleiber, Juan Jose y Keimer. "
                "Puedes preguntarme por nuestras comidas favoritas, películas, deportes, canciones, materias o debilidades.")

# ---------------------------------------------------------
# INTERFAZ DE CHAT Y VOZ
# ---------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Historial de mensajes
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Captura de entrada del usuario
user_input = st.chat_input("Escribe tu pregunta para el grupo...")

if user_input:
    # Guardar y mostrar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Generar respuesta del bot
    respuesta_bot = obtener_respuesta(user_input)

    # Mostrar respuesta y generar audio de voz
    with st.chat_message("assistant"):
        st.write(respuesta_bot)

        # Generar archivo de audio con gTTS
        tts = gTTS(text=respuesta_bot, lang='es')
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)

        # Reproducir audio automáticamente
        st.audio(audio_bytes, format='audio/mp3', autoplay=True)

    # Guardar respuesta en el historial
    st.session_state.messages.append({"role": "assistant", "content": respuesta_bot})
