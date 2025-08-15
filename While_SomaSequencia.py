
print("Digite uma sequência de valores, terminada quando digitar 0.")
soma = 0

valor = 1
while valor != 0:
    valor = int(input("Digite um valor a ser somado: "))
    soma = soma + valor

print("A soma dos valores digitados é: ", soma)