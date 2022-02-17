class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b and self.b == self.c:
            return 'equilátero'
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return 'isósceles'
        else:
            return 'escaleno'

    def retangulo(self):
        lados = [self.a, self.b, self.c]
        hipotenusa = max(lados)
        catetos = [lado for lado in lados if lado != hipotenusa]
        if self.a == self.b and self.b == self.c:
            catetos.append(self.a)
            catetos.append(self.b)
        elif hipotenusa == self.a and hipotenusa == self.b:
            catetos.append(self.a)
        elif hipotenusa == self.a and hipotenusa == self.c:
            catetos.append(self.a)
        elif hipotenusa == self.b and hipotenusa == self.c:
            catetos.append(self.b)
        return hipotenusa ** 2 == (catetos[0] ** 2) + (catetos[1] ** 2)

    def semelhantes(self, triangulo):
        return self.a / triangulo.a == self.b / triangulo.b and self.b / triangulo.b == self.c / triangulo.c
