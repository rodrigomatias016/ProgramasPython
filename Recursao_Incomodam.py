####Implemente a função incomodam(n) que devolve uma string contendo "incomodam " (a palavra seguida de um espaço) n vezes.
#### Se n não for um inteiro estritamente positivo, a função deve devolver uma string vazia. Essa função deve ser implementada utilizando recursão.
####Utilizando a função acima, implemente a função elefantes(n) que devolve uma string contendo a letra da música "Um elefante incomoda muita gente" de 1 até n elefantes. 
#### Se n não for maior que 1, a função deve devolver uma string vazia. Essa função também deve ser implementada utilizando recursão.
#### Observe que, para um elefante, você deve escrever por extenso e no singular ("Um elefante..."); para os demais, utilize números e o plural ("2 elefantes...").


def incomodam(n):
    # Retorna uma string vazia se n não for um inteiro positivo.
    if not isinstance(n, int) or n <= 0:
        return ""
    # Caso base da recursão: para n=1, ou quando n chega a 1 após subtrações.
    # A recursão 'incomodam (n-1)' eventualmente chamará 'incomodam(0)', que retornará "".
    return "incomodam " + incomodam(n - 1)

def elefantes(n):
    # Retorna uma string vazia se n não for um inteiro maior que 1.
    if not isinstance(n, int) or n <= 1:
        return ""
    # Caso base específico: define o trecho para 2 elefantes.
    # É o ponto onde a música começa a se expandir com a repetição.
    elif n == 2:
        return "Um elefante incomoda muita gente\n2 elefantes " + incomodam(2) + "muito mais\n"
    # Passo recursivo: constrói a letra para n elefantes.
    else:
        # A recursão se baseia na letra para (n-1) elefantes.
        parte_anterior = elefantes(n - 1)
        # Adiciona a linha sobre (n-1) elefantes incomodando "muita gente".
        linha_incomoda = f"{n-1} elefantes incomodam muita gente\n"
        # Adiciona a linha sobre 'n' elefantes incomodando "muito mais".
        linha_mais = f"{n} elefantes " + incomodam(n) + "muito mais\n"
        
        # Concatena as partes para formar o segmento da música para este 'n'.
        return parte_anterior + linha_incomoda + linha_mais
