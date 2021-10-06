#!/usr/bin/env python3

"""A Resposta de Theon

Implementa desafio de código 'A Resposta de Theon' em Python.
Para mais detalhes consulte o README.md.
"""
__version__ = "1.0"
__author__  = "Ivanildo Silva"
__email__   = "ijsfilho@gmail.com"

N = int(input())
persons = [int(i) for i in input().split()]
min_person = persons.index(min(persons))+1

print(min_person)
