def imprime(i):
    if i > 0:
        print(i)
        imprime(i-1)

imprime(5)