def calcula_listas_aninhadas(lista):
    contador_sublistas = 0
    for item in lista:
        if isinstance(item, list):
            contador_sublistas += 1
    
    return f"A lista inserida contém {contador_sublistas} lista(s) aninhadas"

