def calcula_listas_aninhadas_soma_valores(lista):
    if not isinstance(lista, list):
        return f"Você inseriu um objeto do tipo {type(lista)}, que não é uma lista e não pode ser processado por nosso programa. Tente novamente."
    contador_sublistas = 0
    for index in range(len(lista)):
        if isinstance(lista[index], list):
            lista[index] = sum(lista[index])
    
    return lista