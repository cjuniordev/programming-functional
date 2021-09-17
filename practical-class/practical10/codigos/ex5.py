def myMap(f, x, V = []):
    if len(x) == 0:
        return V
    else: 
        a = f(x[0])
        return myMap(f, x[1:], V + [a])
    
def funcao1(x):
    return x**2
    
funcao2 = lambda x: x**3

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
y1 = myMap(funcao1, x)
y2 = myMap(funcao2, x)
y3 = myMap(lambda a:a**4, x)
print(y1)
print(y2)
print(y3)