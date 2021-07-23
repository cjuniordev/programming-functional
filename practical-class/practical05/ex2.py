def soma3(x, y):
    return x + y
    print("Chegouaqui!")

def main():
    x = float(input('Digite um número: '))
    y = float(input('Digite outro: '))
    print(soma3(x, y))

main()


# A mensagem do print dentro da função soma3 não foi executada porque 
# ela está depois de um return, 
# quando a função retorna algo ela nao executa o resto de suas linhas.