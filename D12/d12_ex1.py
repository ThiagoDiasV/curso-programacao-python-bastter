import string

texto = 'Silvio Santos Ipsum Ma o Silvio Santos Ipsum é muitoam interesanteam. Com ele ma você vai gerar textuans ha haae. Mah você mora com o papai ou com a mamãem? Ha haeeee. Hi hi. Valendo um milhão de reaisammm. Mah é a porta da esperançaam. É com você Lombardiam. Ma você, topa ou não topamm. Ma tem ou não tem o celular do milhãouamm? É com você Lombardiam. Valendo um milhão de reaisammm. O arriscam tuduam, valendo um milhão de reaisuam. Ma quem quer dinheiroam? Ma vai pra lá.'

caracteres = string.ascii_lowercase + 'záàâãéèêíïóôõöúçñ'

texto_minusculas = texto.lower()

resultados = dict()

for letra in texto_minusculas:
    if letra in caracteres:
        try:
            resultados[letra] += 1
        except KeyError:
            resultados[letra] = 1

resultados_ordenados = {k:v for k,v in sorted(resultados.items(), key=lambda x: x[1], reverse=True)}

print(resultados_ordenados)
