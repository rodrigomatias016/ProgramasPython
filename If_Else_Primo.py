####Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo.####
####Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".####

n = int(input("Digite um número inteiro positivo: "))

if (n % 2 == 0 and n != 2) or n == 1 or (n % 5 == 0 and n !=5) or (n % 11 == 0 and n != 11):
    print("não primo")
else:
    print("primo")