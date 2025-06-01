def CriaLabirinto(Vertices, Arestas):
    # Iremos representar os adjacentes como um conjunto, por conta de arestas repetidas
    Labirinto = {v: set() for v in range(0, Vertices)}
    for j in range(Arestas):
        Nodo1, Nodo2 = map(int, input().split())
        Labirinto[Nodo1].add(Nodo2)
        Labirinto[Nodo2].add(Nodo1)
    return Labirinto

def CalculaQuantidadeMov(Labirinto):
    return sum(len(Vizinhos) for Vizinhos in Labirinto.values())

TotalCasos = int(input())
QuantidadeMovimentos = []

# Vamos processar os movimentos pra cada labirinto
for i in range(TotalCasos):
    NodoInicial = int(input())
    Vertices, Arestas = map(int, input().split())

    # Representando o labirinto como uma lista de adjacências
    Labirinto = CriaLabirinto(Vertices, Arestas)
    numMovimentos = CalculaQuantidadeMov(Labirinto)
    QuantidadeMovimentos.append(numMovimentos)

# Printando o resultado
for numMovimentos in QuantidadeMovimentos:
    print(numMovimentos)