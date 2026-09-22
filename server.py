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

    if not data or 'text' not in data:
        return jsonify({'error': 'No se proporciono texto'}), 400

    text = data['text']

    if not text or text.strip() == '':
        return jsonify({'error': 'El texto no puede estar vacio'}), 400

    try:
        result = emotion_detector(text)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
