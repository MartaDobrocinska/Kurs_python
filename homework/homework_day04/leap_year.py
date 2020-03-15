def leap(date):
    """Checks whether given year is a leap year"""
    if date % 4 == 0 and date % 100 != 0:
        print("Podany rok", date, "jest przestępny.")
    elif date % 400 == 0:
        print("Podany rok", date, "jest przestępny.")
    else:
        print("Podany rok", date, "nie jest przestępny.")


while True:
    year = (input("Podaj rok: "))
    try:
        int(year)
        break
    except ValueError:
        print("Nieprawidłowe dane, podaj rok jako wartość liczbową.")
leap(int(year))
