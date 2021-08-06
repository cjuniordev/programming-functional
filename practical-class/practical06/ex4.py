def imprime(n, m):
    if n == m:
        print(m)
    else:
        print(n)
        imprime(n + 1, m)


def main():
    imprime(56, 100)

main()