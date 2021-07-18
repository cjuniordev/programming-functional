jogador1 = input('X ou O? ')

if jogador1 == 'X':
    jogador2 = 'O'
elif jogador1 == 'O':
    jogador2 = 'X'
else:
    print('Erro! Tente novamente!')

print(jogador1, jogador2)