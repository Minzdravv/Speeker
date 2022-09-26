from gtts import gTTS
from playsound import playsound

class Speeker:
    def __init__(self):
        text=None

    def speek(text, language):
        # speek file
        s = gTTS(text, lang = language)
        s.save('sample.mp3')
        return playsound('sample.mp3')