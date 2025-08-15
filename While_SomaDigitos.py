dígitos = int(input("Digite um número inteiro com mais de 3 dígitos: "))

d = 0
soma = 0

while dígitos > 0:

    d = dígitos % 10
    dígitos = dígitos // 10
    soma = soma + d

print(soma)







