def f1(n, m):
    """imprime de n até m"""
    if n<=m:
        print("Ida:", n)
        f1(n+1, m)
        print("Volta:", n)

def f2(n, m):
    """imprime de n até m"""
    if n>m:
        return #mesmo que return None
    else:
        print(n)
        f2(n+1, m) 

def f3(n, m):
    """imprime de n até m"""
    print(n)
    if n==m:
        return None
    f3(n+1, m)

def f4(n, m):
    """imprime de n até m"""
    print(n)
    if n!=m:
        f4(n+1, m)

def f5(n, m):
    """imprime de m até n"""
    if n <= m:
        print(f'Ida: {n}')
        f5(n+1, m)
        print(n)

def main():
    print("f1(0,10)")
    # funcao f1 printa de n ate m na ida e depois m ate n na volta
    f1(10, 5) # nao funciona quando n > m
    print("f2(0,10)")
    f2(10, 5) # n ate m // nao funciona quando n > m
    #print("f3(0,10)")
    #f3(10, 5) # n ate m // recursao infinita nao quando n > m
    #print("f4(0,10)")
    #f4(10, 5) # n ate m // recursao infinita nao quando n > m
    print("f5(0,10)")
    f5(10, 5) # m até n // nao funciona quando n > m

main()