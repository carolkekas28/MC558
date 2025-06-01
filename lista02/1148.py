import heapq

def CriarGrafo(Nos):
    Grafo = {}
    for i in range(1, Nos + 1):
        Grafo[i] = []
    return Grafo

def AdicionarAresta(Grafo, No1, No2, Peso):
    Grafo[No1].append((No2, Peso))
    Grafo[No2].append((No1, Peso))

def Dijkstra(Grafo, Origem):
    # Inicializar as distâncias como infinito
    Distancias = {No: float('inf') for No in Grafo}
    Distancias[Origem] = 0
    
    FilaPrioridade = [(0, Origem)]
    
    heapq.heapify(FilaPrioridade)

    while FilaPrioridade:
        DistanciaAtual, VerticeAtual = heapq.heappop(FilaPrioridade)
        
        for Vizinho, Peso in Grafo[VerticeAtual]:
            NovaDistancia = DistanciaAtual + Peso
            # Se encontramos um caminho mais curto, atualizamos
            if NovaDistancia < Distancias[Vizinho]:
                Distancias[Vizinho] = NovaDistancia
                heapq.heappush(FilaPrioridade, (NovaDistancia, Vizinho))
    
    return Distancias

def CriarMapa(N, E):
    Grafo = CriarGrafo(N)

    for i in range (E):
        U, V = map(int, input().split())
        AdicionarAresta(Grafo, U, V, 1)

    return Grafo

def VerificarSeHaCaminho(Distancias, P):
    for i in range (P):
        K, L = map(int, input().split())

        if Distancias[K][L] == float('inf'):
            print("Deu ruim")

        else:
            print("Lets que lets")

# Função principal
N, M, P = map(int, input().split())
Grafo = CriarMapa(N, M)

Distancias = {i: Dijkstra(Grafo, i) for i in range(1, N + 1)}

VerificarSeHaCaminho(Distancias, P)
