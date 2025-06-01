# Funçao para construir o grafo que representa as cartas e as ligaçoes entre elas
def ConstroiGrafo(N, Conexoes): # N
    Grafo = [[] for _ in range(N)]
    for A, B in Conexoes:
        Grafo[A-1].append(B-1)
        Grafo[B-1].append(A-1)
    return Grafo

# Funçao para realizar uma busca em largura
def BFS(Grafo, Comeco, Fim, N):
    Fila = [(Comeco, 0)] # Inicializa a fila com o vertice de comeco e a distancia 0
    Frente = 0
    Tras = 1 # Ja iniciamos com 1 item na fila

    Visitados = [False]*N # Inicializa a lista de visitados
    Visitados[Comeco] = True

    while Frente < Tras:
        Vertice, Distancia = Fila[Frente]
        Frente += 1

        if Vertice == Fim:
            return Distancia
        
        for Vizinho in Grafo[Vertice]:
            if not Visitados[Vizinho]:
                Visitados[Vizinho] = True
                Fila.append((Vizinho, Distancia + 1))
                Tras += 1

# Funçao para encontrar a quantidade maxima de pontos possivel
def PontosMaximo(N, C, Conexoes):
    pontosMaximos = 0

    # Construimos o nosso grafo
    Grafo = ConstroiGrafo(N, Conexoes)

    # Criamos uma lista para armazenar as posiçoes de cartas iguais
    Posicoes = [[] for _ in range(N//2 + 1)]
    for i in range (N):
        Posicoes[C[i]].append(i)

    # Os numeros das cartas vao de 1 a N/2, entao vamos encontrar cartas correspondentes e calcular a distancia
    for i in range(1, N//2 + 1):
        Posicao1, Posicao2 = Posicoes[i] # Pegamos as duas posicoes da carta
        distancia = BFS(Grafo, Posicao1, Posicao2, N)
        pontosMaximos += distancia
    
    return pontosMaximos

# Recebendo os dados de entrada
N = int(input())
C = list(map(int, input().split()))
Conexoes = [tuple(map(int, input().split())) for _ in range(N-1)]

# Chamamos a funcao para achar o resultado
pontosMax = PontosMaximo(N, C, Conexoes)
print(pontosMax)