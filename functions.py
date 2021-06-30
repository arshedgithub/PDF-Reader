import PyPDF2
import pyttsx3


speaker = pyttsx3.init()


def getFile(file_name):
    file = open(file_name, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(file)

    pages = pdf_reader.numPages
    print(f"This file has {pages} pages\n")

    start = input("Press 1 to start : ")
    if start == '1':
        page = pdf_reader.getPage(1)

        text = page.extractText()
        print(text)

        speaker.say(text)
        speaker.runAndWait()
