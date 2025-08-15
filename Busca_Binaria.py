####Busca sequencial e busca binária (divide os elementos até encontrar o número em uma lista já ordenada)

import time
import Busca_Criar_Listas

class Buscador:
    def busca_sequencial(self, lista, x):
        antes = time.time()
        for i in range(len(lista)):
            if lista[i] == x:
                depois = time.time()
                print ("Tempo busca sequencial", depois - antes)
                return i
        depois = time.time()
        print ("Tempo", depois - antes)  
        return -1
        
    
    def busca_binaria(self, lista, x):
        antes = time.time()
        primeiro = 0
        ultimo = len(lista)-1

        while primeiro <= ultimo:
            meio = (primeiro + ultimo)//2
            if lista[meio] == x:
                depois = time.time()
                print ("Tempo busca binaria", depois - antes)
                return meio
            else:
                if x < lista[meio]:
                    ultimo = meio - 1
                else:
                    primeiro = meio + 1

        depois = time.time()
        print ("Tempo", depois - antes)
        return -1
                 

