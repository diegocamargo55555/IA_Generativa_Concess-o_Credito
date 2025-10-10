from suport import *


populacao = gerar_populacao(10)

for i, individuo in enumerate(populacao, 1):
    individuo["fitness"] = fitness(individuo)
    
if len(populacao) > 0:
    ranking(populacao, 0, len(populacao) - 1)

print_populacao(populacao)    

