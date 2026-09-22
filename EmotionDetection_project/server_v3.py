"""
Servidor Flask para la aplicacion de Deteccion de Emociones.

Este modulo proporciona endpoints REST para analizar emociones en texto
utilizando la biblioteca Watson NLP de IBM.
"""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def home():
    """
    Pagina de inicio de la API.

    Returns:
        str: Mensaje de bienvenida
    """
    return "Bienvenido a la API de Deteccion de Emociones"


@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Endpoint POST para detectar emociones en texto.

    Espera un JSON con la estructura: {"text": "texto a analizar"}

    Returns:
        tuple: (response, status_code)
            - response: JSON con las emociones detectadas o mensaje de error
            - status_code: 200 (exito), 400 (error cliente), 500 (error servidor)
    """
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No se proporciono datos JSON'}), 400

    if 'text' not in data:
        return jsonify({'error': 'El campo "text" es requerido'}), 400

    text = data['text']

    if text is None or text.strip() == '':
        return jsonify({'error': 'El texto no puede estar vacio'}), 400

    try:
        result = emotion_detector(text)

        if result is None:
            return jsonify({'error': 'No se pudo analizar el texto'}), 400

        return jsonify(result), 200

    except Exception as exception_error:
        return jsonify({'error': f'Error interno: {str(exception_error)}'}), 500


@app.route('/emotionDetector', methods=['GET'])
def detect_emotion_get():
    """
    Endpoint GET para detectar emociones.

    Acepta parametro 'text' en query string.

    Returns:
        tuple: (response, status_code)
    """
    text = request.args.get('text', '')

    if not text or text.strip() == '':
        return jsonify({'error': 'El parametro "text" es requerido'}), 400

    try:
        result = emotion_detector(text)

        if result is None:
            return jsonify({'error': 'No se pudo analizar el texto'}), 400

        return jsonify(result), 200

    except Exception as exception_error:
        return jsonify({'error': f'Error interno: {str(exception_error)}'}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
