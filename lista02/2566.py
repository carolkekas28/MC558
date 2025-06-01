import heapq

def CriarGrafo(Nos):
    Grafo = {}
    for i in range(Nos):
        Grafo[i] = []
    return Grafo

def AdicionarAresta(Grafo, No1, No2, Peso):
    Grafo[No1].append((No2, Peso))
    Grafo[No2].append((No1, Peso))

def Dijkstra(Grafo, Origem):
    # Initialize single source
    Distancias = {No: float('inf') for No in Grafo}
    Distancias[Origem] = 0
    
    FilaPrioridade = [(0, Origem)]
    
    heapq.heapify(FilaPrioridade)

    while FilaPrioridade:
        DistanciaAtual, VerticeAtual = heapq.heappop(FilaPrioridade)
        
        for Vizinho, Peso in Grafo[VerticeAtual]:
            NovaDistancia = DistanciaAtual + Peso
            
            if NovaDistancia < Distancias[Vizinho]:
                Distancias[Vizinho] = NovaDistancia
                heapq.heappush(FilaPrioridade, (NovaDistancia, Vizinho))
    
    return Distancias

