def B(n):
    if n == 0:
        return 0
    else:
        b = n % 2 + 10 * B(n // 2)
    
    return b

def main():
    print(B(0))
    print(B(1))
    print(B(2))
    print(B(3))
    print(B(4))
    print(B(5))
    print(B(6))
    print(B(7))
    print(B(8))
    print(B(9))
    print(B(10))
    print(B(11))
    print(B(12))
    print(B(13))
    ## a funcao B(n) imprime o número em binário

main()