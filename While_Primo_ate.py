####Imprimir todos os primos até um determinado número digitado pelo usuário####



n = int(input("Digite um número inteiro positivo: "))
c = 1

while  c <= n:  
    p = 0
    i = 1
    while i <= c:
        if c % i == 0:
            p = p + 1
        i = i + 1
    if p == 2:
        print(c)        
    c = c + 1


         




