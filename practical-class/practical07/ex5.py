def b(n):
    if type(n) != int or n < 0: #n deve ser um número natural
        print("ERRO: O argumento deve ser inteiro positivo")
        return None
    elif n < 2: #Você consegue pensar em uma forma de simplificar essa parte?
        if n == 0:
            return "0"
        else:
            return "1"
    else: #Você consegue pensar em uma forma de simplificar o return?
         return ("0" if n % 2==0 else "1") + b(n//2) # nao altera o valor retornado da função

def main():
    print("b(1) =", b(1))
    print("b(2) =", b(2))
    print("b(3) =", b(3))
    print("b(4) =", b(4))
    print("b(10) =", b(10))
    print("b(20) =", b(20))
    print("b(0) =", b(0))
    # a funcao retorna numeros correspondente em binário
    # n%1 se n for string, o codigo quebra

main()