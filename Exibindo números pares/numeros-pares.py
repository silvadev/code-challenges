#!/usr/bin/env python3

"""Exibindo Números Pares
Implementa desafio de código 'Exibindo Números Pares' em Python.
Para mais detalhes consulte o README.md.
"""
__version__ = "1.0"
__author__  = "Ivanildo Silva"
__email__   = "ijsfilho@gmail.com"


num = int(input())

for i in range(2,num+1):
    if ((i % 2) == 0):
        print(i)
