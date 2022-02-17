import math

class Bhaskara:

    def delta(self, a, b, c):
        return b ** 2 - (4 * a * c)

    def calcula_raizes(self, a, b, c):
        delta = self.delta(a, b, c)
        if delta > 0:
            raiz1 = (- b + math.sqrt(delta)) / (2 * a)
            raiz2 = (- b - math.sqrt(delta)) / (2 * a)
            return 2, raiz1, raiz2
        elif delta == 0:
            raiz = (- b + math.sqrt(delta)) / (2 * a)
            return 1, raiz
        else:
            return 0

    def main(self):
        a = float(input("Digite o valor de a:"))
        b = float(input("Digite o valor de b:"))
        c = float(input("Digite o valor de c:"))
        calculo = self.calcula_raizes(a, b, c)
        if calculo == 0:
            print('esta equação não possui raízes reais')
        elif calculo[0] == 2:
            print('as raízes da equação são', calculo[1], 'e', calculo[2])
        elif calculo[0] == 1:
            print('a raiz desta equação é', calculo[1])

bhaskara = Bhaskara()
if __name__ == '__main__':
    bhaskara.main()
