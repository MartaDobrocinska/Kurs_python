def fahr_to_cels():
    """converts fahrenheit degrees to celsius"""
    while True:
        f = input("Podaj temperaturę w stopniach Fahrenheita: ")
        try:
            int(f)
            break
        except ValueError:
            try:
                float(f)
                break
            except ValueError:
                print("Nieprawidłowe dane, podaj temperaturę jako wartość liczbową.")
    print('''Wzór na przeliczanie stopni Fahrenheita na stopnie Celsjusza:
    [\u00b0C] = ([\u00b0F] - 32) / 1.8''')
    print("Podana temperatura przeliczona na stopnie Celsjusza: ", end="")
    print(float(f) * 9 / 5 + 32)
