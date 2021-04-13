#https://pymupdf.readthedocs.io/en/latest/document.html#Document.metadata
import fitz #PyMuPDF Library
fileName = "c:/Coding Samples/Python/evd.pdf" #File path
doc=fitz.open(fileName)

print("Previous table of properties...")
print(doc.metadata)
doc.set_metadata({}) #Clear TOC with a clean dictionary {}
print("=====")
print("After modication of TOC...")
#Let's create our new TOC
mytitle="Sample project record"
myformat="PDF 1.3"
meauthor="EVD Click Coding Technology"
mysubject="Software Design Area"
mykeywords="PDF Property table modification, custon TOC and some other stuffs"
myapp='Data Manipulation'

#Let's set our new TOC for PDF
doc.set_metadata({'format': myformat,
                  'title': mytitle,
                  'author': meauthor,
                  'subject': mysubject,
                  'keywords': mykeywords,
                  'creator': myapp,
                  'producer': 'PyMuPDF',
                  'creationDate': '20130917',
                  'modDate': '20210410',
                  'trapped': '',
                  'encryption': None})
#Print our new TOC and Save changes in a new file
print(doc.metadata)
doc.save("c:/Coding Samples/Python/evd customized TOC.pdf", garbage = 4)
doc.close() #Close file
print("File saved... check modified TOC in new file")
