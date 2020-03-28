def div_by_either():
    """checks whether a number is divisible by any of the 3 given numbers"""
    while True:
        number = (input("Podaj liczbę: "))
        try:
            int(number)
            break
        except ValueError:
            try:
                float(number)
                break
            except ValueError:
                print("Nieprawidłowe dane, podaj wartość liczbową.")
    if float(number) % 3 == 0:
        print("Podana liczba jest podzielna przez 3.")
    if float(number) % 5 == 0:
        print("Podana liczba jest podzielna przez 5.")
    if float(number) % 7 == 0:
        print("Podana liczba jest podzielna przez 7.")
    if float(number) % 3 != 0 and float(number) % 5 != 0 and float(number) % 7 != 0:
        print("Podana liczba nie jest podzielna przez 3, 5 ani 7.")
