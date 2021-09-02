# receber o tipo de obj a ser desenhado (R, P, TE, TRE, TRD)
# receber tamanhos(altura para triangulas, HxW para outros)
# receber char ASCII

# se o tipo de obj ano existir, exibir: 'Objeto invalido'
# se as medidas nao forem maior que zero, exibir: 'Medida invalida'
# no caso dos dois erros, exibir a primeira mensagem

def quantasDimensoes(tipo):
    if tipo == 'R' or tipo == 'P':
        return 2
    elif tipo == 'TE' or tipo == 'TRE' or tipo == 'TRD':
        return 1
    else:
        return 0

def verificaDimensoes(largura, altura):
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

def desenhaDuasDimensoes(tipo, largura, altura, ascii):
    if tipo == 'R':
        desenhaRetangulo(largura, altura, ascii)
    else:
        desenhaParalelograma(largura, altura, ascii)

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
                print(f'{" "*(altura-i)}{ascii}{" "*(gap + 1)}{ascii}')
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

def desenhaUmaDimensao(tipo, altura, ascii):
    if tipo == 'TE':
        desenhaTrianguloEquilatero(altura, ascii)
    elif tipo == 'TRE':
        desenhaTrianguloRetanguloEsquerdo(altura, ascii)
    elif tipo == 'TRD':
        desenhaTrianguloRetanguloDireito(altura, ascii)

def main():
    tipo = input()
    if quantasDimensoes(tipo) == 2:
        largura = int(input())
        altura = int(input())
        ascii = input()
        if not verificaDimensoes(largura, altura):
            print('Medida invalida')
        else:
            desenhaDuasDimensoes(tipo, largura, altura, ascii)

    elif quantasDimensoes(tipo) == 1:
        largura = 1
        altura = int(input())
        ascii = input()
        if not verificaDimensoes(largura, altura):
            print('Medida invalida')
        else:
            desenhaUmaDimensao(tipo, altura, ascii)
    else:
        print('Objeto invalido')

main()