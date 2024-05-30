#Como primer paso debemos tratar de leer el contenido del archivo PDF mediante la librería PyPDF2
#https://pypi.org/project/PyPDF2/
from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("base.pdf")
writer = PdfWriter()
numberOfPages = len(reader.pages)
page = reader.pages[0]     #Leer pagina 0 porque es la única que tenemos
writer.add_page(page)      #Preparar una página en blanco para un nuevo archivo
textContent = page.extract_text() #Extraer el contenido de la página cero

print(textContent) #Ya en este punto hay una base para explorar el contenido y rellenar los campos segun
                   #los criterios que solicitas

celdasParaLlenar = reader.get_form_text_fields() #Las celdas para llenar son registros disponibles
                                                 #Y los voy a meter en un diccionario para fácil
                                                 #procesamiento
#https://pypdf2.readthedocs.io/en/3.x/user/forms.html
#En este punto voy a enumerar todas las celdas disponibles para poder cargarle los números aleatorios
#que recomiendas usar según la solicitud.
fieldEnumerator=0
for key, values in celdasParaLlenar.items():
 writer.update_page_form_field_values(
    writer.pages[0], {key: fieldEnumerator})   #Procedo a llenar con números consecutivos iniciando desde CERO
 fieldEnumerator+=1

# write "output" to PyPDF2-output.pdf
with open("conCamposEnumerados.pdf", "wb") as output_stream:
    writer.write(output_stream)
