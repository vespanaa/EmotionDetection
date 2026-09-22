# Emotion Detection Application

## Descripcion del Proyecto
Esta aplicacion utiliza la biblioteca Watson NLP de IBM para detectar emociones en texto. La aplicacion identifica cinco emociones principales: alegria, tristeza, ira, miedo y sorpresa.

## Caracteristicas Principales
- Deteccion de emociones en tiempo real
- API RESTful construida con Flask
- Manejo de errores para entradas invalidas
- Pruebas unitarias completas
- Analisis de codigo estatico con pylint

## Requisitos
- Python 3.8+
- watson-nlp-lib
- Flask
- pytest

## Instalacion
```bash
pip install watson-nlp-lib flask pytest
```

## Uso
```bash
python server.py
```

La aplicacion estara disponible en http://localhost:5000

## Estructura del Proyecto
```
EmotionDetection/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── tests/
│   └── test_emotion_detection.py
├── server.py
├── README.md
└── requirements.txt
```

## Autor
Proyecto desarrollado como parte del curso de IBM sobre desarrollo de aplicaciones AI con Python y Flask.
