####Calcular através de um loop se um número é primo ou não####
####O loop irá fazer as divisões do número por todos os números abaixo dele####
####Se tiver mais de dois divisores não é primo####

n = 1
while n != 0:
    n = int(input("Digite um número inteiro positivo: "))
    i = 1
    p = 0
    while i <= n:
        if n % i == 0:
            p = p + 1
        i = i + 1
    if p == 2:
        print("É um número primo!!")
    else:
        print("Não é um número primo!!")
            