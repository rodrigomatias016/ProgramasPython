#Função menor_nome(nomes) que recebe uma lista de strings com nome de pessoas 
#Como parâmetro e devolve o nome mais curto presente na lista.
#A função deve ignorar espaços antes e 
#Depois do nome e deve devolver o menor nome presente na lista
#Este nome deve ser devolvido com a primeira letra maiúscula 
#E seus demais caracteres minúsculos


#Exemplo
#lista_de_nomes = ["  ana    ","josé" ,"Arquibaldo",   "Alouhis"]
#mais_curto(lista_de_nomes)

def menor_nome(lista_de_nomes):
    A = 0
    for nome in lista_de_nomes:
        if A < 1:
              name1 = nome.strip().capitalize()
              tamanho1 = len(name1)
              A = 1
        else:      
            name2 = nome.strip().capitalize()
            tamanho2 = len(name2)   
            if tamanho1 <= tamanho2:
               resultado = name1
               menor = tamanho1
            else:
               resultado = name2
               menor = tamanho2
            name1 = resultado
            tamanho1 = menor       
    return resultado    