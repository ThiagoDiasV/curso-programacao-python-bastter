def calcula_listas_aninhadas(lista):
    if not isinstance(lista, list):
        return f"Você inseriu um objeto do tipo {type(lista)}, que não é uma lista e não pode ser processado por nosso programa. Tente novamente."
    contador_sublistas = 0
    for item in lista:
        if isinstance(item, list):
            if len(item) > 1:
                contador_sublistas += 1
    
    return f"A lista inserida contém {contador_sublistas} lista(s) aninhadas"