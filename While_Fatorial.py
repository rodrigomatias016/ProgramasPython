####Escreva um programa que receba um número natural n na entrada e imprima n! (fatorial) na saída.####


n = int(input("Digite um número natural: "))

n2 = 1

while n > 0:
    n2 = n2 * n
    n = n - 1

print(n2)    


