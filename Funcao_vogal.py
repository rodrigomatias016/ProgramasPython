####Escreva a função vogal que recebe um único caractere como parâmetro####
####e devolve True se ele for uma vogal e False se for uma consoante.####
####Os valores True e False devolvidos devem ser do tipo bool (booleanos), e não strings####

def vogal(x):
    if x == "a" or x == "A" or x == "e" or x == "E" or x == "i" or x == "I" or x == "o" or x == "O" or x == "u" or x == "U":
        return True
    else:
        return False    
