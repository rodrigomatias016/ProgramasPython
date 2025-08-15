



def insercao_direta(lista):
    ###Ordena uma lista usando o algoritmo de Inserção Direta.

        n = len(lista)  # Obtém o tamanho da lista
        print("0", n)

        # Percorre a lista a partir do segundo elemento (índice 1)
        # O elemento lista[0] é considerado a sublista ordenada inicial
        for i in range(1, n):
            print("i", i)    
            chave = lista[i]
            print("chave", chave)
            # Elemento atual a ser inserido na posição correta
            j = i - 1
            print("j1", j)
            # Índice do último elemento na sublista ordenada

            # Move os elementos da sublista ordenada (lista[0...i-1]) que são
            # maiores que a chave para uma posição à frente de sua posição atual
            while j >= 0 and chave < lista[j]:
                lista[j + 1] = lista[j]
                print ("p1", lista[j + 1])
                j -= 1
                print ("j2", j)

            # Insere a chave na sua posição correta
            lista[j + 1] = chave
            print ("p2", lista[j +1])
            print (lista)
        return lista  
