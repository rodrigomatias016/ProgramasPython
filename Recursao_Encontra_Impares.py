####Implemente a função encontra_impares(lista), que recebe como parâmetro uma lista de números inteiros 
####e devolve uma outra lista apenas com os números ímpares da lista dada.

####Essa função deve ser recursiva e utilizar do método extend()


def encontra_impares(lista):
    """
    Recebe uma lista de números inteiros e devolve uma nova lista
    contendo apenas os números ímpares, utilizando recursão.
    """
    impares_encontrados = []

    if not lista:
        return impares_encontrados
    else:
        primeiro_elemento = lista[0]
        restante_da_lista = lista[1:]

        if primeiro_elemento % 2 != 0:
            impares_encontrados.append(primeiro_elemento)

        impares_encontrados.extend(encontra_impares(restante_da_lista))

        return impares_encontrados