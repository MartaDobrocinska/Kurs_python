def leap():
    """Checks whether given year is a leap year"""
    while True:
        year = (input("Podaj rok: "))
        try:
            int(year)
            break
        except ValueError:
            print("Nieprawidłowe dane, podaj rok jako wartość liczbową.")
    if int(year) % 4 == 0 and int(year) % 100 != 0:
        print("Podany rok", year, "jest przestępny.")
    elif int(year) % 400 == 0:
        print("Podany rok", year, "jest przestępny.")
    else:
        print("Podany rok", year, "nie jest przestępny.")
