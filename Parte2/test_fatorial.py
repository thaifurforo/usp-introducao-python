from fatorial import *
import pytest

@pytest.mark.parametrize('entrada, esperado', [
    (0, 1),
    (1, 1),
    (-10, 0),
    (4, 24),
    (5, 120)
])

def testa_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado