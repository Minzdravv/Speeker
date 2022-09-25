from gtts import gTTS
from playsound import playsound

class Speeker:
    def __init__(self):
        text=None
        language='ru'
    def speek(text):
        # speek file
        s = gTTS(text, lang='ru')
        s.save('sample.mp3')
        return playsound('sample.mp3')