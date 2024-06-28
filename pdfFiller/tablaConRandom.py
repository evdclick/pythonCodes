#Como primer paso debemos tratar de leer el contenido del archivo PDF mediante la librería PyPDF2
#https://pypi.org/project/PyPDF2/
from PyPDF2 import PdfReader, PdfWriter
import os
import random #Es para poder generar números aleatorios en los criterios especificados

listadoDir = os.listdir()
soloPDFs = []
for misPDFs in listadoDir:
 if misPDFs[-4:] == '.pdf': #Este renglón es para estar seguro que el archivo en la carpta actual es PDF
  soloPDFs.append(misPDFs)
  print(misPDFs)


for arcPDF in soloPDFs:
 reader = PdfReader(arcPDF)
 writer = PdfWriter()
 numberOfPages = len(reader.pages)
 page = reader.pages[0]     #Leer pagina 0
 writer.add_page(page)
 textContent = page.extract_text() #Extraer el contenido de la página cero

 #print(textContent) #Ya en este punto hay una base para explorar el contenido y rellenar los campos segun
                   #los criterios que solicitas

                  
 celdasParaLlenar = reader.get_form_text_fields() #Las celdas para llenar son registros disponibles
                                                 #Y los voy a meter en un diccionario para fácil
                                                 #procesamiento 
 """Al imprimir el diccionario de las celdasParaLlenar 
 obtento una serie de items que se resume en las siguientes listas para
 aplicar los criterios que mencionas de evaluar su contenido y aplicar
 el número aleatorio que dices para cada caso:
 listKeyCoords1 = ["T",[9,64]] Aplicar valores entre 0.04 y 0.1
 listKeyCoords2 = ["E", [1, 52] Aplicar valores entre 0.07 y 0.18
 listKeyCoords3 = ["EE", [1, 7] Aplicar valores entre 0.07 y 0.18
 """
 print(celdasParaLlenar)
 #Se procede entonces a alimentar tres listas que permitan identificar ese conjunto de celdas
 #Para así evaluarlas y poder aplicar los criterios de llenar con número aleatorio
 bex1 = [] #Lista que relaciona las keys que aplican para valores aleatorios entre 0.04 y 0.1 
 bex2 = [] #Lista que relaciona las keys que aplican para valores aleatorios entre 0.07 y 0.18
 bex3 = [] #Lista que relaciona las keys que aplican para valores aleatorios entre 0.07 y 0.18
 for i in range(9,64):
  bex1.append('T'+str(i))
 for i in range(1,52):
  bex2.append('E'+str(i))
 for i in range(1,7):
  bex3.append('EE'+str(i))

 r=[]
 for i in range(193):
 
  if i>11 and i<74:
   p1 = 0
   for j in range(200):
    p1=round(random.uniform(0.04,0.1),2)
   r.append([True, p1])
  elif i>95 and i<153:
   p1 = 0
   for j in range(250):
    p1 = round(random.uniform(0.07,0.18),2)
   r.append([True, p1])
  elif i>112 and i<117:
   p1 = 0
   for j in range(300):
    p1 = round(random.uniform(0.07,0.18),2)   
   r.append([True, p1])
  else:
   r.append([False, 0])

 mol=0

#https://pypdf2.readthedocs.io/en/3.x/user/forms.html
#En este punto voy a enumerar todas las celdas disponibles para poder cargarle los números aleatorios
#que recomiendas usar según la solicitud.
#fieldEnumerator=0
 for key, value in celdasParaLlenar.items():
  #print (key,value)
  if r[mol][0]==True and value!=None: #Estar seguro que la celda contiene algún número
   fol = r[mol][1]
   fol = str(fol)
   fol = fol.replace('.', ',')
   writer.update_page_form_field_values(writer.pages[0], {key: fol})   #Procedo a llenar con números aleatorios entre 0.04 y 0.1
  mol+=1

 #reader.close()
 os.remove(arcPDF) 
# write "output" to PyPDF2-output.pdf
 with open(arcPDF, "wb") as output_stream:
  writer.write(output_stream)
