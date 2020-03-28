def cels_to_fahr():
    """converts celsius degrees to fahrenheit"""
    while True:
        celsius = input("Podaj temperaturę w stopniach Celsjusza: ")
        try:
            int(celsius)
            break
        except ValueError:
            try:
                float(celsius)
                break
            except ValueError:
                print("Nieprawidłowe dane, podaj temperaturę jako wartość liczbową.")
    print('''Wzór na przeliczanie stopni Celsjusza na stopnie Fahrenheita:
    [\u00b0F] = [\u00b0C] * 9/5 + 32''')
    print("Podana temperatura przeliczona na stopnie Fahnrenheita: ", end="")
    print(float(celsius) * 9 / 5 + 32)
