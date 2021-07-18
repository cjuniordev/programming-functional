nota1 = input('Digite sua nota 1: ')
nota2 = input('Digite sua nota 2: ')
nota3 = input('Digite sua nota 3: ')

nota1, nota2, nota3 = float(nota1), float(nota2), float(nota3)

print('\n---------------------------\n')

print('Nota da  primeira  prova:', nota1)
print('Nota da  segunda  prova:', nota2)
print('Nota da  terceira  prova:', nota3)

print('\n---------------------------\n')

media = (nota1 + nota2 + nota3) / 3
provafinal = media < 7
print('Nota  media  do  aluno:', media)
print('Necessita da prova final:', provafinal)