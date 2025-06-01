def EncontraFamilia(Pessoa, Familias):
    for Familia in Familias:
        if Pessoa in Familia:
            return Familias.index(Familia) # Retorna o indice da familia da pessoa
    return -1 # Caso ela nao tenha familia, retorna -1 para indicar

def ContaFamilias(M, N, Relacoes):
    # Inicializamos a lista de familias como uma lista vazia
    Familias = []

    for Relacao in Relacoes:
        # Pessoa1 relaçao Pessoa2
        Pessoa1 = Relacao.split()[0]
        Pessoa2 = Relacao.split()[2]
        # Verificamos os indices de cada pessoa para ver se elas possuem ou nao familia
        IndiceFamilia1 = EncontraFamilia(Pessoa1, Familias)
        IndiceFamilia2 = EncontraFamilia(Pessoa2, Familias)
        # Vamos verificar os casos possiveis
        if IndiceFamilia1 == -1 and IndiceFamilia2 == -1: # Ambas nao tem familia
            novaFamilia = set([Pessoa1, Pessoa2])
            Familias.append(novaFamilia)

        elif IndiceFamilia1 != -1 and IndiceFamilia2 == -1: # 1 esta em uma familia, 2 nao
            Familias[IndiceFamilia1].add(Pessoa2)

        elif IndiceFamilia1 == -1 and IndiceFamilia2 != -1: # 2 esta em uma familia, 1 nao
            Familias[IndiceFamilia2].add(Pessoa1)

        elif IndiceFamilia1 != -1 and IndiceFamilia2 != -1: # Ambas ja tem uma familia
            if IndiceFamilia1 != IndiceFamilia2: # Checa se sao familias distintas
                Familias[IndiceFamilia1].update(Familias[IndiceFamilia2])
                Familias.pop(IndiceFamilia2)
    
    return len(Familias)

M, N = map(int, input().split())
Relacoes = [input() for i in range (N)]

numeroFamilias = ContaFamilias(M, N, Relacoes)
print(numeroFamilias)