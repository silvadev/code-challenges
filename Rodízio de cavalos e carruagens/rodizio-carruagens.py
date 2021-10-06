#!/usr/bin/env python3

"""Rodízio de cavalos e carruagens

Implementa desafio de código 'Rodízio de cavalos e carruagens' em Python.
Para mais detalhes consulte o README.md.
"""
__version__ = "1.0"
__author__  = "Ivanildo Silva"
__email__   = "ijsfilho@gmail.com"

#Importa a função 're.match()' e inicializa variável 'check' com padrão
#'AAA-0000'.
from re import match
check = '^[A-Z]{3}-[0-9]{4}$'

# Inicializa tupla com dias da semana seguindo índice do término das placas.
days = ('SEXTA', 'SEGUNDA', 'SEGUNDA', 'TERCA', 'TERCA', 'QUARTA', 'QUARTA', 
        'QUINTA', 'QUINTA', 'SEXTA')

# Solicita número de checagens na variável 'n'.
n = int(input())

for i in range(n):
    plate = str(input())

    '''[TERNARY]
    
    print(days[int(plate[-1])] if (match(check, plate)) else 'FALHA')
    '''
    if (match(check, plate)):
        end_plate = int(plate[-1])
        msg = days[end_plate]
    else:
        msg = 'FALHA'
    print(msg)
