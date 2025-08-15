#Escrever uma função que recebe uma lista de String contendo nomes pessoas como parâmetro
#E devolve o nome mais curto. A função deve ignorar espaços antes e depois do nome e deve
#Devolver o nome "capitalizado", ou seja, apenas com a 1a letra maiúscula.

#Exemplo
#lista_de_nomes = ["  ana    ","josé" ,"Arquibaldo",   "Alouhis"]
#mais_curto(lista_de_nomes)

def mais_curto(lista_de_nomes):
    A = 0
    for nome in lista_de_nomes:
        if A < 1:
              name1 = nome.strip().capitalize()
              tamanho1 = len(name1)
              A = 1
        else:      
            name2 = nome.strip().capitalize()
            tamanho2 = len(name2)   
            if tamanho1 < tamanho2:
               resultado = name1
               menor = tamanho1
            else:
               resultado = name2
               menor = tamanho2
            name1 = resultado
            tamanho1 = menor       
    return resultado        
             


def teste_mais_curto():
    lista_de_nomes = ["  ana    ","josé" ,"Arquibaldo",   "Alouhis"]
    resultado = mais_curto(lista_de_nomes)
    if resultado == "Ana":
        print("Teste 1 funcionou")
    else:
        False    
        print("Teste 1 falhou")

    lista_de_nomes = ["  ana    ","josé" ,"   Jó    ", "Arquibaldo",   "Alouhis"]
    resultado = mais_curto(lista_de_nomes)
    if resultado == "Jó":
        print("Teste 2 funcionou")
    else:
        False      
        print("Teste 2 falhou")

    lista_de_nomes = ["  pedro    ","josé" ,"   Antonio    ", "Arquibaldo",   "Alouhis"]
    resultado = mais_curto(lista_de_nomes)
    if resultado == "José":
        print("Teste 3 funcionou")
    else:
        False      
        print("Teste 3 falhou")    

    lista_de_nomes = ["   Antoni    ", "Arquibaldo",   "Alouhis", "Madalena     "]
    resultado = mais_curto(lista_de_nomes)
    if resultado == "Antoni":
        print("Teste 4 funcionou")
    else:
        False      
        print("Teste 4 falhou")     
    
                

        
        







