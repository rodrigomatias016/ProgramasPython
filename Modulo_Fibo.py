#Funcões que retornam na tela a sequência de Fibonati
#Essa sequência é determinada pela soma do número
#Presente com o número anterior em uma determinada 
#Sequência de números


def fib(n):  #write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()    

def fib2(n):  #return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

print(__name__)




