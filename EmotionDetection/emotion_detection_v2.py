from watson_nlp_lib import NLP

def emotion_detector(text):
    """
    Funcion que detecta emociones en un texto usando Watson NLP.

    Parametros:
    text (str): El texto a analizar

    Retorna:
    dict: Diccionario con las emociones detectadas, sus puntuaciones y la emocion dominante
    """
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

# Prueba basica
if __name__ == "__main__":
    test_text = "I am so happy and excited about this!"
    result = emotion_detector(test_text)
    print(f"Texto: {test_text}")
    print(f"Resultado: {result}")
    print(f"Emocion dominante: {result['dominant_emotion']}")
