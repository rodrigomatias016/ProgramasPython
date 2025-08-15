####Teste Fatorial utilizando pytest e parametrize

def fatorial(x):
    if x < 0:
        return 0
    x2 = 1       
    while x > 1:
       x2 = x2 * x
       x = x - 1
    return x2

import pytest

@pytest.mark.parametrize("entrada, esperado", [
    (0, 1),
    (1, 1),
    (-10, 0),
    (4, 24),
    (5, 120)
    ])

def test_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado

