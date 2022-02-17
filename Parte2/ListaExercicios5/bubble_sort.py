def bubble_sort(lista):
    for index in range(len(lista)):
        for index in range(len(lista)-1):
            if lista[index] >= lista[index+1]:
                lista[index], lista[index+1] = lista[index+1], lista[index]
                print(lista)
    return lista
