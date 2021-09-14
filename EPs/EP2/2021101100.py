import random
from os import X_OK, system, name 

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
    ## verificar depois se aceita chars minúsculos
    simboloHumano = input('Escolha um simbolo para jogar(X ou O): ')
    if simboloHumano == 'X':
        simboloComputador = 'O'
        return simboloHumano, simboloComputador
    elif simboloHumano == 'O':
        simboloComputador = 'X'
        return simboloHumano, simboloComputador
    else:
        print('Digite um símbolo válido!')
        _ = input('Pressione enter para continuar.')
        return escolheSimbolo()


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
    return


def jogadaHumano(tabuleiro, simboloHumano):
    jogada = int(input('Digite uma posição: [1-9] '))
    if jogada < 1 or jogada > 9:
        _ = input('Valor inválido, pressione enter para tentar novamente.')
        return jogadaHumano(tabuleiro, simboloHumano)
    else:
        ## verificar se o espaço está disponível
        if tabuleiro[jogada] == ' ':
            tabuleiro[jogada] = simboloHumano
            return tabuleiro
        else:
            _ = input('Essa opção está ocupada, pressione enter para tentar novamente.')
            return jogadaHumano(tabuleiro, simboloHumano)

def imprimeTabuleiro(tabuleiro):
    print(f'{tabuleiro[7]} | {tabuleiro[8]} | {tabuleiro[9]}')
    print('--+---+--')
    print(f'{tabuleiro[4]} | {tabuleiro[5]} | {tabuleiro[6]}')
    print('--+---+--')
    print(f'{tabuleiro[1]} | {tabuleiro[2]} | {tabuleiro[3]}')

def vitória(tabuleiro, simbolo):
    ## horizontais: 123, 456, 789
    ## verticais: 147, 258, 369
    ## diagonais: 357, 159
    if tabuleiro[1] == tabuleiro[2] == tabuleiro[3] == simbolo:
        return True, simbolo
    elif tabuleiro[4] == tabuleiro[5] == tabuleiro[6] == simbolo:
        return True, simbolo
    elif tabuleiro[7] == tabuleiro[8] == tabuleiro[9] == simbolo:
        return True, simbolo
    elif tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == simbolo:
        return True, simbolo
    elif tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == simbolo:
        return True, simbolo
    elif tabuleiro[3] == tabuleiro[6] == tabuleiro[9] == simbolo:
        return True, simbolo
    elif tabuleiro[3] == tabuleiro[5] == tabuleiro[7] == simbolo:
        return True, simbolo
    elif tabuleiro[1] == tabuleiro[5] == tabuleiro[9] == simbolo:
        return True, simbolo
    else:
        return False, simbolo

def main():
    #Você pode, se quiser, comentar os dois prints abaixo:
    #print(getNome())
    #print(getMatricula())

    tabuleiro = [' ']*10
    limpaTela()

    simboloHumano, simboloComputador = escolheSimbolo()
    primeiroJogador = quemInicia()

    tabuleiro = jogadaHumano(tabuleiro, simboloHumano)
    imprimeTabuleiro(tabuleiro)
    #if primeiroJogador == 0:
    #    jogadaHumano(tabuleiro, simboloHumano)
    #else:
    #    jogadaComputador(tabuleiro, simboloComputador)


## NÃO ALTERE O CÓDIGO ABAIXO ##
if __name__ == "__main__":
    main()

## tabuleiro
## 7, 8, 9
## 4, 5, 6
## 1, 2, 3

## estratégia