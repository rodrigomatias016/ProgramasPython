####Ordenar uma lista utilizando uma método de seleção direta e também do tipo bolha, nesta caso uma bolha mais curta
####Consiste em ordenar uma lista que já está quase ordenada



class Ordenador:
    def selecao_direta (self, lista):

        fim = len(lista)

        for i in range(fim - 1):
            # Inicialmente, o menor elemento já visto é o i-ésimo
            posicao_do_minimo = i

            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j


            # Coloca o menor elemento encontrado no início da sub-lista
            # Para isso, troca de lugar os elementos nas posições i e posicao_do_minimo
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
            

        ####print(lista)


    def bolha(self, lista):
        fim = len(lista)

        for i in range(fim-1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

    def bolha_curta(self, lista):
        fim = len(lista)

        for i in range(fim-1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]     
                    trocou = True
            if not trocou:
                return       

    def insercao_direta(self, lista):
    ###Ordena uma lista usando o algoritmo de Inserção Direta.

        n = len(lista)  # Obtém o tamanho da lista

        # Percorre a lista a partir do segundo elemento (índice 1)
        # O elemento lista[0] é considerado a sublista ordenada inicial
        for i in range(1, n):
            chave = lista[i]  # Elemento atual a ser inserido na posição correta
            j = i - 1         # Índice do último elemento na sublista ordenada

            # Move os elementos da sublista ordenada (lista[0...i-1]) que são
            # maiores que a chave para uma posição à frente de sua posição atual
            while j >= 0 and chave < lista[j]:
                lista[j + 1] = lista[j]
                j -= 1

            # Insere a chave na sua posição correta
            lista[j + 1] = chave
        return lista                    