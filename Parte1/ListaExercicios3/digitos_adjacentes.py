num = int(input('Digite um número inteiro: '))

numeroAdjacente = False

while num != 0 and not numeroAdjacente:
    digito1 = num % 10
    num = num // 10
    digito2 = num % 10
    if digito1 == digito2:
        numeroAdjacente = True
    digito1 = digito2

if numeroAdjacente:
    print('sim')
else:
    print('não')
