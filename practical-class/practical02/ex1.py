distance = int(input())

if 0 > distance:
    print('0')
else:
    if distance <= 800:
        print('1')
    else:
        if distance <= 1400:
            print('2')
        else:
            if distance <= 2000:
                print('3')
            else:
                print('Entrada inválida')
        

