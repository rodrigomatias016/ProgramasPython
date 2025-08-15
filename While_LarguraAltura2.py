####Refaça o exercício 1 imprimindo os retângulos sem preenchimento####
####de forma que os caracteres que não estiverem na borda do retângulo sejam espaços###

####Imprimir tudo só na primeira e na última linha####
####Solução: criei o primeiro if na altura para imprimir o # em todas as linhas no começo####
####E no fim da contagem e no else eu coloquei um if para imprimir somente o primeiro e último####
####Item na contagem da largura####

l = int(input("Digite a largura: "))
a = int(input("Digite a altura: "))

x = 0
while a > x:
    y = 0
    if x == 0 or a == x+1:
        while l > y:
            print("#", end="")
            y = y + 1
    else:
        while l > y:
            if y == 0 or l == y+1:
                print("#", end="")
            else:
                print(end=" ")
            y = y + 1
    x = x + 1
    print("")   