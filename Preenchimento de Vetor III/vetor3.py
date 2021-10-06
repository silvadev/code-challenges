#!/usr/bin/env python3

"""Preenchimento de Vetor III

Implementa desafio de código 'Preenchimento de Vetor III' em Python.
Para mais detalhes consulte o README.md.
"""
__version__ = "1.0"
__author__  = "Ivanildo Silva"
__email__   = "ijsfilho@gmail.com"

n=[float(input())]

for i in range(100):
    print('N[{}] = {:.4f}'.format(i, n[i]))
    if i != 99:
        n.append(n[i]/2)
