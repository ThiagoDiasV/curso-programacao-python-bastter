def calcula_listas_aninhadas(lista):
    contador_sublistas = 0
    for item in lista:
        if isinstance(item, list):
            if len(item) > 1:
                contador_sublistas += 1
    
    return f"A lista inserida contém {contador_sublistas} lista(s) aninhadas"

