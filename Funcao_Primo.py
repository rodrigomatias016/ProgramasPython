####Função dividindo um determinado número até a metade de um número####
####Se encontrar um divisor além de um e do próprio número, ele não é primo####
####Do contrário é primo###


def éPrimo (x):
    fator = 2
    if x == 2:
        return True
    while x % fator != 0 and fator <= x/2:
        fator = fator + 1
        print(fator)
    if x % fator == 0:
        return False
    else:
        return True   

n = int(input("Digite um número inteiro: "))

while n > 0:
    if éPrimo(n):
        print(n, "é primo!")
    else:
        print(n, "não é primo :-(")
    n = int(input("Digite um número inteiro: "))

 

        
