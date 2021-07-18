def convert(seconds):
    hours = seconds // 3600
    rest = seconds % 3600

    minutes = rest // 60
    rest = rest % 60

    print(f'{hours} : {minutes} : {rest}')

def main():
    s = int(input('Digite a quantidade de segundos: '))
    convert(s)

main()