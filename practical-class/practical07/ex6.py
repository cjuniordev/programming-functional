def M(a, b):
    """Multiplica a por b"""
    if not isinstance(b, int) or b < 0:
        print("ERRO")
        return None
    elif b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a + M(a, b - 1)
        
def DI(a, b):
    """Divide inteiro, a por b"""
    if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b <= 0:
        print("ERRO")
        return None
    if a < b:
        return 0
    else:
        return 1 + DI(a - b, b)

def RD(a, b):
    """Resto da Divisão de a por b"""
    if a < b:
        return a
    else:
        return RD(a - b, b)
        
def main():
    print(M(2, 3))
    print(M(4, 2))
    print(DI(2, 3))
    print(DI(3, 2))
    print(DI(4, 2))
    print(DI(10, 6))
    print(RD(2, 3))
    print(RD(3, 2))
    print(RD(25.5, 10.5))

    """ Saída:
        6
        8   
        0
        1
        2
        1
        2
        1
        4.5 
    """

main()