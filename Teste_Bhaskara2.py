####Criar uma sequência de testes para o código Teste_Bhaskara####


import Teste_Bhaskara
import pytest

class TestBhaskara: ####É necessário criar a classe com T maiúsculo para que o pyteste idenfifique como classe de teste####
    
    @pytest.fixture
    def b(self):
        return Teste_Bhaskara.Bhaskara()
    
    
    def testa_uma_raiz(self, b):
        assert b.calcula_raizes(1, 0, 0) == (1, 0)
        
    ####Exemplo dessa função sem a fixture
    ####def testa_uma_raiz(self):
    #######b = Teste_Bhaskara.Bhaskara()  
    #######assert b.calcula_raizes(1, 0, 0) == (1, 0)  

    def testa_duas_raiz(self, b):
        assert b.calcula_raizes(1, -5, 6) == (2, 3, 2)    

    def testa_zero_raiz(self, b):
        assert b.calcula_raizes(10, 10, 10) == 0

    def testa_raiz_negativa(self, b):
        assert b.calcula_raizes(10, 20, 10) == (1, -1)    
        


