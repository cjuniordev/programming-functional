a = int(input('Digite o valor da carta A: '))
b = int(input('Digite o valor da carta B: '))
c = int(input('Digite o valor da carta C: '))

if 0 <= a <= 100 and 0 <= b <= 100 and 0 <= c <= 100 :
    if a == b:
        print(c)
    else:
        if b == c:
            print(a)
        else:
            if a == c:
                print(b)
            else:
                print('Sem solução')
else:
    print('Valores inválidos, Tente novamente!')