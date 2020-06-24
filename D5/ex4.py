from random import randint


def computador_calcula_numero():
    comp = randint(1, 3)

    return comp


def usuario_escolhe_numero_e_compara():
    comp = computador_calcula_numero()
    numero_usuario = int(input("Digite um número entre 1 e 3: "))

    if comp == numero_usuario:
        print("Você acertou, o computador escolheu {}".format(comp))
    else:
        print("Você errou, o computador escolheu {}".format(comp))


usuario_escolhe_numero_e_compara()
