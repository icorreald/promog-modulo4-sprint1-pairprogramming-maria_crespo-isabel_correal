import pandas as pd
import numpy as np
import re

def duraciones(linea):   
    numeros = re.findall(r'\d+', linea)

    numeros_enteros = [int(numero) for numero in numeros]

    if len(numeros_enteros) == 2:
        resultado = float((numeros_enteros[0] + (numeros_enteros[1] / 100)) * 60)
        return resultado
    
    elif len(numeros_enteros) == 1:
        resultado = int(numeros_enteros[0])
        return resultado
    else:
        return np.nan

def rating(valor):
     return valor.replace('-', '').replace('(', '').replace(')', '').replace('  ', ' ').lower().strip().replace('r  17+', 'r17+')

df[['premiered', 'ended']] = df['Aired'].str.split(" to ", expand=True)