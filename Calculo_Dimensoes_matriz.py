####Escreva uma função dimensoes(matriz) que recebe uma matriz####
####como parâmetro e imprime as dimensões da matriz recebida, no formato iXj.####


def dimensoes(minha_matriz):
    linhas = 0
    colunas = 0
    for i in minha_matriz:
        lin = i
        linhas = linhas + 1
    for j in lin:
        colunas = colunas + 1
        
    print(linhas,"X",colunas,sep='')


 

             
    