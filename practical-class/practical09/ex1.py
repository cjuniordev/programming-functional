def myRange1(n, L=[], i=0):
    if i == n:
        return L + [i]
    else:
        return myRange1(n, L + [i], i+1)
## caso fosse [i] + L, a lista ficaria invertida(decrescente)

def myRange2(a, b, L=[]):
    if a > b:
        return []

    if a == b:
        return L + [a]
    else:
        return myRange2(a + 1, b, L + [a])

def myRange3(a, b, s, L=[]):
    if a > b:
        return []

    if a >= b:
        return L + [a]
    else:
        return myRange3(a + s, b, s, L + [a])

def myRange(a=0, b=0, s=0):
    if s > 0:
        return myRange3(a, b, s)
    elif b > 0:
        return myRange2(a, b)
    else:
        return myRange1(a)

def main():
    print(myRange(10))
    print(myRange(2, 10))
    print(myRange(10, 2))
    print(myRange(0, 10, 2))
    print(myRange(5, 30, 5))

main()