def soma1():
    x = float(input('Digite um número: '))
    y = float(input('Digite outro: '))
    return x + y

def soma2(x, y):
    return x + y

def main():
    print(soma1())

    a = float(input('Digite um número: '))
    b = float(input('Digite outro: '))
    print(soma2(a, b))

main()