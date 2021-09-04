def concatena(L, i = 0, s = "0"):
    if type(L[i]) != str: return None
    if i < len(L):
        return concatena(L, i + 1, s + L[i])
    else:    
        return s

def main():
    lista = ["1", "0", "1", "1", "0"]
    resultado = concatena(lista)
    print(resultado)

main()