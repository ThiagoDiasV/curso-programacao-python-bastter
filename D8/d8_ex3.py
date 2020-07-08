import os

# Checa se a pasta de resultados já existe.
# Se não existir, cria a pasta
if not 'resultados' in os.listdir('.'):
    os.mkdir(f'{os.path.abspath("")}/resultados')

with open('resultados/silvio_ex2.txt', 'r') as arquivo:
    for line in arquivo:
        if 'Mah' in line or 'Ma' in line:
            print(line)