def fatorial(n):
    if n < 0:
        return 'não existe fatorial de número negativo'
    elif n < 1:
        return 1
    else:
        return n * fatorial(n-1) #chamada recursiva - a função fatorial está chamando a própria função fatorial
