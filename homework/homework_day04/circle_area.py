def circ_area():
    """calculates the area of a circle with the given radius"""
    while True:
        radius = input("Podaj promień koła: r = ")
        try:
            int(radius)
            break
        except ValueError:
            try:
                float(radius)
                break
            except ValueError:
                print("Nieprawidłowe dane, podaj promień jako wartość liczbową.")
    print('''Wzór na pole powierzchni koła:
    P = \u03C0 * r\N{SUPERSCRIPT TWO}''')
    pi = 3.14
    print("P =", pi * float(radius) ** 2)
