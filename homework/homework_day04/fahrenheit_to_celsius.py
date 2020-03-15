def fahr_to_cels(fahrenheit):
    """converts fahrenheit degrees to celsius"""
    print(fahrenheit * 9 / 5 + 32)


while True:
    fahrenheit = input("Podaj temperaturę w stopniach Fahrenheita: ")
    try:
        int(fahrenheit)
        break
    except ValueError:
        try:
            float(fahrenheit)
            break
        except ValueError:
            print("Nieprawidłowe dane, podaj temperaturę jako wartość liczbową.")
print('''Wzór na przeliczanie stopni Fahrenheita na stopnie Celsjusza:
[\u00b0C] = ([\u00b0F] - 32) / 1.8''')
print("Podana temperatura przeliczona na stopnie Celsjusza: ", end="")
fahr_to_cels(float(fahrenheit))
