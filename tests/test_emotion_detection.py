import pytest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection:
    """Clase de pruebas para el detector de emociones"""

    def test_joy_detection(self):
        """Prueba deteccion de alegria"""
        text = "I am so happy and excited about this!"
        result = emotion_detector(text)
        assert 'joy' in result
        assert result['joy'] > 0.5
        assert result['dominant_emotion'] == 'joy'

    def test_sadness_detection(self):
        """Prueba deteccion de tristeza"""
        text = "I am very sad and disappointed."
        result = emotion_detector(text)
        assert 'sadness' in result
        assert result['dominant_emotion'] == 'sadness'

    def test_anger_detection(self):
        """Prueba deteccion de ira"""
        text = "I am furious and angry about this situation!"
        result = emotion_detector(text)
        assert 'anger' in result
        assert result['dominant_emotion'] == 'anger'

    def test_fear_detection(self):
        """Prueba deteccion de miedo"""
        text = "I am scared and worried about what might happen."
        result = emotion_detector(text)
        assert 'fear' in result
        assert result['dominant_emotion'] == 'fear'

    def test_surprise_detection(self):
        """Prueba deteccion de sorpresa"""
        text = "Wow! I can't believe this happened!"
        result = emotion_detector(text)
        assert 'surprise' in result
        assert result['dominant_emotion'] == 'surprise'

    def test_empty_string(self):
        """Prueba con cadena vacia"""
        text = ""
        result = emotion_detector(text)
        assert result is not None

    def test_none_input(self):
        """Prueba con entrada None"""
        with pytest.raises(Exception):
            emotion_detector(None)

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
