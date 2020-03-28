def div_all_3():
    """Checks whether number is divisible by 3, 5 and 7"""
    while True:
        dividend = (input("Podaj liczbę: "))
        try:
            int(dividend)
            break
        except ValueError:
            try:
                float(dividend)
                break
            except ValueError:
                print("Nieprawidłowe dane, podaj wartość liczbową.")
    if float(dividend) % 3 == 0 and float(dividend) % 5 == 0 and float(dividend) % 7 == 0:
        print("Podana liczba jest podzielna przez 3, 5 i 7.")
    else:
        print("Podana liczba nie jest podzielna przez 3, 5 i 7.")
