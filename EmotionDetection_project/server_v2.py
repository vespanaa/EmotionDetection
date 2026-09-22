from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """Pagina de inicio"""
    return "Bienvenido a la API de Deteccion de Emociones"

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Endpoint para detectar emociones en texto.

    Espera un JSON con la estructura: {"text": "texto a analizar"}
    """
    data = request.get_json()

    # Validar que se proporciono JSON
    if not data:
        return jsonify({'error': 'No se proporciono datos JSON'}), 400

    # Validar que existe el campo 'text'
    if 'text' not in data:
        return jsonify({'error': 'El campo "text" es requerido'}), 400

    text = data['text']

    # Validar que el texto no esta vacio o es None
    if text is None or text.strip() == '':
        return jsonify({'error': 'El texto no puede estar vacio'}), 400

    try:
        result = emotion_detector(text)

        # Si emotion_detector devuelve None, retornar error 400
        if result is None:
            return jsonify({'error': 'No se pudo analizar el texto'}), 400

        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': f'Error interno: {str(e)}'}), 500

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion_get():
    """
    Endpoint GET para detectar emociones (acepta parametro 'text' en query string).
    """
    text = request.args.get('text', '')

    if not text or text.strip() == '':
        return jsonify({'error': 'El parametro "text" es requerido y no puede estar vacio'}), 400

    try:
        result = emotion_detector(text)

        if result is None:
            return jsonify({'error': 'No se pudo analizar el texto'}), 400

        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': f'Error interno: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
