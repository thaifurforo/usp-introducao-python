import pytest
from triangulos_semelhantes import *

@pytest.mark.parametrize('a, b, c, tipo_triangulo',[
    (1, 1, 1, 'equilátero'),
    (1, 1, 0, 'isósceles'),
    (0, 1, 1, 'isósceles'),
    (1, 0, 1, 'isósceles'),
    (0, 1, 2, 'escaleno'),
])
def test_tipo_triangulo(a, b, c, tipo_triangulo):
    triangulo = Triangulo(a, b, c)
    triangulo.tipo_lado() == tipo_triangulo

@pytest.mark.parametrize('a, b, c, perimetro', [
    (1, 2, 3, 6),
    (1, 1, 1, 3),
    (-1, -2, -3, -6),
    (-2, 1, 1, 0)
])
def test_triangulo(a, b, c, perimetro):
    t = Triangulo(a, b, c)
    t.perimetro() == perimetro

@pytest.mark.parametrize('a, b, c, retangulo', [
    (5, 3, 4, True),
    (8, 6, 10, True),
    (8, 15, 17, True),
    (5, 12, 13, False),
    (3, 3, 3, False),
    (2, 2, 1, False),
    (2, 1, 2, False),
    (1, 2, 2, False)
])
def test_retangulo(a, b, c, retangulo):
    t = Triangulo(a, b, c)
    t.retangulo() == retangulo

@pytest.mark.parametrize('a1, b1, c1, a2, b2, c2, semelhantes', [
    (2, 3, 5, 4, 6, 10, True),
    (1, 2, 3, 3, 6, 9, True),
    (10, 8, 4, 5, 4, 2, True),
    (1, 2, 3, 4, 5, 6, False),
    (6, 5, 4, 3, 2, 1, False)
])
def test_semelhantes(a1, b1, c1, a2, b2, c2, semelhantes):
    t1 = Triangulo(a1, b1, c1)
    t2 = Triangulo(a2, b2, c2)
    t1.semelhantes(t2) == semelhantes
