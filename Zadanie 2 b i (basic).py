def pomnoz_przez_2(lista_liczb):
    wynik = []
    for liczba in lista_liczb:
        wynik.append(liczba * 2)
    return wynik

lista_liczb = [1, 2, 3, 4, 5]
wynik = pomnoz_przez_2(lista_liczb)
print(wynik)