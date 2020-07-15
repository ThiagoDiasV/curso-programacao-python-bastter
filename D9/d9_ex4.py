def calcula_listas_aninhadas_soma_valores_somente_pares(lista):
    if not isinstance(lista, list):
        return f"Você inseriu um objeto do tipo {type(lista)}, que não é uma lista e não pode ser processado por nosso programa. Tente novamente."
    contador_sublistas = 0
    for index in range(len(lista)):
        if isinstance(lista[index], list):
            numeros_pares = []
            for sub_item in lista[index]:
                if sub_item % 2 == 0:
                    numeros_pares.append(sub_item)
            soma_pares = sum(numeros_pares)
            lista[index] = soma_pares
    
    return lista