# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:34:12 2023

@author: student
"""

def sprawdź_czy_występuje_wartość(lista, wartość):
    if wartość in lista:
        return True
    else:
        return False

lista_liczb = [1, 2, 3, 4, 5]
szukana_wartość = 2
wynik = sprawdź_czy_występuje_wartość(lista_liczb, szukana_wartość)
print(wynik)