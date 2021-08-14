def P(n, nd=0, i=1):
    if n <= 1:
        return False

    if i == n:
        nd += 1
        return True if nd == 2 else False
    else:
        if n % i == 0:
            return P(n, i+1)
        else:
            return P(n, i+1)

def main():
    print(P(1))
    print(P(3))
    print(P(8))

    # a funcao retorna true se n for número primo
    # o parametro nd representa q quantidade de números dividem n
    # se for somente 2(1 e ele mesmo), é primo
    # sem nd a função nao funciona

main()
