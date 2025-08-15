def fatorial(x):
    if x < 0:
        return 0
    x2 = 1       
    while x > 1:
       x2 = x2 * x
       x = x - 1
    return x2

def test_fatorial0():
    assert fatorial(0) == 1

def test_fatorial():
    assert fatorial(1) == 1

def test_fatorial_negativo():
    assert fatorial(-10) == 0

def test_fatorial4():
    assert fatorial(4) == 24

def test_fatorial5():
    assert fatorial(5) == 120
    
