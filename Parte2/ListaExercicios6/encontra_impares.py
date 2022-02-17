def encontra_impares(lista):
    if len(lista) == 0:
        return lista
    elif lista[0] % 2 == 0:
        return encontra_impares(lista[1:])
    else:
        return [lista[0]] + encontra_impares(lista[1:])