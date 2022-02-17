import pytest
from algoritmos_recursivos import *

@pytest.mark.parametrize('numero, resultado',[
    (-1, 'não existe fatorial de número negativo'),
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (7, 5040)
])
def test_fatorial(numero, resultado):
    assert fatorial(numero) == resultado

@pytest.mark.parametrize('numero, resultado',[
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13)
])
def test_fibonacci(numero, resultado):
    assert fibonacci(numero) == resultado

@pytest.mark.parametrize('item, lista, resultado',[
    (0, [0, 1, 2, 3, 4, 5], 0),
    (3, [0, 1, 2, 3, 4, 5], 3),
    (7, [1, 3, 5, 7, 9, 11], 3),
    (5, [1, 3, 5, 7, 9, 11], 2),
    (1, [1, 2, 3, 4, 5, 6], 0),
    (2, [1, 2, 3, 4, 5, 6], 1),
    (9, [1, 3, 5, 7, 9, 11], 4),
    (6, [1, 2, 3, 4, 5, 6], 5),
                         ])
def test_busca_binaria(item, lista, resultado):
    assert busca_binaria(item, lista) == resultado

@pytest.mark.parametrize('lista, resultado',[
    ([7, 8, 6, 3, 4, 1, 2, 9, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9])
])
def test_merge_sort(lista, resultado):
    assert merge_sort(lista) == resultado