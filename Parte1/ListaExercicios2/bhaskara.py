import math

a = float(input("Digite o valor de a:"))
b = float(input("Digite o valor de b:"))
c = float(input("Digite o valor de c:"))

delta = b ** 2 - (4 * a * c)

if delta >= 0:
    raiz1 = (- b + math.sqrt(delta)) / (2 * a)
    raiz2 = (- b - math.sqrt(delta)) / (2 * a)
    if raiz1 > raiz2:
        resultado1 = raiz2
        resultado2 = raiz1
    else:
        resultado1 = raiz1
        resultado2 = raiz2


if delta > 0:
    print('as raízes da equação são', resultado1, 'e', resultado2)
elif delta == 0:
    print('a raiz desta equação é', raiz1)
else:
    print('esta equação não possui raízes reais')
