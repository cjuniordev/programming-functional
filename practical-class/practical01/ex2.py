import math
pi = math.pi

raio = float(input('Digite o valor do raio em centimetros: '))

area = 4 * pi * (raio**2)
volume = (3/4) * pi * (raio**3)

print('Área da esfera: ', area, 'cm')
print('Volume da esfera: ', volume, 'cm')