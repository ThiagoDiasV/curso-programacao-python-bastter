from random import randint

jogadas = [randint(1, 6) for x in range(100)]

contador = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
}

for jogada in jogadas:
    contador[str(jogada)] += 1

print(f"O número 1 foi lançado {contador['1']} vezes.")
print(f"O número 2 foi lançado {contador['2']} vezes.")
print(f"O número 3 foi lançado {contador['3']} vezes.")
print(f"O número 4 foi lançado {contador['4']} vezes.")
print(f"O número 5 foi lançado {contador['5']} vezes.")
print(f"O número 6 foi lançado {contador['6']} vezes.")