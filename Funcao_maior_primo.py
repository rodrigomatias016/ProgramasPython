####Função para determinar o maior primo até um determinado número####

def maior_primo(n):
    c = 1
    r = 0
    while  c <= n:  
        p = 0
        i = 1
        while i <= c:
            if c % i == 0:
                p = p + 1
            i = i + 1
        if p == 2:
            r = c        
        c = c + 1
    return r       



    
