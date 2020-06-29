import pytesseract
import os
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
inputpath = r'C:\Users\sarth\OneDrive\Desktop\CS Question Bank\\'
outputpath = r'C:\Users\sarth\OneDrive\Desktop\scanned1\\'
outputname = 0
for filename in os.listdir(inputpath):
    img = Image.open(inputpath + filename)
    text = pytesseract.image_to_string(img)
    outputname += 1
    file = open(outputpath + str(outputname),"w")
    file.write(text)

