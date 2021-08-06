def fatorial(n):
    if type(n) == int and n >= 0:
        return 1 if n == 0 or n == 1 else n*fatorial(n-1)
    else:
        return 'Valor Inválido'

def main():
    n=5
    print(f"{n}! = {fatorial(n)}")
    n=-2
    print(f"{n}! = {fatorial(n)}")

main()