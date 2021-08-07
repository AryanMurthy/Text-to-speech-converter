import PyPDF2
import pyttsx3
book = open('Camelot.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(0, pages):
    page = pdfReader.getPage(0)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()