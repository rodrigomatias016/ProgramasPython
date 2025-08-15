####Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros#### 
####verifica se tal lista possui elementos repetidos e os remove####
####A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos####



def remove_repetidos(x):
    x.sort()
    removida = []
    ref = -1
    for i in x:
        if x == x[0]: 
            removida.append(i)
        else:
            if i != x[ref]:
                removida.append(i)

        ref = ref + 1      

    return removida  


