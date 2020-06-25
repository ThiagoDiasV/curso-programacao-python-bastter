palavra = input('Digite uma palavra para saber se ela é um palíndromo: ')
print('Obs: palíndromos são palavras que lidas de trás pra frente são iguais à leitura de frente pra trás')

palavra_inversa = palavra[::-1]

if palavra == palavra_inversa:
    print(f"A palavra '{palavra}' é um palíndromo")
else:
    print(f"A palavra '{palavra}' não é um palíndromo")