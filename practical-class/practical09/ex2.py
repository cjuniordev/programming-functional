def semRepetidos(l1, L=[], i=0):
    if i < len(l1):
        if l1[i] not in L:
            L += [l1[i]]
        return semRepetidos(l1, L, i+1)
    else: 
        return L

def main():
    l1 = [1, 2, 1, 3, 2, 1, 4, 0]
    print(semRepetidos(l1))

main()