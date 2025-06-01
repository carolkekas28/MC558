def CriarGrafo(Nos):
    Grafo = {}
    for i in range(Nos + 1):
        Grafo[i] = []
    return Grafo

def AdicionarAresta(Grafo, No1, No2, Peso):
    Grafo[No1].append((No2, Peso))
    Grafo[No2].append((No1, Peso))

def EncontrarPai(Pai, No):
    if Pai[No] != No:
        Pai[No] = EncontrarPai(Pai, Pai[No])
    return Pai[No]

def UnirConjuntos(Pai, Rank, No1, No2):
    Raiz1 = EncontrarPai(Pai, No1)
    Raiz2 = EncontrarPai(Pai, No2)

    if Raiz1 != Raiz2:
        if Rank[Raiz1] > Rank[Raiz2]:
            Pai[Raiz2] = Raiz1
        elif Rank[Raiz1] < Rank[Raiz2]:
            Pai[Raiz1] = Raiz2
        else:
            Pai[Raiz2] = Raiz1
            Rank[Raiz1] += 1

def Kruskal(Grafo, CustoTotal):
    Arestas = []

    for No in Grafo:
        for Vizinho, Peso in Grafo[No]:
            if No < Vizinho:
                Arestas.append((No, Vizinho, Peso))

    Arestas.sort(key=lambda valor: valor[2])

    N = len(Grafo)
    Pai = list(range(N))
    Rank = [0] * N

    MST = []
    CustoMST = 0
    for No1, No2, Peso in Arestas:
        if EncontrarPai(Pai, No1) != EncontrarPai(Pai, No2):
            MST.append((No1, No2, Peso))
            UnirConjuntos(Pai, Rank, No1, No2)
            CustoMST += Peso
    
    return CustoTotal - CustoMST

def LerVariaveis():
    m, n = map(int, input().split())
    return m, n

m, n = LerVariaveis()

while m != 0 and n != 0:
    Grafo = CriarGrafo(m)
    CustoTotal = 0

    for i in range(n):
        x, y, z = map(int, input().split())
        AdicionarAresta(Grafo, x, y, z)
        CustoTotal += z
    
    ValorEconomizado = Kruskal(Grafo, CustoTotal)
    print(ValorEconomizado)

    m, n = LerVariaveis()