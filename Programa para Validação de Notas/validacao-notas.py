#!/usr/bin/env python3

"""Programa para Validação de Notas

Implementa desafio de código 'Programa para Validação de Notas' em Python.
Para mais detalhes consulte o README.md.
"""
__version__ = "1.0"
__author__  = "Ivanildo Silva"
__email__   = "ijsfilho@gmail.com"

def notas_media(x, y):
    media = (x + y) / 2
    print('media = {:.2f}'.format(media))


def notas_validas():
    x = float(input())
    if (0 <= x <= 10):
        return x
    else:
        print('nota invalida')
        return notas_validas()

def notas_calculo():
    k = notas_validas()
    j = notas_validas()
    notas_media(k,j)

if __name__ == '__main__':
    notas_calculo()
    novo_calculo = ''
    while not novo_calculo in ['1', '2']:
        novo_calculo = input('novo calculo (1-sim 2-nao)\n')
        if novo_calculo == '1':
            notas_calculo()
            novo_calculo = ''
