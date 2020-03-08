liczba = int(input("Podaj liczbę: "))
if liczba % 3 == 0 and liczba % 5 ==0 and liczba % 7 == 0:
    print("Podana liczba",liczba,"jest podzielna przez 3, 5 i 7.")
else:
    print("Podana liczba",liczba,"nie jest podzielna przez 3 i 5 i 7.")
