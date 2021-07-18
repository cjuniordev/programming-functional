contaPar = 0
contaImpar = 1
x = int(input('Digite um número: '))

if x % 2 == 0:
    contaPar += 1
else:
    contaImpar += 1

x = int(input('Digite um numero: '))
if x % 2 == 0:
    contaPar += 1 
else:
    contaImpar += 1

x = int(input('Digite um numero: '))
if x % 2 == 0:
    contaPar += 1
else:
    contaImpar += 1

x = int(input('Digite um numero: '))
if x % 2 == 0:
    contaPar += 1
else:
    contaImpar += 1

media = contaImpar / 4
print(f'Foram digitados {contaPar} números pares e {media} media de números impares')