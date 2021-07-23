def ehNumero(valor):
    if isinstance(valor, int) or isinstance(valor, float):
        return True
    else:
        return False

def main():
    a_string = input('Digite um valor de texto: ')
    print(ehNumero(a_string))

    a_int = int(input('Digite um valor inteiro: '))
    print(ehNumero(a_int))

    a_float = float(input('Digite um valor real: '))
    print(ehNumero(a_float))

main()