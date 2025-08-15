#Para fazer multiplicação de matriz tem que levar em conta que o número de colunas
#Da primeira matriz deve ser igual a número de linhas da segunda matriz.
#Exemplo 2x3 - 3x2.
#Multiplicação deve ser feita pelo primeiro elemento 1x1 pelo 1x1, depois 1x2 por 2x1
#Assim por diante.
#A soma de uma matriz 2x3 com 3x2 terá como resultado uma matriz 2x2


import Matriz_Cria2

def multi_matrizes(A, B):
    num_lin = len(A)
    print(num_lin)
    num_col = len(B[0])
    
    assert len(A[0]) == len(B)
    
    C = Matriz_Cria2.cria_matriz(num_lin, num_col, 0)
    print(num_col)
    print(C)
    
    colA = len(A[0])
    print(colA)
    soma = 0

    for lin in range(num_lin): # Percorre as linhas da matriz
        print(lin)
        for col in range(num_col): # Percorre as colunas da matriz
            print(col)
            for mult in range(colA):
                soma = soma + (A[lin][mult] * B[mult][col])
                print("Soma ", soma)
            C[lin][col] = soma
            soma = 0
            print(C[lin][col])
  
    return C

if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[10, 20], [40, 50], [70, 80]]
    print(multi_matrizes(A, B)) 
    
    C = [[1 ,2], [3, -1]]
    D = [[1, -2, 3], [2, 4, 0]]
    print(multi_matrizes(C, D))    

    #C[1][1] = A11 * B11 + A12 * B21
    #C[1][2] = A11 * B12 + A12 * B22
    #C[1][3] = A11 * B13 + A12 * B23

    #C[2][1] = A21 * B11 + A22 * B21
    #C[2][2] = A21 * B12 + A22 * B22
    #C[2][3] = A21 * B13 + A22 * B23
