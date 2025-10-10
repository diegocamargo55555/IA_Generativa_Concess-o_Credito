import random
import math
from suport import ranges


def cruzamento(individuo1, individuo2):
    filho = {}
    for key in ranges.keys():
        filho[key] = random.choice([individuo1[key], individuo2[key]])
    return filho

def mult_cruzamentos(populacao):
    filhos = []
    for i in range(round(len(populacao)*0.7)):
        filho = cruzamento(random.choice(populacao), random.choice(populacao))
        filhos.append(filho)
    return filhos
    

