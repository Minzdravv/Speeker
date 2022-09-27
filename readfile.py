

from PyPDF2 import PdfReader
import os
class ReadFile:
    def readFile(file):
        #check type file
        ext = os.path.splitext(file)[-1].lower()
        #print(ext)
        if ext == ".txt":
            type = "txt"
            return ReadFile.reader(file, type)
        elif ext == ".pdf":
            type = "pdf"
            return ReadFile.reader(file, type)
        elif ext == ".doc" or ".docx" or ".rtx":
            type = "doc"
            return ReadFile.reader(file, type)
        else:
            print("File format " + ext + " not support")
            return
    def reader(file, type):
        if type == "txt":
            f = open(file, 'r', encoding='utf-8')
            return f.read()
        elif type == "pdf":
            reader = PdfReader(file)
            page = reader.pages[0]
            return page.extract_text()