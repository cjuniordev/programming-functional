from random import randint

def sorteioMegaSena(L=[], i=0):
    if i < 6:
        n = randint(1, 60)
        if n in L:
            return sorteioMegaSena(L, i)
        return sorteioMegaSena(L + [n], i+1)
    else:
        return L

def main():
    print(sorteioMegaSena())

main()