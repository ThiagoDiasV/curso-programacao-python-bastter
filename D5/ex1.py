altura = float(input("Digite sua altura em metros: ").replace(",", "."))
peso = float(input("Digite seu peso em Kg: ").replace(",", "."))

imc = round(peso / (altura * altura), 2)


def calc_imc(imc):
    """
    Calcula IMC e retorna resultado
    """
    if imc < 18.5:
        mensagem = "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        mensagem = "Peso normal"
    elif 25 < imc < 29.9:
        mensagem = "Sobrepeso"
    elif 30 < imc < 34.9:
        mensagem = "Obesidade Grau I"
    elif 35 < imc < 39.9:
        mensagem = "Obesidade Grau II"
    elif imc > 40:
        mensagem = "Obesidade Grau III"

    return f"Seu IMC é de {str(imc).replace('.', ',')} - {mensagem}"


mensagem = calc_imc(imc)

print(mensagem)
