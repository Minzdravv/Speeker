
from speeker import Speeker
from langdetect import detect
from PyPDF2 import PdfReader
import os
class Readfile:
    def readfile(file):
        #check type file
        ext = os.path.splitext(file)[-1].lower()
        print(ext)
        if ext == ".txt":
            type = "txt"
            Readfile.reader(file, type)
        elif ext == ".pdf":
            type = "pdf"
            Readfile.reader(file, type)
        elif ext == ".doc" or ".docx" or ".rtx":
            type = "doc"
            Readfile.reader(file, type)
        else:
            print("File format " + ext + " not support")

    def reader(file, type):
        if type == "txt":
            f = open(file, 'r', encoding='utf-8')
            text = f.read()
            #check language
            language = detect(text)
            print("language:" + language)
            return Speeker.speek(text,language)
            f.close()
        elif type == "pdf":
            reader = PdfReader(file)
            page = reader.pages[0]
            text = page.extract_text()
            language = detect(text)
            print("language:" + language)
            return Speeker.speek(text, language)
            f.close()