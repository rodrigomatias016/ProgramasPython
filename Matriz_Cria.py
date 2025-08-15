

def cria_matriz(num_linhas, num_colunas, valor):
    ''' (int, int, valor) -> matriz (lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas
    colunas em que cada elemento é igual ao valor dado.
    '''
    matriz = [] # lista vazia
    for i in range(num_linhas):
        # cria a linha i
        linha = [] # lista vazia
        for j in range(num_colunas):
            linha.append(valor)    

        # adiciona linha à matriz
        matriz.append(linha)

    #for linha in matriz:
    #    print(" ".join(map(str, linha))) 
    # Exemplo de saída
    # 4 4 4
    # 4 4 4
    # 4 4 4

    for linha in matriz:
        print(linha)   
    # Exemplo de saída    
    # [4, 4, 4]
    # [4, 4, 4]
    # [4, 4, 4]

   

    
     