def divisores(n, L=[], i=1):
    if i <= n:
        if n % i == 0:
            return divisores(n, L + [i], i + 1)
        else:
            return divisores(n, L, i + 1)
    else:
        return L

def listaPrimos(n, L=[], i=0, j=2): # Se precisar, pode adiconar outros parâmetros opcionais
    if i < n:
        w = divisores(j)
        if len(w) == 2:
            return listaPrimos(n, L + [j], i+1, j+1)
        else:
            return listaPrimos(n, L, i, j+1)
    else:
        return L

def main():
    print(listaPrimos(5))
    print(listaPrimos(10))
    L = listaPrimos(15)
    print([x**2 for x in L])
    # A linha acima multiplica cada elemento de L por 2

main()