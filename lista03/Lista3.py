import pulp as plp

# Definindo o problema
max_z = plp.LpProblem("Maximizar Z", plp.LpMaximize)

# Definindo as variaveis do problema
x1 = plp.LpVariable("x1", lowBound=0, cat='Integer')
x2 = plp.LpVariable("x2", lowBound=0, cat='Integer')
x3 = plp.LpVariable("x3", lowBound=0, cat='Integer')

# Escrevendo a funçao objetivo
max_z += 50*x1 + 40*x2 + 45*x3

# Escrevendo as restrições
max_z += 1.2*x1 + 0.8*x2 + 1.0*x3 <= 1500
max_z += 0.1*x1 + 0.1*x2 + 0.1*x3 <= 70
max_z += -1*x1 <= -100
max_z += -1*x2 <= -80
max_z += -1*x3 <= -60

# Resolvendo o problema
max_z.solve()
print("Vinho tinto: " + str(int(x1.varValue)) + " garrafas")
print("Vinho branco: " + str(int(x2.varValue)) + " garrafas")
print("Vinho rosé: " + str(int(x3.varValue)) + " garrafas")
print("Lucro máximo: R$" + str(plp.value(max_z.objective)))
