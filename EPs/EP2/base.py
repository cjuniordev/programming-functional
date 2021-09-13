import random
from os import system, name 

def getMatricula():
    """
    Retorna a matricula do aluno como string
    """
    return "SUA MATRICULA" 

def getNome():
    """
    Retorna o nome completo do aluno
    """
    return "SEU NOME COMPLETO" 

def limpaTela(): 
	if name == 'nt': 
		system('cls') 
	else: 
		system('clear') 

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

def main():
    limpaTela()
    #Você pode, se quiser, comentar os dois prints abaixo:
    print(getNome())
    print(getMatricula())


## NÃO ALTERE O CÓDIGO ABAIXO ##
if __name__ == "__main__":
    main()