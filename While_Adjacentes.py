####Sequência que possui 2 números adjacentes iguais####


número = int(input("Digite um número inteiro com mais de 3 dígitos: "))

adjacentes = False
d1 = 0
d2 = 0

while número > 0 and not adjacentes:

    d1 = número % 10
    número = número // 10
    d2 = número % 10
    if d1 == d2:
        adjacentes = True

if adjacentes:
    print("sim")
else:
    print("não")    
    