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

def jogadaComputador(tabuleiro, simboloComputador, vazio, posicoes_livres, preferencias):
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
    if vazio:
        jogada = random.choice(posicoes_desejaveis)
        return jogada
    
    jogada = random.choice(preferencias)
    return jogada
    
    

def jogadaHumano(tabuleiro, simboloHumano):
    jogada = int(input('Digite uma posição: [1-9] '))
    if jogada < 1 or jogada > 9:
        _ = input('Valor inválido, pressione enter para tentar novamente.')
        return jogadaHumano(tabuleiro, simboloHumano)
    else:
        ## verificar se o espaço está disponível
        if tabuleiro[jogada] == ' ':
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

def alteraTabuleiro(tabuleiro, jogada, simbolo):
    tabuleiro[jogada] = simbolo
    return tabuleiro

def tabuleiroVazio(tabuleiro, vazio=True, i=0):
    if i < len(tabuleiro):
        if tabuleiro[i] == ' ':
            return tabuleiroVazio(tabuleiro, vazio, i+1)
        else:
            return tabuleiroVazio(tabuleiro, False, i+1)
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

def jogo(tabuleiro, simboloHumano, simboloComputador, vez, i=0):
    if i < 9:
        if vez == 0:
            imprimeTabuleiro(tabuleiro)
            jogada = jogadaHumano(tabuleiro, simboloHumano)
            alteraTabuleiro(tabuleiro, jogada, simboloHumano)
            venceu = vitoria(tabuleiro, simboloHumano)
            empatou = empate(tabuleiro, venceu)
            if venceu:
                return simboloHumano
            elif empatou:
                return ' '
            else:
                return jogo(tabuleiro, simboloHumano, simboloComputador, 1, i+1)
        elif vez == 1:
            jogada = jogadaHumano2(tabuleiro, simboloComputador)
            alteraTabuleiro(tabuleiro, jogada, simboloComputador)
            venceu = vitoria(tabuleiro, simboloComputador)
            empatou = empate(tabuleiro, venceu)
            if venceu:
                return simboloComputador
            elif empatou:
                return ' '
            else:
                return jogo(tabuleiro, simboloHumano, simboloComputador, 0, i+1)
    else:
        return 'erro'

def fimDeJogo(resultado, simboloHumano, simboloComputador):
    if resultado == ' ':
        print('Empatou!')
    elif resultado == simboloHumano:
        print('Humano venceu!')
    elif resultado == simboloComputador:
        print('Computador venceu!')

    _ = input('Pressione enter para continuar.')

def jogadas_preferenciais(posicoes_disponiveis, posicoes_desejaveis = [1, 3, 5, 7, 9], J=[], i=0):
    if i < len(posicoes_disponiveis):
        if posicoes_disponiveis[i] in posicoes_desejaveis:
            return jogadas_preferenciais(posicoes_disponiveis, posicoes_desejaveis, J+[posicoes_disponiveis[i]], i+1)
        else:
            return jogadas_preferenciais(posicoes_disponiveis, posicoes_desejaveis, J, i+1)
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

def verificaPossívelVitoria(tabuleiro, posicoes_disponiveis, simbolo, copiaTabuleiro=[], i=0):
    # fazer recursao q verifica todos espaços vazios, gera copia do tabuleiro, e tenta verificar se alguma gera vitoria
    if i == 0:
        return verificaPossívelVitoria(tabuleiro, posicoes_disponiveis, simbolo, tabuleiro[:], i+1)
    elif i <= len(posicoes_disponiveis):
        jogada = posicoes_disponiveis[i-1]
        copiaTabuleiro[jogada] = simbolo
        if vitoria(copiaTabuleiro, simbolo):
            return jogada
        else:
            return verificaPossívelVitoria(tabuleiro, posicoes_disponiveis, simbolo, tabuleiro[:], i+1)
    else:
        return None

    


def main():
    #Você pode, se quiser, comentar os dois prints abaixo:
    #print(getNome())   
    #print(getMatricula())

    tabuleiro = [' ']*10
    limpaTela() 

    tab = [' ',
    'X', ' ', 'X',
    ' ', 'O', 'X',
    ' ', ' ', ' ']
    #vazio = tabuleiroVazio(tab)
    disponiveis = pegaJogadasDisponiveis(tab)
    print(verificaPossívelVitoria(tab, disponiveis, 'X'))
    #preferencia = jogadas_preferenciais(disponiveis)
    
    #print(jogadaComputador(tab, 'O', vazio, disponiveis, preferencia))

"""
    simboloHumano, simboloHumano2 = escolheSimbolo()
    primeiroJogador = quemInicia()

    resultado = jogo(tabuleiro, simboloHumano, simboloHumano2, primeiroJogador)
    fimDeJogo(resultado, simboloHumano, simboloHumano2)
    """
## NÃO ALTERE O CÓDIGO ABAIXO ##
if __name__ == "__main__":
    main()

# nao deixar usar o 0
# fazer o computador ver se tem como ganhar e, um lance


## tabuleiro
## 7, 8, 9
## 4, 5, 6
## 1, 2, 3

## estratégia
### verificar se tem como ganhar em um lance
### buscar os cantos e depois o centro