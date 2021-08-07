# Programação I / Programação Funcional (2021-1)
# miniEP5 - Jogo da Velha

def imprimeTabuleiro(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e imprime o tabuleiro
    """
    print(f' {p7} | {p8} | {p9} ')
    print('---+---+---')
    print(f' {p4} | {p5} | {p6} ')
    print('---+---+---')
    print(f' {p1} | {p2} | {p3} ')

def entradaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores são válidos, ou seja, retorna True
    se cada variável possui " " ou "x" ou "o" e False, caso contrário.
    """
    if p1 != 'o' and p1 != 'x' and p1 != ' ': return False
    if p2 != 'o' and p2 != 'x' and p2 != ' ': return False
    if p3 != 'o' and p3 != 'x' and p3 != ' ': return False
    if p4 != 'o' and p4 != 'x' and p4 != ' ': return False
    if p5 != 'o' and p5 != 'x' and p5 != ' ': return False
    if p6 != 'o' and p6 != 'x' and p6 != ' ': return False
    if p7 != 'o' and p7 != 'x' and p7 != ' ': return False
    if p8 != 'o' and p8 != 'x' and p8 != ' ': return False
    if p9 != 'o' and p9 != 'x' and p9 != ' ': return False
    return True

def diferenca_valida(x, o):
    """
    Verifica se a diferença entre a quantidade de x e a quantidade de o é maior que 1
    """
    diferenca = x - o
    if diferenca < 0: diferenca *= (-1)

    if diferenca <= 1: return True
    return False

def jogadaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores formam uma jogada válida.

    Retorna True se a jogada for válida e False, caso contrário
    """
    conta_x = 0
    conta_o = 0

    if p1 == 'x': conta_x += 1
    elif p1 == 'o': conta_o += 1

    if p2 == 'x': conta_x += 1
    elif p2 == 'o': conta_o += 1

    if p3 == 'x': conta_x += 1
    elif p3 == 'o': conta_o += 1
    
    if p4 == 'x': conta_x += 1
    elif p4 == 'o': conta_o += 1

    if p5 == 'x': conta_x += 1
    elif p5 == 'o': conta_o += 1
    
    if p6 == 'x': conta_x += 1
    elif p6 == 'o': conta_o += 1

    if p7 == 'x': conta_x += 1
    elif p7 == 'o': conta_o += 1

    if p8 == 'x': conta_x += 1
    elif p8 == 'o': conta_o += 1

    if p9 == 'x': conta_x += 1
    elif p9 == 'o': conta_o += 1

    return diferenca_valida(conta_x, conta_o)
    
def quem_ganhou(char):
    """
    Recebe o caractere do vencedor, verifia se ele não é vazio e escreve que ele ganhou
    """
    if char == ' ': return False
    print("O jogador 'x' venceu!") if char == 'x' else print("O jogador 'o' venceu!")
    return True

def empate(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    if not (p1 == ' ' or p2 == ' ' or p3 == ' ' or p4 == ' ' or p5 == ' ' or p6 == ' ' or p7 == ' ' or p8 == ' ' or p9 == ' '):
        print('Empate!')

def verificaJogada(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    imprime se um jogador ('x' ou 'o') venceu a jogada. 
    (Cada variável representa uma posição no tabuleiro)
    """
    vitoria = False
    if p1 == p2 == p3 and p1 != ' ':
        vitoria = quem_ganhou(p1)
    elif p4 == p5 == p6 and p4 != ' ':
        vitoria = quem_ganhou(p4)
    elif p7 == p8 == p9 and p7 != ' ':
        vitoria = quem_ganhou(p7)
    elif p7 == p4 == p1 and p7 != ' ':
        vitoria = quem_ganhou(p7)
    elif p8 == p5 == p2 and p8 != ' ':
        vitoria = quem_ganhou(p8)
    elif p9 == p6 == p3 and p9 != ' ':
        vitoria = quem_ganhou(p9)
    elif p7 == p5 == p3 and p7 != ' ':
        vitoria = quem_ganhou(p7)
    elif p9 == p5 == p1 and p9 != ' ':
        vitoria = quem_ganhou(p9)
    
    if not vitoria:
        if p1 == ' ' or p2 == ' ' or p3 == ' ' or p4 == ' ' or p5 == ' ' or p6 == ' ' or p7 == ' ' or p8 == ' ' or p9 == ' ':
            print('O jogo nao terminou!')
        else:
            empate(p1, p2, p3, p4, p5, p6, p7, p8, p9)

def main():
    t1 = input()
    t2 = input()
    t3 = input()
    t4 = input()
    t5 = input()
    t6 = input()
    t7 = input()
    t8 = input()
    t9 = input()
    imprimeTabuleiro(t1, t2, t3, t4, t5, t6, t7, t8, t9)
    if not entradaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9):
        print("Entrada invalida!")
    elif not jogadaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9):
        print("Jogada invalida!")
    else:
        verificaJogada(t1, t2, t3, t4, t5, t6, t7, t8, t9)

main()
