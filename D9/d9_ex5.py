def retorna_lista_fatiada_sem_extremos(lista):
    if not isinstance(lista, list):
        return f"Você inseriu um objeto do tipo {type(lista)}, que não é uma lista e não pode ser processado por nosso programa. Tente novamente."
    return lista[1:-1]