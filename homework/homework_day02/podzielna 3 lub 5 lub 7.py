liczba = int(input("Podaj liczbę: "))
if liczba % 3 == 0:
    print("Podana liczba",liczba, "jest podzielna przez 3.")
if liczba % 5 == 0:
    print("Podana liczba", liczba, "jest podzielna przez 5.")
if liczba % 7 == 0:
    print("Podana liczba", liczba, "jest podzielna przez 7.")
if liczba % 3 != 0 and liczba % 5 !=0 and liczba % 7 != 0:
    print("Podana liczba",liczba,"nie jest podzielna przez 3, 5 ani 7.")