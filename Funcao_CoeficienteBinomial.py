####resolver a formula de coeficiente binomial utilizando funções####

def fatorial(x):
    x2 = 1       
    while x > 1:
       x2 = x2 * x
       x = x - 1
    return x2

n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de K: "))

resultado = fatorial(n) / (fatorial(k) * fatorial(n-k))

print("o resultado é ",resultado)
