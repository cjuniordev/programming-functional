# x e y são números reais
# op é a operação que será feita
x = float(input())
op = input()
y = float(input())

# flags
opIsValid = True
yIsZero = False

if op == '+':
    resultado = x + y
elif op == '-':
    resultado = x - y
elif op == '*':
    resultado = x * y
elif op == '//':
    if y == 0:
        yIsZero = True
    else:
        resultado = x // y
elif op == '%':
    if y == 0:
        yIsZero = True
    else:
        resultado = x % y
elif op == '**':
    resultado = x ** y
else:
    opIsValid = False

if(opIsValid):
    if not yIsZero:
        print(f'{x} {op} {y} = {resultado}')
    else:
        print('Divisao por 0!')
else:
    print('Operacao nao reconhecida!')