def div_3_5_7(num):
    """Checks whether a given number is divisible by 3, 5 and 7"""
    if num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
        print("Podana liczba", num, "jest podzielna przez 3, 5 i 7.")
    else:
        print("Podana liczba", num, "nie jest podzielna przez 3 i 5 i 7.")


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
number = int(input("Podaj liczbę: "))
div_3_5_7(number)
