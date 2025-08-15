####Conta o tempo de execução, neste caso de programas de busca e seleção

import Busca_Selecao_Direta
import Busca_Bolha_Curta
import random
import time

class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)] # imteiros entre 0 e 999
        return lista   

    def lista_quase_ordenada(self, n): 
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista

    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]
        lista3 = lista1[:]
        

        o = Busca_Selecao_Direta.Ordenador()
        b = Busca_Bolha_Curta.Ordenador()

        print("Comparando com listas aleatorias")
        
        antes = time.time()
        b.bolha_curta(lista1)
        depois = time.time()
        print("Bolha curta demorou ", depois - antes)

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("Selecao direta demorou ", depois - antes)

        antes = time.time()
        b.insercao_direta(lista3)
        depois = time.time()
        print("Insercao direta demorou ", depois - antes)      


        print("\nComparando com quase ordenadas")

        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:]
        lista3 = lista1[:]
        
        antes = time.time()
        b.bolha_curta(lista1)
        depois = time.time()
        print("Bolha curta demorou ", depois - antes)

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("Selecao direta demorou ", depois - antes)

        antes = time.time()
        b.insercao_direta(lista3)
        depois = time.time()
        print("Insercao direta demorou ", depois - antes)



