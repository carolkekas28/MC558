def CriarGrafo(Nos):
    Grafo = [[0]*(Nos + 1) for _ in range(Nos + 1)]
    return Grafo

def AdicionarAresta(Grafo, Origem, Destino, Capacidade):
    Grafo[Origem][Destino] = Capacidade
    Grafo[Destino][Origem] = 0

def BFS(Grafo, Fonte, Sumidouro, Vertices, Pai):
    Visitados = [False] * Vertices
    Fila = [Fonte]
    Visitados[Fonte] = True
    Pai[Fonte] = -1

    while Fila:
        VerticeAtual = Fila.pop(0)

        for Vizinho in range(Vertices):
            if not Visitados[Vizinho] and Grafo[VerticeAtual][Vizinho] > 0:
                Fila.append(Vizinho)
                Visitados[Vizinho] = True
                Pai[Vizinho] = VerticeAtual

                if Vizinho == Sumidouro:
                    return True
    
    return False

def FordFulkerson(Grafo, Fonte, Sumidouro, Nos):
    GrafoResidual = [fila[:] for fila in Grafo]
    Pai = [-1] * Nos
    FluxoMaximo = 0

    while BFS(GrafoResidual, Fonte, Sumidouro, Nos, Pai):
        CaminhoFluxo = float('inf')
        v = Sumidouro

        while v != Fonte:
            u = Pai[v]
            CaminhoFluxo = min(CaminhoFluxo, GrafoResidual[u][v])
            v = u

        v = Sumidouro
        while v != Fonte:
            u = Pai[v]
            GrafoResidual[u][v] -= CaminhoFluxo
            GrafoResidual[v][u] += CaminhoFluxo
            v = u

        FluxoMaximo += CaminhoFluxo
    return FluxoMaximo

def EncontrarIndiceCamiseta(TamanhoCamiseta):
    if TamanhoCamiseta == 'XS':
        return 1
    elif TamanhoCamiseta == 'S':
        return 2
    elif TamanhoCamiseta == 'M':
        return 3
    elif TamanhoCamiseta == 'L':
        return 4
    elif TamanhoCamiseta == 'XL':
        return 5
    elif TamanhoCamiseta == 'XXL':
        return 6    

def ConectarFonteACamisetas(Grafo, N):
    for i in range (1, 7):
        AdicionarAresta(Grafo, 0, i, N//6)

def ReceberTamanhoCamisetas(Grafo, M):
    for i in range(M):
        # Conectando os nos das camisetas aos voluntarios
        Tamanho1, Tamanho2 = input().split()
        Tamanho1 = EncontrarIndiceCamiseta(Tamanho1)
        Tamanho2 = EncontrarIndiceCamiseta(Tamanho2)
        AdicionarAresta(Grafo, Tamanho1, 7 + i, 1)
        AdicionarAresta(Grafo, Tamanho2, 7 + i, 1)

        # Conectar cada voluntario ao sumidouro
        AdicionarAresta(Grafo, 7 + i, 7 + M, 1)

def VerificarSeHaDistribuicao(FluxoMaximo, M):
    if FluxoMaximo == M:
        print("YES")
    else:
        print("NO")

# 1->XS, 2->S, 3->M, 4->L, 5->XL, 6->XXL
NumeroCasos = int(input())
for i in range(NumeroCasos):
    N, M = map(int, input().split())
    Grafo = CriarGrafo(8 + M)

    ConectarFonteACamisetas(Grafo, N)
    ReceberTamanhoCamisetas(Grafo, M)

    FluxoMaximo = FordFulkerson(Grafo, 0, 7 + M, 8 + M)

    VerificarSeHaDistribuicao(FluxoMaximo, M)