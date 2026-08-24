import time

def processar_pagamento(valor: float)-> bool:
    if valor <= 0:
        return False

    #Simula a latencia de rede ou comunicacao com API exrterna
    time.sleep(0.05)
    return True