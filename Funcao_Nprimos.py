####Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2####
####como parâmetro e devolve a quantidade de números primos####
####que existem entre 2 e n (incluindo 2 e, se for o caso, n).####

def n_primos (n):
    c = 1
    resultado = 0
    while  c <= n:  
        p = 0
        i = 1
        while i <= c:
            if c % i == 0:
                p = p + 1
            i = i + 1
        if p == 2:
            resultado = resultado + 1       
        c = c + 1
    return resultado    
