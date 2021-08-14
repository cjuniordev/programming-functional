import random as r

def contaAcerto(n1, n2, n3, n4, n5, n6, sorteio, acertos):
    """
    Recebe os valores do usuario e o numeor sorteado, conta os acertos do usuário, soma nos acertos e o retorna.
    """
    if n1 == sorteio: acertos += 1
    if n2 == sorteio: acertos += 1
    if n3 == sorteio: acertos += 1
    if n4 == sorteio: acertos += 1
    if n5 == sorteio: acertos += 1
    if n6 == sorteio: acertos += 1

    return acertos

def megaSena(n1, n2, n3, n4, n5, n6, n, maxi, i=0, sorteio=0, acertos=0):
    """
    Sorteia 'maxi' números de 1 à 'n' e conta acertos.
    """
    if 60<n1 or n1<=0 or 60<n2 or n2<=0 or 60<n3 or n3<=0 or 60<n4 or n4<=0 or 60<n5 or n5<=0 or 60<n6 or n6<=0: 
        print('Valor inválido! Tente novamente')
        return 0

    sorteio = r.randint(1, n)
    if i == maxi:
        return contaAcerto(n1, n2, n3, n4, n5, n6, sorteio, acertos)
    else:
        acertos += contaAcerto(n1, n2, n3, n4, n5, n6, sorteio, acertos)
        acertos += megaSena(n1, n2, n3, n4, n5, n6, n, maxi, i + 1, acertos)
        return acertos

def megaSenaTunada(n1, n2, n3, n4, n5, n6, simulacoes, n, maxi, i=0, acertos=0):
    """
    Simula 'simulacoes' sorteios e soma o total de acertos
    """
    if i == simulacoes - 1:
        acertos += megaSena(n1, n2, n3, n4, n5, n6, n, maxi)
    else:
        acertos += megaSena(n1, n2, n3, n4, n5, n6, n, maxi)
        acertos += megaSenaTunada(n1, n2, n3, n4, n5, n6, simulacoes, n, maxi, i + 1, acertos)

    return acertos

def main():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))
    n3 = int(input('Digite um número: '))
    n4 = int(input('Digite um número: '))
    n5 = int(input('Digite um número: '))
    n6 = int(input('Digite um número: '))
    
    qtd_simulacao = int(input('Insira o número de simulações: '))

    n = 6
    maxi = 60
    sorteio = megaSenaTunada(n1, n2, n3, n4, n5, n6, n, maxi, qtd_simulacao)
    print(f'Acertos: {sorteio}')

main()