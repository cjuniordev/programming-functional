numero = int(input('Digite um número: '))

if numero < 100 or numero > 999:
    print('Erro! Número inválido')
else:
    primeiro = numero // 100
    resto = numero % 100
    segundo = resto // 10
    resto = numero % 10
    terceiro = resto

    if primeiro < segundo:
        if segundo < terceiro:
            print(primeiro, segundo, terceiro)
        elif primeiro > terceiro:
            print(terceiro, primeiro, segundo)
        else:
            print(primeiro, terceiro, segundo)
    else:
        if primeiro < terceiro:
            print(segundo, primeiro, terceiro)
        elif segundo > terceiro:
            print(terceiro, segundo, primeiro)
        else:
            print(segundo, terceiro, primeiro)