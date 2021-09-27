def recebeCandidatos(n, L=[''], i=1):
    """
    Recebe um número inteiro 'n', faz uma recursão para receber os nomes dos candidatos na posição i.
    Retorna uma lista com n+1 posições com o nome de todos candidatos.
    """
    if i <= n:
        nome = input()
        return recebeCandidatos(n, L + [nome], i + 1)
    else:
        return L

def recebeVotos(v, votos, i=0):
    """
    Recebe um número inteiro 'v', faz uma recursão para receber os votos dos eleitores.
    cada voto para um c canditado, é somado 1 em sua posição na lista votos.
    retorna uma lista com todos os votos, onde a posição 0 são os votos brancos, e a última posição para nulos.
    """
    if i < v:
        voto = int(input())
        if voto >= (len(votos)-1):
            votos[len(votos)-1] += 1
        else:
            votos[voto] += 1
        return recebeVotos(v, votos, i+1)
    else:
        return votos

def relatorio(candidatos, votos, i=1):
    """
    Imprime um relatório com os votos por candidato, votos nulos e brancos
    """
    if i < len(candidatos):
        print(f'{candidatos[i]}: {votos[i]}')
        return relatorio(candidatos, votos, i + 1)
    else:
        print(f'Brancos: {votos[0]}')
        print(f'Nulos: {votos[len(votos)-1]}')

def vencedor(candidatos, votos, candidato=0, maisVotado=0, i=0):
    """
    Verifica quem mais recebeu votos e retorna a posição do vencedor
    """
    if i < len(votos):
        if votos[i] > maisVotado:
            return vencedor(candidatos, votos, i, votos[i], i+1)
        return vencedor(candidatos, votos, candidato, maisVotado, i+1)
    else:
        return candidato

def main():
    # numero de candidatos
    n = int(input())
    candidatos = recebeCandidatos(n)

    # numero de eleitores/votos
    v = int(input())
    
    # lista com tamanho n+2, pois n ==  numero de candidatos,
    # posição 0 para voto branco e posição n+1 para nulos
    l = [0]*(n+2)
    votos = recebeVotos(v, l)

    relatorio(candidatos, votos)
    
    eleito = vencedor(candidatos, votos)
    print(f'Vencedor(a): {candidatos[eleito]}')

main()