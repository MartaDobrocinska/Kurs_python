def first_last(num):
    """gives first and last digits of a given number"""
    print("Ilość cyfr: ", len(num))
    print("Pierwsza cyfra:", num[0])
    print("Ostatnia cyfra:", num[-1])


while True:
    number = input("Podaj liczbę: ")
    try:
        int(number)
        break
    except ValueError:
        try:
            float(number)
            break
        except ValueError:
            print("Nieprawidłowe dane, podaj wartość liczbową.")
first_last(number)
