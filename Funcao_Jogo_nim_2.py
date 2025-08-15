####Jogo do NIM####

def main():
     print("Bem-vindo ao jogo do NIM! Escolha:")
     
     print("1 - para jogar uma partida isolada")
     escolha = float(input("2 - para jogar um campeonato: "))
     if escolha == 1:
        print("Voce escolheu uma partida!")
        partida()
     else:
        print("Voce escolheu um campeonato!")
        campeonato()
     

def computador_escolhe_jogada(n,m):
    if n > m:
        if n % (m+1) == 0:    ####if criado para casos onde a estratégia ganhadora não é possível####
            jogada_computador = m
            return jogada_computador
        else:        
            jogada_computador = 1
            while (n - jogada_computador) % (m+1) != 0:
                jogada_computador = jogada_computador + 1
            return jogada_computador   
    else:
        jogada_computador = n
        return jogada_computador
        

def usuario_escolhe_jogada(n,m):
    jogada_usuario = float(input("Quantas peças você vai tirar: "))
    while jogada_usuario > m or jogada_usuario <= 0 or jogada_usuario > n: ####último or criado para casos hipotéticos####
        print("Oops! Jogada inválida! Tente de novo.")  
        jogada_usuario = float(input("Quantas peças você vai tirar: "))  
    return jogada_usuario        
        

def partida():
    n = float(input("Quantas peças?: "))
    m = float(input("Limite de peças por jogada?: "))
    if n % (m+1) == 0 or m > n:
        print("Você começa")
        while n >= 1:
            jogada_usuario = usuario_escolhe_jogada(n,m)
            n = n - jogada_usuario
            print("Você tirou", jogada_usuario,"peça(s).")
            if n == 0:
                resultado = 1
                print("Fim do jogo! O jogador ganhou!")
            else:    
                print("Agora resta", n,"peça(s).")
                jogada_computador = computador_escolhe_jogada(n,m)
                n = n - jogada_computador
                print("Computador tirou", jogada_computador,"peça(s).")
                if n == 0:
                    resultado = 2
                    print("Fim do jogo! O computador ganhou!")
                else:    
                    print("Agora resta", n,"peça(s).")  
        return resultado                      
    else:
        print("Computador começa")    
        while n >= 1:
            jogada_computador = computador_escolhe_jogada(n,m)
            n = n - jogada_computador
            print("Computador tirou", jogada_computador,"peça(s).")
            if n == 0:
                resultado = 2
                print("Fim do jogo! O computador ganhou!")
            else: 
                print("Agora resta", n,"peça(s).")
                jogada_usuario = usuario_escolhe_jogada(n,m)
                n = n - jogada_usuario
                print("Você tirou", jogada_usuario,"peça(s).")
                if n == 0:
                    resultado = 1
                    print("Fim do jogo! O jogador ganhou!")
                else:  
                    print("Agora resta", n,"peça(s).")
        return resultado                


def campeonato(): ####chama a função partida 3x
    c = 1
    jogador = 0
    computador = 0
    while c <= 3:
        print("**** Rodada", c,"****")
        resultado = partida()
        if resultado == 1:
            jogador = jogador + 1
        else:
            computador = computador + 1 
        c = c + 1
    print("**** Final do campeonato! ****")    
    print("Placar: Você",jogador,"X",computador,"Computador")

main()

 


