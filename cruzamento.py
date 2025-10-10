import random
from suport import ranges


def cruzamento(individuo1, individuo2):
    filho = {}
    for key in ranges.keys():
        filho[key] = random.choice([individuo1[key], individuo2[key]])
    return filho

def mult_cruzamentos(individuo1, individuo2, n):
    filhos = []
    for _ in range(n):
        filhos.append(cruzamento(individuo1, individuo2))
    return filhos

