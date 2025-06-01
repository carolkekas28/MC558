def EhCosta(i, j, M, N, mapa):
    if mapa[i][j] == '#':
        # Verificamos em cima
        if i == 0 or mapa[i-1][j] == '.':
            return True
        # Verificamos em baixo
        if i == M - 1 or mapa[i+1][j] == '.':
            return True
        #Verificamos à esquerda
        if j == 0 or mapa[i][j-1] == '.':
            return True
        #Verificamos à direita
        if j == N - 1 or mapa[i][j+1] == '.':
            return True
        return False
    
def ContaCostas(mapa, M, N):
    numeroCostas = 0
    for i in range(M):
        for j in range(N):
            if EhCosta(i, j, M, N, mapa):
                numeroCostas += 1
    return numeroCostas

M, N = map(int, input().split())
mapa = [input().strip() for _ in range(M)]

quantidadeCostas = ContaCostas(mapa, M, N)
print(quantidadeCostas)