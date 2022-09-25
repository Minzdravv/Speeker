from speeker import Speeker
class Readfile:
    def readfile(file):
        f = open(file, 'r', encoding='utf-8')
        text = f.read()
        return Speeker.speek(text)
        f.close()