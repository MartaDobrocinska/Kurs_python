def even_odd():
    """checks if a number is even or odd"""
    while True:
        num = input("Podaj liczbę całkowitą: ")
        try:
            int(num)
            break
        except ValueError:
            print("Nieprawidłowe dane, podaj liczbę całkowitą.")
    if int(num) % 2 == 0:
        print("Podana liczba", num, "jest parzysta.")
    else:
        print("Podana liczba", num, "jest nieparzysta.")
