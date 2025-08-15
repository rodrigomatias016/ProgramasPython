####Escreva um programa que recebe como entradas (utilize a função input)####
####dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente####
####O programa deve imprimir, usando repetições encaixadas (laços aninhados)####
####uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída####

l = int(input("Digite a largura: "))
a = int(input("Digite a altura: "))

x = 0
while a > x:
    x = x + 1
    y = 0
    while l > y:
        print("#", end="")
        y = y + 1
    print()    




