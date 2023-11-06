# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:23:52 2023

@author: student
"""

def sprawdź_czy_parzysta(liczba):
    if liczba % 2 == 0:
        return True
    else:
        return False

sprawdzana_liczba = 10
wynik = sprawdź_czy_parzysta(sprawdzana_liczba)

if wynik:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")