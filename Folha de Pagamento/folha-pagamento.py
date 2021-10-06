#!/usr/bin/env python3

"""Folha de Pagamento

Implementa desafio de código 'Folha de Pagamento' em Python.
Para mais detalhes consulte o README.md.
"""
__version__ = "1.0"
__author__  = "Ivanildo Silva"
__email__   = "ijsfilho@gmail.com"

emp_no = int(input())

worked_hours = int(input())

receives_per_worked_hour = float(input())

salary = worked_hours * receives_per_worked_hour

print("NUMBER =", emp_no)
print("SALARY = U$ {:.2f}".format(salary))
