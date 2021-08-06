def desenha1(n, c="*", i=1):
    """
    Esta função desenha um quadrado nxn na tela
    """
    if i <=n :
        print(c*n) 
        desenha1(n, c, i+1)

def desenha2(n, c="*", i=1):
    """
    Esta função desenha um triangulo retangulo de altura n a base n na tela
    """
    if i <= n:
        print(c*i)
        desenha2(n, c, i+1)

def desenha3(n, c="*", i=1):
    """
    Esta função desenha um triangulo isósceles de base n na tela
    """
    if n % 2 == 0:
        print("n deve ser impar")
    if i <= n:
        ne = (n-i) // 2
        print(" "*ne + c*i)
        desenha3(n, c, i+2)

def main():
    desenha3(5)

main()