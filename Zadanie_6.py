# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:37:16 2023

@author: student
"""

def zmodyfikuj_listy(lista1, lista2):
    lista_połączona = lista1 + lista2
    
    lista_bez_duplikatow = list(set(lista_połączona))
    
    lista_podniesiona_do_potęgi = [x**3 for x in lista_bez_duplikatow]
    
    return lista_podniesiona_do_potęgi

lista1 = [9, 8, 7, 6]
lista2 = [3, 4, 5, 6]
wynik = zmodyfikuj_listy(lista1, lista2)
print(wynik)