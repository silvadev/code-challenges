#!/usr/bin/env python3

"""Fibonacci Fácil

Implementa desafio de código 'Fibonacci Fácil' em Python.
Para mais detalhes consulte o README.md.
"""
__version__ = "1.0"
__author__  = "Ivanildo Silva"
__email__   = "ijsfilho@gmail.com"


n = int(input())
fib_list = [0]

if (n > 1):
    n -= 1
    fib_list = [0,1]
    for x in range(1,n):
        num = fib_list[-2]+fib_list[-1]
        fib_list.append(num)

fib_string = ' '.join([str(i) for i in fib_list])
print(fib_string)
