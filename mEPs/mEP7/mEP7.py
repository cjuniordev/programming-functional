def recabeCandidatos(n, L=[''], i=1):
    if i <= n:
        nome = input()
        return recabeCandidatos(n, L + [nome], i + 1)
    else:
        return L

def recebeVotos(v, votos, i=0):
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
    if i < len(candidatos):
        print(f'{candidatos[i]}: {votos[i]}')
        return relatorio(candidatos, votos, i + 1)
    else:
        print(f'Brancos: {votos[0]}')
        print(f'Nulos: {votos[len(votos)-1]}')

def vencedor(candidatos, votos, candidato=0, maisVotado=0, i=0):
    if i < len(votos):
        if votos[i] > maisVotado:
            return vencedor(candidatos, votos, i, votos[i], i+1)
        return vencedor(candidatos, votos, candidato, maisVotado, i+1)
    else:
        return candidato

def main():
    # numero de candidatos
    n = int(input()) # 2 <= n <= 100
    candidatos = recabeCandidatos(n)

    # numero de eleitores/votos
    v = int(input())
    votos = recebeVotos(v, [0]*(n+2))

    relatorio(candidatos, votos)
    
    eleito = vencedor(candidatos, votos)
    print(f'Vencedor(a): {candidatos[eleito]}')

main()