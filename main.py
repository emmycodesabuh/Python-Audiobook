import pyttsx3
import PyPDF2

#edit the oop.pdf to another PDF book in your folder
book = open('oop.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()

for num in range(7, pages):

    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
