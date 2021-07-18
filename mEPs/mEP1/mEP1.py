eixoX = float(input())
eixoY = float(input())

if eixoX == 0 or eixoY == 0:
    print('EIXOS')
else:
    if eixoX > 0 and eixoY > 0:
        print('I')
    else:
        if eixoX < 0 and eixoY > 0:
            print('II')
        else: 
            if eixoX < 0 and eixoY < 0:
                print('III')
            else:
                if eixoX > 0 and eixoY < 0:
                    print('IV')