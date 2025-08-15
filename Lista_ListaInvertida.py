####Programa que leia uma sequência de números inteiros####
####e quando o usuário digita 0 ele mostra a sequencia na ordem inversa####

x = int(input("Digite uma sequencia de números: "))
lista = []

while x != 0:
    lista.append(x)
    x = int(input("Digite uma sequencia de números: "))
print("Sequência digitada é", lista, end=", ")
print()

len = len(lista)
n = -1

print("Sequência invertida é")
while len > 0:
    print (lista[n], end=", ")
    len = len - 1
    n = n - 1

