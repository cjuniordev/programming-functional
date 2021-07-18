media = float(input('Média do aluno: '))

if media > 10.0 or media < 0:
    print('Erro! Digite uma nota válida')
elif media >= 9.0:
    print('A')
elif media >= 8.0:
    print('B')
elif media >= 7.0:
    print('C')
elif media >= 6.0:
    print('D')
else:
    print('R')