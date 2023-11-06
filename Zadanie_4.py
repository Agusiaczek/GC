# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:31:21 2023

@author: student
"""

def sprawdź_sume_liczb(x, y, z):
    suma = x + y
    if suma >= z:
        return True
    else:
        return False

liczba1 = 1
liczba2 = 2
liczba3 = 3
wynik = sprawdź_sume_liczb(liczba1, liczba2, liczba3)
print(wynik)