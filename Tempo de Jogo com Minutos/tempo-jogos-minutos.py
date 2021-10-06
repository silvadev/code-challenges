#!/usr/bin/env python3

"""Tempo de Jogo com Minutos

Implementa desafio de código 'Tempo de Jogo com Minutos' em Python.
Para mais detalhes consulte o README.md.
"""
__version__ = "1.0"
__author__  = "Ivanildo Silva"
__email__   = "ijsfilho@gmail.com"

from time import strftime, gmtime

hi, mi, hf, mf = map(int, input().split())

# Calcula diferença em segundos.
sh, sm = 3600, 60 # Fator de multiplicação '[sh = horas, sm = minutos]'
ds = (hf*sh + mf*sm) - (hi*sh + mi*sm) # Diferença em segundos

# Converte segundos em horas e minutos.
h, m = map(int, strftime('%H %M', gmtime(ds)).split())

# Se diferença for igual à zero ou maior que 86400 segundos (24 horas),
# adicionamos +24 horas.
if ds == 0 or ds >= 86400:
    h += 24

print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')
