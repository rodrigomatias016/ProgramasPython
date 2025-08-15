####Criar uma sequência de testes para o código Teste_Bhaskara utilizando o parametrize####


import Teste_Bhaskara
import pytest

class TestBhaskara: ####É necessário criar a classe com T maiúsculo para que o pyteste idenfifique como classe de teste#### 


    @pytest.mark.parametrize("entrada1, entrada2, entrada3, esperado1, esperado2", [
        (1, 0, 0, 1, 0),
        (10, 20, 10, 1, -1)
        ])
    def testa_uma_raiz(self, entrada1, entrada2, entrada3, esperado1, esperado2):
        b = Teste_Bhaskara.Bhaskara()
        assert b.calcula_raizes(entrada1, entrada2, entrada3) == (esperado1, esperado2)

    @pytest.mark.parametrize("entrada1, entrada2, entrada3, esperado1, esperado2, esperado3", [
        (1, -5, 6, 2, 3, 2)
        ])
    def testa_duas_raizes(self, entrada1, entrada2, entrada3, esperado1, esperado2, esperado3):
        b = Teste_Bhaskara.Bhaskara()
        assert b.calcula_raizes(entrada1, entrada2, entrada3) == (esperado1, esperado2, esperado3)

    @pytest.mark.parametrize("entrada1, entrada2, entrada3, esperado1", [
        (10, 10, 10, 0)
        ])
    def testa_zero_raiz(self, entrada1, entrada2, entrada3, esperado1):
        b = Teste_Bhaskara.Bhaskara()
        assert b.calcula_raizes(entrada1, entrada2, entrada3) == esperado1