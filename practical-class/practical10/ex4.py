def divisores(n, L=[], i=1):
    if i <= n:
        if n % i == 0:
            return divisores(n, L + [i], i + 1)
        else:
            return divisores(n, L, i + 1)
    else:
        return L

n = 30 # recebe n
primos = [x for x in range(2, n) if len(divisores(x)) == 2]
print(f'Primos até {n}: {primos}') #devolve numeros primos