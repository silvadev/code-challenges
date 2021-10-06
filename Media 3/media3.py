#!/usr/bin/env python3

"""Média 3

Implementa desafio de código 'Média 3' em Python.
Para mais detalhes consulte o README.md.
"""
__version__ = "1.0"
__author__  = "Ivanildo Silva"
__email__   = "ijsfilho@gmail.com"

# Lê as 4 notas numa lista criada coma função split() e transforma os valores em
# float usando o recurso 'list comprehension'.
n1, n2, n3, n4 = [float(i) for i in input().split()] 

# Como a soma dos pesos é igual a 10, multiplicamos as notas pelo peso indicado
# dentro de uma lista, somar todas as notas com a função sum() e dividir o valor
# por 10 para obter a média das notas.
media = sum([n1*2,n2*3,n3*4,n4*1])/10
print('Media: {:.1f}'.format(media))

if (media >= 7):
    print('Aluno aprovado.')
elif (media < 5):
    print('Aluno reprovado.')
elif (5.0 <= media <= 6.9):
    print('Aluno em exame.')
    n5 = float(input())
    final = (media + n5) / 2
    print('Nota do exame: {:.1f}'.format(n5))

    if (final >= 5):
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado')
    print('Media final: {:.1f}'.format(final))
