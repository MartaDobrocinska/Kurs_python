def div_all_3(dividend, divisors):
    """Checks whether number is divisible by all three given numbers"""
    if dividend % int(divisors[0]) == 0 and dividend % int(divisors[1]) == 0 and dividend % int(divisors[2]) == 0:
        print("Podana liczba jest podzielna przez ", divisors)
    else:
        print("Podana liczba nie jest podzielna przez ", divisors)


while True:
    number = (input("Podaj liczbę: "))
    try:
        int(number)
        break
    except ValueError:
        try:
            float(number)
            break
        except ValueError:
            print("Nieprawidłowe dane, podaj wartość liczbową.")
div_all_3(float(number), [3, 5, 7])
