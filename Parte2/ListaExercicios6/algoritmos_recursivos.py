def fatorial(n):
    if n < 0:
        return 'não existe fatorial de número negativo'
    elif n < 1:
        return 1
    else:
        return n * fatorial(n-1) #chamada recursiva - a função fatorial está chamando a própria função fatorial

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def busca_binaria(item, lista, min=0, max=None):
    if max == None:
        max = len(lista)-1
    if max < min:
        return False
    else:
        meio = min + (max-min) // 2
    if item == lista[meio]:
        return meio
    elif item < lista[meio]:
        return busca_binaria(item, lista, min, meio-1)
    else:
        return busca_binaria(item, lista, meio+1, max)

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    lado_esquerdo = merge_sort(lista[:meio])
    lado_direito = merge_sort(lista[meio:])

    return merge(lado_esquerdo, lado_direito)

def merge(lado_esquerdo, lado_direito):
    if not lado_esquerdo:
        return lado_direito
    if not lado_direito:
        return lado_esquerdo
    if lado_esquerdo[0] < lado_direito[0]:
        return [lado_esquerdo[0]] + merge(lado_esquerdo[1:], lado_direito)
    if lado_direito[0] < lado_esquerdo[0]:
        return [lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])

