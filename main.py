import random

ranges = {
    "serasa": (0, 1000),
    "renda": (0, 40000),
    "tempo_empregado": (0, 120),
    "limite": (0, 2.5),
    #"limite": (10, 70000, float),
    "patrimonio": (0, 2000000),
    "numero_cartoes": (0, 5),
    "idade": (0, 120),
    "historico_inadimplencia": (0, 60),
    "renda_ocupada": (0, 1), # como a gente ia fazer msm
}

def fitness(individuo):
    serasa = individuo["serasa"] / 1000
    renda = individuo["renda"] / 40000
    tempo_empregado = individuo["tempo_empregado"] / 120
    limite = individuo["limite"] / 2.5
    patrimonio = individuo["patrimonio"] / 2000000
    numero_cartoes = individuo["numero_cartoes"] / 5
    idade = individuo["idade"] / 120
    historico_inadimplencia = individuo["historico_inadimplencia"] / 60
    renda_ocupada = (individuo["renda_ocupada"] + 1)
    
    return (serasa * 0.27 + renda* 0.22 + tempo_empregado* 0.17 + limite* 0.18 + patrimonio* 0.1 + numero_cartoes* 0.05 + idade* 0.03 - historico_inadimplencia* 0.25 - renda_ocupada* 0.20)


def gerar_individuo():
    individuo = {}
    inteiros = {"serasa", "tempo_empregado", "numero_cartoes", "idade", "historico_inadimplencia"}
    for key, (min_val, max_val) in ranges.items():
        if key in inteiros:
            individuo[key] = random.randint(min_val, max_val)
        else:
            individuo[key] = random.uniform(min_val, max_val)
    return individuo

def gerar_populacao(n):
    return [gerar_individuo() for _ in range(n)]

populacao = gerar_populacao(100)

for i, individuo in enumerate(populacao, 1):
    print(f"\n--- Individuo {i} ---")
    for key, value in individuo.items():
        print(f"{key}: {value:.2f}")
    
    score = fitness(individuo)
    print(f"Fitness Score: {score:.4f}")
