n = 1
lista = []
while n != 0:
    n = int(input('Digite um número inteiro:'))
    lista.append(n)

i = -2
while i <= 0 and i >= 0 - len(lista):
    print(lista[i])
    i -= 1
