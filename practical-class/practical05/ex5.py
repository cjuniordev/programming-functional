def divisivel(x, y):
    return 0 if ( x % y == 0) else 1

def main():
    x = int(input('X: '))
    y = int(input('Y: '))

    print(divisivel(x, y))

main()