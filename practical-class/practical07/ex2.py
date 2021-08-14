def f1(n):
    """Retorna a quantidade de números naturais pares menores ou iguais a n"""
    if n == 0:
        return 1
    elif n % 2==0:
        pares = 1 + f1(n-2) #Porque n-2? Pois se o numero cai nessa condição, ele ja é par, fazendo n-2 vai ser o próximo número par
    else:
        pares =  f1(n-1) #Porquen-1? Pois se um numéro é impar, se remover n - 1 dele, ele fica par

    return pares
        
def f2(n):
    """Retorna a soma dos números naturais menores ou iguais a n"""
    return 1 if n==1 else n + f2(n - 1)

def main():
    print(f'Qtd de números pares: {f1(10)}')
    print(f'Soma dos números naturais menores que n: {f2(10)}')

main()