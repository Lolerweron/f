#Input pobiera dane z konsoli 
ileKotow = input("Jak wysoka piramide z kotow mam zrobic: ")
#zamiana napisu na liczbe
try:
    ileKotow = int(ileKotow)
except ValueError:
    # tutaj sa instrukcje ktore maja sie uruchomic
    # kiedy dojdzie do Value Error
    print("Program przyjmuje tylko liczby całkowite")
    print('Uruchom ponownie :)')
#type(cos) zwarca typ cosia
print(ileKotow, 'typem jest:', type(ileKotow))

"""
    Termin oddania 26.10.2018
    Zadanie na teraz i jak sie nie uda to do domu -_-

    Napisać program który wypisze w jednej lini tyle
    kotów ile podasz(=^.^=)
    Przykład:
    Wpisujesz: 3
    Wypisuje: (=^.^=)(=^.^=)(=^.^=)
"""

"""
    Zadanie domowe:
    Napisac program który wypisuje schodki z kotów,
    wysokość podajecie w konsoli.
    Przykład:
    Dla 4
    Wypisuje:
    (=^.^=)
    (=^.^=)(=^.^=)
    (=^.^=)(=^.^=)(=^.^=)
    (=^.^=)(=^.^=)(=^.^=)(=^.^=)
"""
