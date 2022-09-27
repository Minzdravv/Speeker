import readfile
from speeker import Speeker
from langdetect import detect

#Program
def sendToSpeeker(text):
    language = detect(text)
    print("Load text, language:" + language)
    return Speeker.speek(text, language)

try:
    file = input('Enter file:')
    sendToSpeeker(readfile.ReadFile.readFile(file))
    print(readfile.ReadFile.readFile(file))
    #sendToSpeeker(text)

except:
    print("Stop play.")