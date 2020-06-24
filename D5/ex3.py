n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))


def pega_menor(n1, n2):
    if n1 > n2:
        return n2
    elif n1 < n2:
        return n1
    else:
        return "Os dois são iguais"


resultado = pega_menor(n1, n2)
print(resultado)
