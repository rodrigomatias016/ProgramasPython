####Implemente a função soma_lista(lista), que recebe como parâmetro uma lista de números inteiros
#### e devolve um número inteiro correspondente à soma dos elementos desta lista.


def soma_lista(lista):
    if not lista:
        return 0
    # Opcional: if len(lista) == 1: return lista[0]
    else:
        return lista[0] + soma_lista(lista[1:])