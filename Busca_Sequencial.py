####Busca sequencial


def busca(seq, x):
    ####(list, float) -> bool
    for i in range(len(seq)):
        if seq[i] == x:
            return i
    return False


####Exemplo seq = [1, 2, 3, 4, 5, 6]

