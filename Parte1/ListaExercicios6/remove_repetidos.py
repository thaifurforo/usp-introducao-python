def remove_repetidos(lista):
    lista.sort()
    listaOrdenada = [lista[0]]
    n = 0
    while n >= 0 and n < len(lista)-1:
        if lista[n] != lista[n+1]:
            listaOrdenada.append(lista[n+1])
        n += 1
    return listaOrdenada
