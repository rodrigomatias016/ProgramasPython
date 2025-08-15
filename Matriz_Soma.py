####Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve uma matriz####
####que represente sua soma caso as matrizes tenham dimensões iguais.####
####Caso contrário, a função deve devolver False.####


def soma_matrizes(m1, m2):
    resultado = []
    
    linhas1 = 0
    colunas1 = 0
    for i in m1:
        lin = i
        linhas1 = linhas1 + 1
    for j in lin:
        colunas1 = colunas1 + 1

    linhas2 = 0
    colunas2 = 0
    for n in m2:
        lin = n
        linhas2 = linhas2 + 1
    for m in lin:
        colunas2 = colunas2 + 1    


    if linhas1 == linhas2 and colunas1 == colunas2:
        for x in range(linhas1):
            linha = [0]*colunas1
            resultado.append(linha)
            for y in range(colunas1):
                resultado[x][y] = m1[x][y] + m2[x][y]

        return resultado
    else:
        return False