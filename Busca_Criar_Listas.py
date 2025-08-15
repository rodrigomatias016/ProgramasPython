####Criar um módulo com 3 funções que criam aleatoriamente
####listas de números inteiros em sequências também aleatórias


import random

def cria_lista(n):
    L1 = []
    for i in range(n):
        L1.append(i)
    return L1    
     

def cria_lista1(n):
    L1 = []
    for i in range(n):
        r = random.randint(1, 1000)
        L1.append(r) 
    return L1    

#####Poderia ser
#####def cria_lista(n):
#####    lista = [random.randrange(1000) for x in range(n)]
#####    return lista

def cria_lista2():
    L2 = []
    for i in range(2000):
        r = random.randint(1, 2000)
        L2.append(r) 
    return L2 
    

def cria_lista3():
    L3 = []
    for i in range(3000):
        r = random.randint(1, 3000)
        L3.append(r) 
    return L3     
