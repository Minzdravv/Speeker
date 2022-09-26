
from readfile import ReadFile

#Program

file = input('Enter file:')
try:
    ReadFile.readFile(file)
except:
    print("Stop play.")