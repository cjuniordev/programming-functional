import random
from os import system, name 

def getMatricula():
    """
    Retorna a matricula do aluno como string
    """
    return "2021101100" 

def getNome():
    """
    Retorna o nome completo do aluno
    """
    return "CARLOS ROBERTO ROGÉRIO JUNIOR" 

def limpaTela(): 
	if name == 'nt': 
		system('cls') 
	else: 
		system('clear') 

def quemInicia():
    return random.randint(0, 1)

def escolheSimbolo():
    simboloHumano = input('Escolha um simbolo para jogar(X ou O): ')
    simboloComputador = ''
    if simboloHumano in 'Xx':
        simboloHumano = 'X'
        simboloComputador = 'O'
    elif simboloHumano in 'Oo':
        simboloHumano = 'O'
        simboloComputador = 'X'
    else:
        print('Digite um símbolo válido!')
        _ = input('Pressione enter para continuar.')
        return escolheSimbolo()

    return simboloHumano, simboloComputador

def posicaoDisponível(tabuleiro, jogada):
    if tabuleiro[jogada] == ' ':
        return True
    else:
        return False

def alteraTabuleiro(tabuleiro, jogada, simbolo):
    tabuleiroAuxiliar = tabuleiro[:]
    tabuleiroAuxiliar[jogada] = simbolo
    return tabuleiroAuxiliar

def jogadaHumano(tabuleiro, simboloHumano):
    jogada = int(input('Digite uma posição: [1-9] '))
    if jogada < 1 or jogada > 9:
        _ = input('Valor inválido, pressione enter para tentar novamente.')
        return jogadaHumano(tabuleiro, simboloHumano)
    else:
        if posicaoDisponível(tabuleiro, jogada):
            return jogada
        else:
            _ = input('Essa opção está ocupada, pressione enter para tentar novamente.')
            return jogadaHumano(tabuleiro, simboloHumano)

def imprimeTabuleiro(tabuleiro):
    print(f'{tabuleiro[7]} | {tabuleiro[8]} | {tabuleiro[9]}')
    print('--+---+--')
    print(f'{tabuleiro[4]} | {tabuleiro[5]} | {tabuleiro[6]}')
    print('--+---+--')
    print(f'{tabuleiro[1]} | {tabuleiro[2]} | {tabuleiro[3]}')

def tabuleiroVazio(tabuleiro, vazio=True, i=0):
    if i < len(tabuleiro):
        if tabuleiro[i] == ' ':
            return tabuleiroVazio(tabuleiro, vazio, i+1)
        else:
            return False
    else:
        return vazio

def vitoria(tabuleiro, simbolo):
    ## horizontais: 123, 456, 789
    ## verticais: 147, 258, 369
    ## diagonais: 357, 159
    if tabuleiro[1] == tabuleiro[2] == tabuleiro[3] == simbolo:
        return True
    elif tabuleiro[4] == tabuleiro[5] == tabuleiro[6] == simbolo:
        return True
    elif tabuleiro[7] == tabuleiro[8] == tabuleiro[9] == simbolo:
        return True
    elif tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == simbolo:
        return True
    elif tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == simbolo:
        return True
    elif tabuleiro[3] == tabuleiro[6] == tabuleiro[9] == simbolo:
        return True
    elif tabuleiro[3] == tabuleiro[5] == tabuleiro[7] == simbolo:
        return True
    elif tabuleiro[1] == tabuleiro[5] == tabuleiro[9] == simbolo:
        return True
    else:
        return False

def empate(tabuleiro, vitoria):
    if vitoria:
        return False
    else:
        if ' ' not in tabuleiro:
            return True
        else:
            return False

def fimDeJogo(resultado, simboloHumano, simboloComputador):
    if resultado == simboloHumano:
        print('-> Humano venceu!')
    elif resultado == simboloComputador:
        print('--> Computador venceu!')
    else:
        print('--> Empatou!')

    _ = input('Pressione enter para continuar.')

def jogadasPreferenciais(posicoes_disponiveis, posicoes_desejaveis, J=[], i=0):
    if i < len(posicoes_disponiveis):
        if posicoes_disponiveis[i] in posicoes_desejaveis:
            return jogadasPreferenciais(posicoes_disponiveis, posicoes_desejaveis, J+[posicoes_disponiveis[i]], i+1)
        else:
            return jogadasPreferenciais(posicoes_disponiveis, posicoes_desejaveis, J, i+1)
    else:
        return J

def pegaJogadasDisponiveis(tabuleiro, J=[], i=1):
    if i < len(tabuleiro):
        if tabuleiro[i] == ' ':
            return pegaJogadasDisponiveis(tabuleiro, J+[i], i+1)
        else:
            return pegaJogadasDisponiveis(tabuleiro, J, i+1)
    else:
        return J

def verificaPossivelVitoria(tabuleiro, posicoes_disponiveis, simbolo, copiaTabuleiro=[], i=0):
    # fazer recursao q verifica todos espaços vazios, gera copia do tabuleiro, e tenta verificar se alguma gera vitoria
    if i == 0:
        return verificaPossivelVitoria(tabuleiro, posicoes_disponiveis, simbolo, tabuleiro[:], i+1)
    elif i <= len(posicoes_disponiveis):
        jogada = posicoes_disponiveis[i-1]
        copiaTabuleiro[jogada] = simbolo
        if vitoria(copiaTabuleiro, simbolo):
            return jogada
        else:
            return verificaPossivelVitoria(tabuleiro, posicoes_disponiveis, simbolo, tabuleiro[:], i+1)
    else:
        return None

def verificaPossivelDerrota(tabuleiro, posicoes_disponiveis, simbolo, copiaTabuleiro=[], i=0):
    if i == 0:
        simbolo = 'X' if simbolo == 'O' else 'O'
        return verificaPossivelDerrota(tabuleiro, posicoes_disponiveis, simbolo, tabuleiro[:], i+1)
    elif i <= len(posicoes_disponiveis):
        jogada = posicoes_disponiveis[i-1]
        copiaTabuleiro[jogada] = simbolo
        if vitoria(copiaTabuleiro, simbolo):
            return jogada
        else:
            return verificaPossivelDerrota(tabuleiro, posicoes_disponiveis, simbolo, tabuleiro[:], i+1)
    else:
        return None

def jogaDiagonalOposta(tabuleiro, simboloComputador):
    if tabuleiro[1] == simboloComputador and tabuleiro[9] == ' ':
        return 9
    elif tabuleiro[9] == simboloComputador and tabuleiro[1] == ' ':
        return 1
    elif tabuleiro[3] == simboloComputador and tabuleiro[7] == ' ':
        return 7
    elif tabuleiro[7] == simboloComputador and tabuleiro[3] == ' ':
        return 3
    else:
        return None

def jogadaComputador(tabuleiro, simboloComputador):
    """
    Recebe o tabuleiro e o simbolo (X ou O) do computador e determina onde o computador deve jogar
    O tabuleiro pode estar vazio (caso o computador seja o primeiro a jogar) ou com algumas posições preenchidas, 
    sendo a posição 0 do tabuleiro descartada.

    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro
    simboloComputador: letra do computador

    Retorno:
    Posição (entre 1 e 9) da jogada do computador

    Estratégia:
    Explique aqui, de forma resumida, a sua estratégia usada para o computador vencer o jogador
    """
    posicoes_desejaveis = [1, 3, 7, 9]
    centro = [5]
    if tabuleiroVazio(tabuleiro):
        return random.choice(posicoes_desejaveis)
    
    # pega jogadas disponiveis e as para jogar
    disponiveis = pegaJogadasDisponiveis(tabuleiro)

    vitoriaEmUm = verificaPossivelVitoria(tabuleiro, disponiveis, simboloComputador)
    derrotaEmUm = verificaPossivelDerrota(tabuleiro, disponiveis, simboloComputador)
    if vitoriaEmUm != None:
        return vitoriaEmUm
    elif derrotaEmUm != None:
        return derrotaEmUm
    else:
        preferencias = jogadasPreferenciais(disponiveis, posicoes_desejaveis)

        diagonal_oposta = jogaDiagonalOposta(tabuleiro, simboloComputador)
        if diagonal_oposta != None:
            return diagonal_oposta

        if preferencias:
            return random.choice(preferencias)
        else:
            temCentro = jogadasPreferenciais(disponiveis, centro)
            if temCentro:
                return temCentro
            else:
                return random.choice(disponiveis)

def venceuOuEmpatou(tabuleiro, simbolo):
    venceu = vitoria(tabuleiro, simbolo)
    if venceu:
        return simbolo
    elif empate(tabuleiro, venceu):
        return ' '

def jogo(tabuleiro, simboloHumano, simboloComputador, primeiroJogador, i=0):
    if i < 9:
        if primeiroJogador == 0:
            limpaTela()
            imprimeTabuleiro(tabuleiro)
            jogada = jogadaHumano(tabuleiro, simboloHumano)
            tabuleiro = alteraTabuleiro(tabuleiro, jogada, simboloHumano)
            
            vitoria_ou_empate = venceuOuEmpatou(tabuleiro, simboloHumano)
            if vitoria_ou_empate:
                limpaTela()
                imprimeTabuleiro(tabuleiro)
                return vitoria_ou_empate
            else:
                return jogo(tabuleiro, simboloHumano, simboloComputador, 1, i+1), tabuleiro
            
        elif primeiroJogador == 1:
            jogada = jogadaComputador(tabuleiro, simboloComputador)
            tabuleiro = alteraTabuleiro(tabuleiro, jogada, simboloComputador)

            vitoria_ou_empate = venceuOuEmpatou(tabuleiro, simboloComputador)
            if vitoria_ou_empate:
                limpaTela()
                imprimeTabuleiro(tabuleiro)
                return vitoria_ou_empate
            else:
                return jogo(tabuleiro, simboloHumano, simboloComputador, 0, i+1)

def desejaContinuar():
    limpaTela()
    continuar = input('Deseja continuar jogando? (s/n)')
    if continuar in 'Ss':
        return True
    elif continuar in 'Nn':
        return False
    else:
        print('Opção inválida, tente novamente!')
        return desejaContinuar()

def main():
    #Você pode, se quiser, comentar os dois prints abaixo:
    #print(getNome())   
    #print(getMatricula())

    limpaTela()
    tabuleiro = [' ']*10

    simboloHumano, simbolosComputador = escolheSimbolo()
    primeiroJogador = quemInicia()

    resultado = jogo(tabuleiro, simboloHumano, simbolosComputador, primeiroJogador)
    fimDeJogo(resultado, simboloHumano, simbolosComputador)
    if desejaContinuar():
        main()
    else:
        limpaTela()
        print('Obrigado por jogar!')

## NÃO ALTERE O CÓDIGO ABAIXO ##
if __name__ == "__main__":
    main()

## criar estrategia para quando adversario jogar nos cantos