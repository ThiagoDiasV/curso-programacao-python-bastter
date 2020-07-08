from docx import Document
import os

# Checa se a pasta de resultados já existe.
# Se não existir, cria a pasta
if not 'resultados' in os.listdir('.'):
    os.mkdir(f'{os.path.abspath("")}/resultados')


document = Document()

with open('resultados/silvio_ex2.txt', 'r') as arquivo:
    for line in arquivo:
        document.add_paragraph(line)

document.save('resultados/silvio.docx')