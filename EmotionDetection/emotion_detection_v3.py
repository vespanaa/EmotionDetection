from watson_nlp_lib import NLP

def emotion_detector(text):
    """
    Funcion que detecta emociones en un texto usando Watson NLP.

    Parametros:
    text (str): El texto a analizar

    Retorna:
    dict: Diccionario con las emociones detectadas, sus puntuaciones y la emocion dominante.
          Si el texto esta vacio, devuelve None.
    """
    # Validar entrada
    if text is None or text.strip() == "":
        return None

    try:
        # Cargar el modelo preentrenado de emociones
        nlp = NLP()

        # Analizar el texto
        result = nlp.emotion.predict(text)

        # Obtener las emociones y sus puntuaciones
        emotions = result['emotions']

        # Crear diccionario de resultados con formato correcto
        emotion_dict = {}
        for emotion in emotions:
            emotion_dict[emotion['emotion']] = emotion['score']

        # Determinar la emocion dominante
        dominant_emotion = max(emotions, key=lambda x: x['score'])
        emotion_dict['dominant_emotion'] = dominant_emotion['emotion']

        return emotion_dict

    except Exception as e:
        print(f"Error en la deteccion de emociones: {str(e)}")
        return None

# Prueba basica
if __name__ == "__main__":
    # Prueba con texto valido
    test_text = "I am so happy and excited about this!"
    result = emotion_detector(test_text)
    print(f"Texto: {test_text}")
    print(f"Resultado: {result}")

    # Prueba con texto vacio
    empty_text = ""
    result_empty = emotion_detector(empty_text)
    print(f"\nTexto vacio: '{empty_text}'")
    print(f"Resultado: {result_empty}")

    # Prueba con None
    result_none = emotion_detector(None)
    print(f"\nEntrada None: {result_none}")
