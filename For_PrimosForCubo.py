####A partir de uma lista de primos, modificar cada elemento para o seu valor ao cubo####

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

for i in range(len(primos)):
    primos[i] = primos[i]**3

for x in primos:
    print (x)    