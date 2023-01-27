import pyttsx3,PyPDF2

#Rename pdf as you like
pdfreader = PyPDF2.PdfFileReader(open('sample.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
#Rename mp3 as you like
speaker.save_to_file(clean_text, 'sample.mp3')
speaker.runAndWait()

speaker.stop()