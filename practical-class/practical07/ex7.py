import esfera

def main():
    esfera.areaEsfera1()

    r = float(input('Digite o valor do raio: '))
    
    esfera.areaEsfera2(r)
    print(f'Área: {esfera.areaEsfera3(r)}')

main()