import json
import spacy
from difflib import get_close_matches
from spellchecker import SpellChecker

# Cargar el modelo de lenguaje de spaCy
nlp = spacy.load("es_core_news_sm")

# Cargar datos desde el archivo JSON
with open("padecimientos.json", "r") as json_file:
    data = json.load(json_file)["padecimientos"]  # Accede a la clave "padecimientos"

# Función para corregir ortografía en el mensaje del usuario
def corregir_ortografia(mensaje_usuario):
    spell = SpellChecker(language="es")
    palabras = mensaje_usuario.split()
    palabras_corregidas = []

    for palabra in palabras:
        palabra_corregida = spell.correction(palabra)
        palabras_corregidas.append(palabra_corregida)

    return " ".join(palabras_corregidas)

# Función para detectar padecimientos y mostrar medicamentos
import spacy
import difflib

nlp = spacy.load("es_core_news_sm")

def detectar_padecimiento(mensaje_usuario, data):
    palabras_clave = mensaje_usuario.lower().split()
    mejor_coincidencia = None
    umbral_similitud = 0.6  # Ajusta el umbral según la similitud deseada

    for palabra in palabras_clave:
        for padecimiento, info in data.items():
            sintomas = info["sintomas"]
            for sintoma in sintomas:
                similitud = difflib.SequenceMatcher(None, palabra, sintoma).ratio()
                if similitud >= umbral_similitud:
                    mejor_coincidencia = padecimiento
                    break

            if mejor_coincidencia:
                break

        if mejor_coincidencia:
            break

    if mejor_coincidencia:
        padecimiento_info = data[mejor_coincidencia]
        nombre_padecimiento = mejor_coincidencia
        medicamentos = padecimiento_info["medicamentos"]
        return f"Tienes {nombre_padecimiento}. Puedes considerar tomar {', '.join(medicamentos)} para aliviar los síntomas."

    return None


# Ejemplo de interacción
print("Hola, soy un chatbot. Puedes escribir 'salir' para finalizar la conversación.")

while True:
    mensaje = input("Tú: ")
    if mensaje.lower() == 'salir':
        break

    respuesta = detectar_padecimiento(mensaje, data)

    if respuesta:
        print("Chatbot:", respuesta)
    else:
        print("Chatbot: No entiendo tu pregunta. ¿Puedes ser más específico?")
