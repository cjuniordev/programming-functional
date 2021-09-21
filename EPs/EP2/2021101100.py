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
    """
    Limpa o terminal baseado em seu SO
    """
    if name == 'nt': 
        system('cls') 
    else: 
        system('clear') 

def quemInicia():
    """
    Retorna um número inteiro pseudo aleatório entre 0 e 1 para decidir quem vai começar jogando
    """
    return random.randint(0, 1)

def escolheSimbolo():
    """
    Recebe um simbolo(X, O) escolhido pelo usuário, define o simbolo oposto para o computador e retorna os simbolos
    """
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
    """
    Recebe o tabuleiro e uma jogada e verifica se está disponível retornando True ou False
    """
    if tabuleiro[jogada] == ' ':
        return True
    else:
        return False

def alteraTabuleiro(tabuleiro, jogada, simbolo):
    """
    Função responsável por alterar o tabuleiro
    """
    tabuleiroAuxiliar = tabuleiro[:]
    tabuleiroAuxiliar[jogada] = simbolo
    return tabuleiroAuxiliar

def jogadaHumano(tabuleiro, simboloHumano):
    """
    Função responsável por gerenciar a jogada do Humano
    Recebe a jogada, verifica se esta válida e a retorna
    """
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
    """
    Imprime o tabuleiro formatado no terminal
    """
    print(f'{tabuleiro[7]} | {tabuleiro[8]} | {tabuleiro[9]}')
    print('--+---+--')
    print(f'{tabuleiro[4]} | {tabuleiro[5]} | {tabuleiro[6]}')
    print('--+---+--')
    print(f'{tabuleiro[1]} | {tabuleiro[2]} | {tabuleiro[3]}')

def tabuleiroVazio(tabuleiro, i=0):
    """
    Verifica se o tabuleiro está vazio e retorna True ou False
    """
    if i < len(tabuleiro):
        if tabuleiro[i] == ' ':
            return tabuleiroVazio(tabuleiro, i+1)
        else:
            return False
    else:
        return True

def vitoria(tabuleiro, simbolo):
    """
    Funcção responsável por verificar se houve vitória
    Verifica todas possibilidades de vencer
        --> Horizontais: 123, 456, 789
        --> Verticais: 147, 258, 369
        --> Diagonais: 357, 159
    Retorna True se tiver vitória e false, caso contrário
    """
    
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
    """
    Verifica se houve empate
    Se não houve vitória e todas as casas estão ocupadas, então houve um empate
    Retorna True se tiver Empate e false, caso contrário
    """
    if vitoria:
        return False
    else:
        auxTabuleiro = tabuleiro[1:]
        if ' ' not in auxTabuleiro:
            return True
        else:
            return False

def fimDeJogo(resultado, simboloHumano, simboloComputador):
    """
    Imprime mensagem de fim de jogo ao usuário, mostrando o resultado da partida
    """
    if resultado == simboloHumano:
        print('\n--> Humano venceu!\n')
    elif resultado == simboloComputador:
        print('\n--> Computador venceu!\n')
    else:
        print('\n--> Empatou!\n')

    _ = input('Pressione enter para continuar.')

def pegaJogadasDisponiveis(tabuleiro, J=[], i=1):
    """
    Recebe o tabuleiro e retorna todas casas disponíveis para jogar
    """
    if i < len(tabuleiro):
        if tabuleiro[i] == ' ':
            return pegaJogadasDisponiveis(tabuleiro, J+[i], i+1)
        else:
            return pegaJogadasDisponiveis(tabuleiro, J, i+1)
    else:
        return J

def jogadasPreferenciais(posicoesDisponiveis, posicoesDesejaveis, J=[], i=0):
    """
    Função recursiva que recebe as posições disponíveis na tabuleiro e as desejaveis e retorna as posições desejáveis que estão disponíveis
    """
    if i < len(posicoesDisponiveis):
        if posicoesDisponiveis[i] in posicoesDesejaveis:
            return jogadasPreferenciais(posicoesDisponiveis, posicoesDesejaveis, J+[posicoesDisponiveis[i]], i+1)
        else:
            return jogadasPreferenciais(posicoesDisponiveis, posicoesDesejaveis, J, i+1)
    else:
        return J

def verificaPossivelVitoria(tabuleiro, posicoesDisponiveis, simbolo, copiaTabuleiro=[], i=0):
    """
    Verifica se é possível vencer em um único lance.
    Essa função faz uma cópia do tabuleiro, simula todos os lances possíveis e verifica se alguma gera vitória
    """
    if i == 0:
        return verificaPossivelVitoria(tabuleiro, posicoesDisponiveis, simbolo, tabuleiro[:], i+1)
    elif i <= len(posicoesDisponiveis):
        jogada = posicoesDisponiveis[i-1]
        copiaTabuleiro[jogada] = simbolo
        if vitoria(copiaTabuleiro, simbolo):
            return jogada
        else:
            return verificaPossivelVitoria(tabuleiro, posicoesDisponiveis, simbolo, tabuleiro[:], i+1)
    else:
        return None

def verificaPossivelDerrota(tabuleiro, posicoesDisponiveis, simbolo, copiaTabuleiro=[], i=0):
    """
    Verifica se é possível perder em um único lance.
    Essa função faz uma cópia do tabuleiro, simula todos os lances possíveis e verifica se alguma gera derrota
    """
    if i == 0:
        simbolo = 'X' if simbolo == 'O' else 'O'
        return verificaPossivelDerrota(tabuleiro, posicoesDisponiveis, simbolo, tabuleiro[:], i+1)
    elif i <= len(posicoesDisponiveis):
        jogada = posicoesDisponiveis[i-1]
        copiaTabuleiro[jogada] = simbolo
        if vitoria(copiaTabuleiro, simbolo):
            return jogada
        else:
            return verificaPossivelDerrota(tabuleiro, posicoesDisponiveis, simbolo, tabuleiro[:], i+1)
    else:
        return None

def jogaDiagonalOposta(tabuleiro, simbolo):
    """
    Essa função busca jogar sempre a ponta oposta do simbolo
    """
    if tabuleiro[1] == simbolo and tabuleiro[9] == ' ':
        return 9
    elif tabuleiro[9] == simbolo and tabuleiro[1] == ' ':
        return 1
    elif tabuleiro[3] == simbolo and tabuleiro[7] == ' ':
        return 7
    elif tabuleiro[7] == simbolo and tabuleiro[3] == ' ':
        return 3
    else:
        return None

def quantosLances(tabuleiro, lances=0, i=0):
    """
    Verifica e retorna quantos lances foram jogados na partida
    """
    if i < len(tabuleiro):
        if tabuleiro[i] != ' ':
            return quantosLances(tabuleiro, lances+1, i+1)
        else:
            return quantosLances(tabuleiro, lances, i+1)
    else:
        return lances

def jogouPonta(tabuleiro, jogou=False, pontas=[1, 3, 7, 9], i=0):
    """
    Verifica se alguem jogou nas pontas
    """
    if i < len(tabuleiro):
        if tabuleiro[i] != ' ':
            if i in pontas:
                return jogouPonta(tabuleiro, True, pontas, i+1)
            else:
                return jogouPonta(tabuleiro, jogou, pontas, i+1)
        else:
            return jogouPonta(tabuleiro, jogou, pontas, i+1)
    else:
        return jogou

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
    posicoesDesejaveis = [1, 3, 7, 9]
    centro = [5]
    laterais = [2, 4, 6, 8]
    if tabuleiroVazio(tabuleiro):
        return random.choice(posicoesDesejaveis)

    if quantosLances(tabuleiro) == 1 and jogouPonta(tabuleiro):
        return random.choice(laterais)
    
    # pega jogadas disponiveis e as para jogar
    disponiveis = pegaJogadasDisponiveis(tabuleiro)

    vitoriaEmUm = verificaPossivelVitoria(tabuleiro, disponiveis, simboloComputador)
    derrotaEmUm = verificaPossivelDerrota(tabuleiro, disponiveis, simboloComputador)
    if vitoriaEmUm != None:
        return vitoriaEmUm
    elif derrotaEmUm != None:
        return derrotaEmUm
    else:
        preferencias = jogadasPreferenciais(disponiveis, posicoesDesejaveis)

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
    """
    Verifica se alguém venceu ou empatou usando as funções 'empate' e 'vitoria'
    """
    venceu = vitoria(tabuleiro, simbolo)
    if venceu:
        return simbolo
    elif empate(tabuleiro, venceu):
        return ' '

def jogo(tabuleiro, simboloHumano, simboloComputador, primeiroJogador, i=0):
    """
    Função responsável por controlar todo os sistema de alternancia dos jogadores indicado no fluxograma
    """
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
    """
    Verifica se o jogador deseja continuar
    """
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
    """
    Função raiz de todo o código, inicia variáveis e chama as funções necessárias para se iniciar a partida
    """
    #Você pode, se quiser, comentar os dois prints abaixo:
    #print(getNome())   
    #print(getMatricula())

    limpaTela()
    tabuleiro = [' ']*10

    simboloHumano, simboloComputador = escolheSimbolo()
    primeiroJogador = quemInicia()

    resultado = jogo(tabuleiro, simboloHumano, simboloComputador, primeiroJogador)
    fimDeJogo(resultado, simboloHumano, simboloComputador)
    if desejaContinuar():
        main()
    else:
        limpaTela()
        print('Obrigado por jogar!')

## NÃO ALTERE O CÓDIGO ABAIXO ##
if __name__ == "__main__":
    main()

## a fazer
### buscar terceira diagonal