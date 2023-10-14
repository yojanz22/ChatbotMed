import json

# Cargar datos desde el archivo JSON
with open("padecimientos.json", "r") as json_file:
    data = json.load(json_file)["padecimientos"]

# Inicializar el contexto
contexto = ""

# Mensaje de bienvenida
print("Hola, soy un chatbot. ¿En qué puedo ayudarte? Indica tu problema o hazme una pregunta.")

# Función para detectar padecimientos y mostrar medicamentos
def detectar_padecimiento(mensaje_usuario, data, contexto):
    palabras_clave = mensaje_usuario.lower().split()
    mejor_coincidencia = None
    umbral_similitud = 0.6  # Ajusta el umbral según la similitud deseada

    for palabra in palabras_clave:
        for padecimiento, info in data.items():
            sintomas = info["sintomas"]
            for sintoma in sintomas:
                if sintoma in mensaje_usuario:
                    mejor_coincidencia = padecimiento
                    break

            if mejor_coincidencia:
                break

        if mejor_coincidencia:
            break

    if mejor_coincidencia:
        # Utiliza el JSON de datos para generar una respuesta personalizada
        padecimiento_info = data[mejor_coincidencia]
        nombre_padecimiento = mejor_coincidencia
        medicamentos = padecimiento_info["medicamentos"]

        # Construye una respuesta personalizada
        respuesta = f"Basado en tus síntomas, parece que podrías tener {nombre_padecimiento}. Los medicamentos que podrían ayudarte son: {', '.join(medicamentos)}. ¿Necesitas más información o tienes alguna otra pregunta?"

        contexto = mensaje_usuario  # Actualiza el contexto con el mensaje del usuario
        return respuesta

    return None

# Ejemplo de interacción
while True:
    mensaje = input("Tú: ")
    if mensaje.lower() == 'salir':
        break

    # Responder a saludos
    if mensaje.lower() in ["hola", "¡hola", "buenos días", "buenas tardes", "buenas noches"]:
        print("Chatbot: Hola, ¿en qué puedo ayudarte? Indica tu problema o hazme una pregunta.")
    else:
        respuesta = detectar_padecimiento(mensaje, data, contexto)

        if respuesta:
            print("Chatbot:", respuesta)
        else:
            print("Chatbot: No entiendo tu pregunta. ¿Puedes ser más específico?")
