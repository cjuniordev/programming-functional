def f1(n, i=0, soma=0):
    if i <= n:
        return f1(n, i+1, soma+i)
    else:
        return soma

def imprimeSoma(m, i=1):
    if m != i:
        print(f'{i} = {f1(i)}')
        imprimeSoma(m, i + 1)
    else:
        print(f'{m} = {f1(m)}')

def main():
    imprimeSoma(10)

main()