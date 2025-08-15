#Programa que mostra o método construtor da Classe e como manipular esse método



class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano    = ano
        self.cor    = cor

carro_do_meu_avo = Carro('Ferrari', 1980, 'vermelha')




