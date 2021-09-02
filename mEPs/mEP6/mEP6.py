def verificaDimensoes(altura, largura=1):
    """
    Essa função verifica se as dimensões são válidas.
    retorna True em caso de válido ou False em caso de inválido
    """
    if altura > 0 and largura > 0:
        return True
    else:
        return False

def desenhaRetangulo(largura, altura, ascii, i=0):
    """
    Esta função desenha um retrangulo de dimensão {largura}x{altura} com os caracteres {ascii}
    sem retorno
    """
    if i == 0:
        print(ascii*largura)
        desenhaRetangulo(largura, altura, ascii, i+1)
    elif i == altura-1:
        print(ascii*largura)
    elif i < altura:
        print(ascii + " "*(largura - 2) + ascii)
        desenhaRetangulo(largura, altura, ascii, i+1)

def desenhaParalelograma(largura, altura, ascii, i=0):
    """
    Esta função desenha um paralelograma de dimensão {largura}x{altura} com os caracteres {ascii}
    sem retorno
    """
    if i == 0:
        print(ascii*largura)
        desenhaParalelograma(largura, altura, ascii, i+1)
    elif i == altura-1:
        print(" "*i + ascii*largura)
    elif i < altura:
        print(" "*i + ascii + " "*(largura - 2) + ascii)
        desenhaParalelograma(largura, altura, ascii, i+1)

def desenhaTrianguloEquilatero(altura, ascii, i=1, gap=0):
    """
    Esta função desenha um triangulo equilatero de altura {altura} com os caracteres {ascii}
    sem retorno
    """
    if i == altura:
        if altura%2==1:
            print(ascii*(altura*2-1))
        else:
            print(ascii*((2*altura)-1))
    elif i == 1:
        print(" "*(altura-1) + ascii)
        desenhaTrianguloEquilatero(altura, ascii, i+1, gap+1)
    elif i < altura:
        if altura%2==1:
            print(" "*(altura-i) + ascii + " "*(gap) + ascii)
            desenhaTrianguloEquilatero(altura, ascii, i+1, gap+2)
        else:
            if i-1 == 1:
                print(" "*(altura-i) + ascii + " "*(i-1) + ascii)
                desenhaTrianguloEquilatero(altura, ascii, i+1, gap+2)
            else:
                print(" "*(altura-i) + ascii + " "*gap + ascii)
                desenhaTrianguloEquilatero(altura, ascii, i+1, gap+2)
            
def desenhaTrianguloRetanguloEsquerdo(altura, ascii, i=1, gap=0):
    """
    Esta função desenha um triangulo retangulo esquerdo de altura {altura} com os caracteres {ascii}
    sem retorno
    """
    if i == altura:
        print(ascii*altura)
    elif i == 1:
        print(ascii)
        desenhaTrianguloRetanguloEsquerdo(altura, ascii, i+1)
    else:
        print(ascii + " "*gap + ascii)
        desenhaTrianguloRetanguloEsquerdo(altura, ascii, i+1, gap+1)

def desenhaTrianguloRetanguloDireito(altura, ascii, i=1, gap=0):
    """
    Esta função desenha um triangulo retangulo direito de altura {altura} com os caracteres {ascii}
    sem retorno
    """
    if i == altura:
        print(ascii*altura)
    elif i == 1:
        print(" "*(altura-i) + ascii)
        desenhaTrianguloRetanguloDireito(altura, ascii, i+1)
    else:
        print(" "*(altura-i) + ascii + " "*gap + ascii)
        desenhaTrianguloRetanguloDireito(altura, ascii, i+1, gap+1)

def desenhaDuasDimensoes(tipo, largura, altura, ascii):
    """
    Verica qual tipo de objeto de duas dimensoes deve ser desenhado e chama sua respectiva função
    sem retorno
    """
    if tipo == 'R':
        desenhaRetangulo(largura, altura, ascii)
    elif tipo == 'P':
        desenhaParalelograma(largura, altura, ascii)

def desenhaUmaDimensao(tipo, altura, ascii):
    """
    Verica qual tipo de objeto de uma dimensao deve ser desenhado e chama sua respectiva função
    sem retorno
    """
    if tipo == 'TE':
        desenhaTrianguloEquilatero(altura, ascii)
    elif tipo == 'TRE':
        desenhaTrianguloRetanguloEsquerdo(altura, ascii)
    elif tipo == 'TRD':
        desenhaTrianguloRetanguloDireito(altura, ascii)
    
def main():
    tipo = input()
    if tipo == 'R' or tipo == 'P':
        largura = int(input())
        altura = int(input())
        ascii = input()
        if verificaDimensoes(altura, largura):
            desenhaDuasDimensoes(tipo, largura, altura, ascii)
        else:
            print('Medida invalida.')
    elif tipo == 'TE' or tipo == 'TRE' or tipo == 'TRD':
        altura = int(input())
        ascii = input()
        if verificaDimensoes(altura):
            desenhaUmaDimensao(tipo, altura, ascii)
        else:
            print('Medida invalida.')
    else:
        print('Objeto invalido.')

main()