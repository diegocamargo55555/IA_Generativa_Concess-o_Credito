
import random

ranges = {
    "serasa": (1, 1000),
    "renda": (0, 40000),
    "tempo_empregado": (0, 120),
    "limite": (10, 70000),
    "patrimonio": (0, 2000000),
    "numero_cartoes": (0, 5),
    "idade": (18, 100),
    "historico_inadimplencia": (0, 60),
    "renda_ocupada": (0, 1), 
    "fitness" : (0,1)
}

def limite_porcentagem(limite, renda):
    limiteP = (limite * 100) / renda 
    return limiteP/2.5 if limite < 2.5 else 1

def fitness(individuo):
    serasa = individuo["serasa"] / 1000
    renda = individuo["renda"] / 40000
    tempo_empregado = individuo["tempo_empregado"] / 120
    limite = limite_porcentagem(individuo["limite"], individuo["renda"])
    patrimonio = individuo["patrimonio"] / 2000000
    numero_cartoes = individuo["numero_cartoes"] / 5
    idade = individuo["idade"] / 100
    historico_inadimplencia = individuo["historico_inadimplencia"] / 60
    renda_ocupada = (individuo["renda_ocupada"])
    
    fitness =  (serasa * 0.27 + renda* 0.22 + tempo_empregado* 0.17 + limite* 0.18 + patrimonio* 0.1 + numero_cartoes* 0.05 + idade* 0.03 - historico_inadimplencia* 0.15 - renda_ocupada* 0.10)
    return fitness


def gerar_individuo():
    individuo = {}
    inteiros = {"serasa", "tempo_empregado", "numero_cartoes", "idade", "historico_inadimplencia"}
    for key, (min_val, max_val) in ranges.items():
        if key in inteiros:
            individuo[key] = random.randint(min_val, max_val)
        elif key == "fitness":
            pass
        else:
            individuo[key] = random.uniform(min_val, max_val)
    return individuo

def gerar_populacao(n):
    return [gerar_individuo() for _ in range(n)]

def ranking(A, p, r):
    if p < r:
        q = rankingAux(A, p, r)
        ranking(A, p, q-1)
        ranking(A, q+1, r)

def rankingAux(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j]["fitness"] <= x["fitness"]:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1