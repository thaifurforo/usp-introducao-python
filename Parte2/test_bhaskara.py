import pytest

from bhaskara_refatorado import *
import pytest

class TestBhaskara:

    @pytest.fixture
    def b(self):
        return Bhaskara()

    def testa_raiz01(self, b):
        assert b.calcula_raizes(1, 0, 0) == (1, 0)
    def testa_raiz02(self, b):
        assert b.calcula_raizes(1, -5, 6) == (2, 3, 2)
    def testa_raiz03(self, b):
        assert b.calcula_raizes(10, 10, 10) == 0
    def testa_raiz04(self, b):
        assert b.calcula_raizes(10, 20, 10) == (1, -1)

    @pytest.mark.parametrize('entrada1, entrada2, entrada3, valor_esperado',
                             [(1, 0, 0, (1, 0)),
                              (1, -5, 6, (2, 3, 2)),
                              (10, 10, 10, 0),
                              (10, 20, 10, (1, -1))])

    def testa_raiz(self, entrada1, entrada2, entrada3, valor_esperado):
        b = Bhaskara()
        assert b.calcula_raizes(entrada1, entrada2, entrada3) == valor_esperado

