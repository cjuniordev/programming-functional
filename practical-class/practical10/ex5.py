def myMap(f, x, V = []):
    if len(x) == 0:
        return V
    else: 
        a = f(x[0])
        return myMap(f, x[1:], V + [a])

def myMap2(f, x, V=[], i=0):
    if i < len(x):
        a = f(x[i])
        return myMap2(f, x, V + [a], i+1)
    else: 
        return V


def funcao1(x):
    return x**2
    
funcao2 = lambda x: x**3

""" # myMap
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
y1 = myMap(funcao1, x)
y2 = myMap(funcao2, x)
y3 = myMap(lambda a:a**4, x)
print(y1)
print(y2)
print(y3)

# myMap2
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
y1 = myMap2(funcao1, x)
y2 = myMap2(funcao2, x)
y3 = myMap2(lambda a:a**4, x)
print(y1)
print(y2)
print(y3) """

# para criar my filter, precisamos pegar o elemento da lista se, quando ele passado para funcao f, retorna True
# exemplo abaixo
L = [4, -9, 25, -36, -49]

def myFilter(f, x, V=[]):
    if len(x) == 0:
        return V
    else: 
        if f(x[0]):
            return myFilter(f, x[1:], V + [x[0]])
        else:
            return myFilter(f, x[1:], V)

print(myFilter(lambda y: y % 2 == 1, L))