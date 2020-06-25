string = input('Digite uma palavra: ')

# Método 1
contador_letras_a = 0
for letter in string:
    if letter == 'a':
        contador_letras_a += 1

print(f"Há {contador_letras_a} letras 'a' na palavra {string}")
