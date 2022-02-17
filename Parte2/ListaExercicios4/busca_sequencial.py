def ordenada(lista):
    bool_ordenar = []
    for index, item in enumerate(lista):
        if item >= lista[index-1] or index == 0:
            bool_ordenar.append(True)
        else:
            bool_ordenar.append(False)
    return all(bool_ordenar)

