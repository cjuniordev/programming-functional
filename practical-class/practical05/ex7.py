import math as m

def volumeCilindro(raio, altura):
    if (isinstance(raio, float) or isinstance(raio, int)) and (isinstance(altura, float) or isinstance(altura, int)):
        return m.pi * (raio ** 2) * altura
    else:
        print('Erro!')
        return None

def main():
    r = float(input('Digite o Raio: '))
    h = float(input('Digite a Altura: '))
    print(volumeCilindro(r, h))

main()