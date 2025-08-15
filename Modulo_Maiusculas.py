#Escreva a função maiusculas(frase) que recebe uma frase (uma string) 
#Como parâmetro e devolve uma string com as letras maiúsculas 
#Que existem nesta frase, na ordem em que elas aparecem.

def maiusculas(frase):
    resultado = ""
    for letra in frase:
        if ord(letra) >= 65 and ord(letra) <= 90:
            resultado = resultado + letra

    return resultado        
           

