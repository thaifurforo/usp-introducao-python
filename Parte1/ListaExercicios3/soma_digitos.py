valor = int(input('Digite um número inteiro: '))
soma = 0
digito = 1
while (valor != 0):
    digito = valor % 10
    soma += digito
    valor = valor // 10
print(soma)
