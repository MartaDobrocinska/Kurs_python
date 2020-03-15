def div_by_either(dividend, divisors):
    """checks whether a number is divisible by any of the 3 given numbers"""
    if dividend % divisors[0] == 0:
        print("Podana liczba jest podzielna przez ", divisors[0])
    if dividend % divisors[1] == 0:
        print("Podana liczba jest podzielna przez ", divisors[1])
    if dividend % divisors[2] == 0:
        print("Podana liczba jest podzielna przez ", divisors[2])
    if dividend % divisors[0] != 0 and dividend % divisors[1] != 0 and dividend % divisors[2] != 0:
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
divisors_list = [3, 5, 7]
div_by_either(float(number), divisors_list)
