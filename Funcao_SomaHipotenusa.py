####Soma das hipotenusas####

def é_hipotenusa(x):
    i = 1
    while x > i: 
        j = 1
        while x > j:
            if x**2 == (i**2 + j**2):
                return True 
            j = j + 1
        i = i + 1    
    return False        

def soma_hipotenusas(n):
    r = 1
    soma = 0
    while n >= r:
        if é_hipotenusa(r):
            soma = soma + r
        r = r + 1
    return soma
    


    