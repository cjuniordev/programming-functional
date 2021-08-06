def imprime(m, i = 1):
    if m == i:
        print(m)
    else:
        print(i)
        imprime(m, i + 1)


def main():
    imprime(7)

main()