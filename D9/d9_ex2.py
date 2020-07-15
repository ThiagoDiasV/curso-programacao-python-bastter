def calcula_listas_aninhadas(lista_ou_nao):
    if not isinstance(lista_ou_nao, list):
        return f"Você inseriu um objeto do tipo {type(lista_ou_nao)}, que não é uma lista e não pode ser processado por nosso programa. Tente novamente."
    contador_sublistas = 0
    for item in lista_ou_nao:
        if isinstance(item, list):
            contador_sublistas += 1
    
    return f"A lista inserida contém {contador_sublistas} lista(s) aninhadas"