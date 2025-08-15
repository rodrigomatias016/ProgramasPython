import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    soma = 0
    resultado = 0
    
    diferenca = [abs((as_a[0]-as_b[0])),abs((as_a[1]-as_b[1])),abs((as_a[2]-as_b[2])),abs((as_a[3]-as_b[3])),abs((as_a[4]-as_b[4])),abs((as_a[5]-as_b[5]))]     
    
    for s in diferenca:
        soma += s
    resultado = soma/6

    return resultado

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    n_sentenca = 0
    n_frase = 0
    n_palavras = 0
    n_caracteres = 0
    caracteres_sentenca = 0
    caracteres_frase = 0
    lista_palavras = []
    for sentenca in separa_sentencas(texto):
        caracteres_sentenca = caracteres_sentenca + len(sentenca)
        n_sentenca = n_sentenca + 1
        for frase in separa_frases(sentenca):
            caracteres_frase = caracteres_frase + len(frase)
            n_frase = n_frase + 1
            for palavras in separa_palavras(frase):
                lista_palavras.append(palavras)
                n_palavras = n_palavras + 1
                n_caracteres = n_caracteres + len(palavras)

    tamanho_medio = (n_caracteres/n_palavras)         
    '''Divide o número de caracteres tiranto espaço, ; e . pelo número de palavras'''

    palavras_diferentes = n_palavras_diferentes(lista_palavras)
    relacao_type_token = (palavras_diferentes/(n_palavras))
    '''Divide o número de palavras diferentes de um texto pelo número total de palavras'''

    palavras_unicas = n_palavras_unicas(lista_palavras)
    razao_hapax = (palavras_unicas/(len(lista_palavras)))
    '''Divide o número de palavras únicas de um texto pelo número total de palavras'''

    tamanho_medio_sentenca = (caracteres_sentenca/n_sentenca)
    '''Divide o número de caracteres tiranto espaço, ; e . pelo número de sentenças'''

    complexidade_sentença = (n_frase/n_sentenca)
    '''Divide número total de frases divido pelo número de sentenças.'''

    tamanho_medio_frase = (caracteres_frase/n_frase)
    '''Divide o número de caracteres pelo número de frases'''
    
                
    return [tamanho_medio, relacao_type_token, razao_hapax, tamanho_medio_sentenca, complexidade_sentença, tamanho_medio_frase] 


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    comparacao = []

    for texto in textos:
        as_a = calcula_assinatura(texto)
        comparacao.append(compara_assinatura(as_a,ass_cp))
        min_valor = comparacao.index(min(comparacao)) + 1

    return min_valor

ass_cp = le_assinatura()

textos = le_textos()   

comparacao = avalia_textos(textos,ass_cp)
print ("O autor do texto", comparacao, "está infectado com COH-PIAH")