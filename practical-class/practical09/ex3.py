def uneSemRepetidos(l1, l2, L1=[], L2=[], i=0):
    if i == 0:
        return uneSemRepetidos(l1, l2, l1+l2, L2, i+1)
    elif i <= len(L1):
        if L1[i-1] not in L2:
            L2 += [L1[i-1]]
        return uneSemRepetidos(l1, l2, L1, L2, i+1)
    else: 
        return L2


def main():
    l1 = [1, 2, 3, 3]
    l2 = [1, 5, 3]
    print(uneSemRepetidos(l1, l2))

main()