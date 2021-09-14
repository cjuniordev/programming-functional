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
    ...

def main():
    #Você pode, se quiser, comentar os dois prints abaixo:
    #print(getNome())
    #print(getMatricula())

    tabuleiro = ['']*10
    limpaTela()

    primeiroJogador = quemInicia()
    simboloHumano, simboloComputador = escolheSimbolo()

    if primeiroJogador == 0:
        jogadaHumano(tabuleiro, simboloHumano)
    else:
        jogadaComputador(tabuleiro, simboloComputador)


## NÃO ALTERE O CÓDIGO ABAIXO ##
if __name__ == "__main__":
    main()

## tabuleiro
## 7, 8, 9
## 4, 5, 6
## 1, 2, 3

## estratégia