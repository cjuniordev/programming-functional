import math

def f(x):
    if x <= 1:
        result = math.log(x)
    elif 1 < x and x <= 2:
        result = math.log10x + math.sqrt(x)
    elif 2 < x and x <= 5:
        result = x**2 + math.exp(x)
    else:
        result = x**(x/2) + math.log2(x)

    return result

def main():
    x = float(input('Digite um valor para x: '))
    print(f(x))

main()