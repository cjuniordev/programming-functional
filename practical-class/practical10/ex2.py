def soma1(L, i = 0):
    #Implemente a função usando a variável 'i' para controlar 
    # o número de vezes que a função será chamada recursivamente]
    if i < len(L):
        return L[i] + soma1(L, i+1)
    else:
        return 0

def soma2(L):
    #Implemente a função usando fatiamento
    if len(L) == 0:
        return 0
    else:
        return L[0] + soma2(L[1:])

def main():
    print("Soma1: ", soma1(list(range(1, 100))))
    print("Soma2: ", soma2(list(range(1, 100))))

main()