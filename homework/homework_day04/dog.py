def dog(age):
    """Calculates dog's age in humar years"""
    if float(age) <= 2:
        print("Wiek psa w 'ludzkich' latach: ", (float(age) * 10.5))
    else:
        print("Wiek psa w 'ludzkich' latach: ", (21 + 4 * (float(age) - 2)))


while True:
    age = input("Podaj wiek psa w latach: ")
    try:
        float(age)
        break
    except ValueError:
        print("Nieprawidłowe dane, podaj wiek psa jako liczbę.")

dog(age)





