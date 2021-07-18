import math

def combinations(n, p):
    if p <= n:
        print(math.factorial(n) / ( math.factorial(n - p) * math.factorial(p) ) )
    else:
        print('Erro')

def main():
    n = int(input('Digite um valor para n: '))
    p = int(input('Digite um valor para p: '))

    combinations(n, p)

main()