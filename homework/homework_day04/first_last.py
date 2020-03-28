def first_last():
    """gives first and last digits of a given number"""
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
    print("Ilość cyfr: ", len(number))
    print("Pierwsza cyfra:", number[0])
    print("Ostatnia cyfra:", number[-1])
