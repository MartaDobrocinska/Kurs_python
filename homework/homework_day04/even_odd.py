def even_odd(data):
    """checks if a number is even or odd"""
    if int(data) % 2 == 0:
        print("Podana liczba", num, "jest parzysta.")
    else:
        print("Podana liczba", num, "jest nieparzysta.")


while True:
    num = input("Podaj liczbę całkowitą: ")
    try:
        int(num)
        break
    except ValueError:
        print("Nieprawidłowe dane, podaj liczbę całkowitą.")
even_odd(num)