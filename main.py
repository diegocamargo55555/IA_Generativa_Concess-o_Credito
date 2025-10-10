from suport import *

tamInicial = 50
populacao = gerar_populacao(tamInicial)

for i, individuo in enumerate(populacao, 1):
    individuo["fitness"] = fitness(individuo)
    
if len(populacao) > 0:
    ranking(populacao, 0, len(populacao) - 1)


qntdMutacao = int((len(populacao)*0.15))    
qntdCruzamento = int((len(populacao)*0.83))
qntdCruzamento = qntdCruzamento-1 if qntdCruzamento%2 == 1 else qntdCruzamento

for geracao in range(0, 40):
    populacao = loopMutacao(populacao, qntdMutacao)   
    for i, individuo in enumerate(populacao, 1):
        individuo["fitness"] = fitness(individuo)
    
    populacao = loopCruzamento(populacao, qntdCruzamento)
    for i, individuo in enumerate(populacao, 1):
        individuo["fitness"] = fitness(individuo)
    
    ranking(populacao, 0, len(populacao)-1)
    populacao = selecao(populacao)
    
    if(tamInicial - len(populacao) > 0):
        auxPop = gerar_populacao(tamInicial - len(populacao))
        
        for i, individuo in enumerate(auxPop, 1):
            individuo["fitness"] = fitness(individuo)
        populacao += auxPop
    
    ranking(populacao, 0, len(populacao)-1)
   
    for i, individuo in enumerate(populacao, 1):
        
        print(f"\n--- Individuo {i} ---")
        for key, value in individuo.items():
            print(f"{key}: {value:.2f}")
        
        print(f'Fitness Score: {individuo["fitness"]*100:.7f}')
