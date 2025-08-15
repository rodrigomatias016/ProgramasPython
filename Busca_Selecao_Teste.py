####Criar um teste que verifica se uma lista está em uma sequência crescente


def ordenada(lista):
    primeiro = 0
    for i in lista:
       if primeiro == 0:
           elemento1 = i
           primeiro = 1
       else:   
           elemento2 = i
           if elemento2 < elemento1:
               return False
           elemento1 = elemento2       
    return True


          
       
       
