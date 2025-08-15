####Receba um número inteiro positivo na entrada e imprima os ####
####n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.####


n = int(input("Digite um número positivo: "))

n2 = 1

while n > 0:
    print(n2)
    n2 = n2 + 2
    n = n - 1

