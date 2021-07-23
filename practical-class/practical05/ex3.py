import math as m

def areaEsfera1():
    raio = float(input('Digite o Raio: '))
    area = 4 * m.pi * (raio**2)
    print(area)

def areaEsfera2(raio):
    area = 4 * m.pi * (raio**2)
    print(area)

def areaEsfera3(raio):
    area = 4 * m.pi * (raio**2)
    return area

def main():
    areaEsfera1()

    r = float(input('Digite o Raio: '))
    areaEsfera2(r)

    print(areaEsfera3(r))

main()