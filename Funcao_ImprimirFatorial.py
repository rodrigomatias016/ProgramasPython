####Solicitar ao usuaria que digite um número e imprimir fatorial desse número####
####Finaliza com número negativo####

def fatorial(x):
    x2 = 1       
    while x > 1:
       x2 = x2 * x
       x = x - 1
    return (x2)

x = int(input("Digite um número positivo: "))
while x >= 0:
    x2 = fatorial(x)
    print(x2)
    x = int(input("Digite um número positivo: "))
print("****Fim do cálculo****")    
