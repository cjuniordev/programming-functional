def quantasDimensoes(tipo):
    if tipo == 'R' or tipo == 'P':
        return 2
    elif tipo == 'TE' or tipo == 'TRE' or tipo == 'TRD':
        return 1
    else:
        return 0

def verificaDimensoes(altura, largura=1):
    if altura > 0 and largura > 0:
        return True
    else:
        return False

def desenhaRetangulo(largura, altura, ascii, i=0):
    if i == 0:
        print(f'{ascii*largura}')
        desenhaRetangulo(largura, altura, ascii, i+1)
    elif i == altura-1:
        print(f'{ascii*largura}')
    elif i < altura:
        print(f'{ascii}{" "*(largura - 2)}{ascii}')
        desenhaRetangulo(largura, altura, ascii, i+1)

def desenhaParalelograma(largura, altura, ascii, i=0):
    if i == 0:
        print(f'{ascii*largura}')
        desenhaParalelograma(largura, altura, ascii, i+1)
    elif i == altura-1:
        print(f'{" "*i}{ascii*largura}')
    elif i < altura:
        print(f'{" "*i}{ascii}{" "*(largura - 2)}{ascii}')
        desenhaParalelograma(largura, altura, ascii, i+1)

def desenhaTrianguloEquilatero(altura, ascii, i=1, gap=0):
    if i == altura:
        if altura%2==1:
            print(f'{ascii*(altura*2-1)}')
        else:
            print(f'{ascii*((2*altura)-1)}')
    elif i == 1:
        print(f'{" "*(altura-1)}{ascii}')
        desenhaTrianguloEquilatero(altura, ascii, i+1, gap+1)
    elif i < altura:
        if altura%2==1:
            print(f'{" "*(altura-i)}{ascii}{" "*(gap)}{ascii}')
            desenhaTrianguloEquilatero(altura, ascii, i+1, gap+2)
        else:
            if i-1 == 1:
                print(f'{" "*(altura-i)}{ascii}{" "*(i-1)}{ascii}')
                desenhaTrianguloEquilatero(altura, ascii, i+1, gap+2)
            else:
                print(f'{" "*(altura-i)}{ascii}{" "*gap}{ascii}')
                desenhaTrianguloEquilatero(altura, ascii, i+1, gap+2)
            
def desenhaTrianguloRetanguloEsquerdo(altura, ascii, i=1, gap=0):
    if i == altura:
        print(ascii*altura)
    elif i == 1:
        print(ascii)
        desenhaTrianguloRetanguloEsquerdo(altura, ascii, i+1)
    else:
        print(ascii + " "*gap + ascii)
        desenhaTrianguloRetanguloEsquerdo(altura, ascii, i+1, gap+1)

def desenhaTrianguloRetanguloDireito(altura, ascii, i=1, gap=0):
    if i == altura:
        print(ascii*altura)
    elif i == 1:
        print(" "*(altura-i) + ascii)
        desenhaTrianguloRetanguloDireito(altura, ascii, i+1)
    else:
        print(" "*(altura-i) + ascii + " "*gap + ascii)
        desenhaTrianguloRetanguloDireito(altura, ascii, i+1, gap+1)

def desenhaDuasDimensoes(tipo, largura, altura, ascii):
    if tipo == 'R':
        desenhaRetangulo(largura, altura, ascii)
    else:
        desenhaParalelograma(largura, altura, ascii)

def desenhaUmaDimensao(tipo, altura, ascii):
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