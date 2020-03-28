def change():
    print("Kalkulator reszty")
    while True:
        value = input("Podaj kwotę w PLN: ")
        try:
            float(value)
            break
        except ValueError:
            print("Nieprawidłowe dane, podaj kwotę jako wartość liczbową.")
    coins = [5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    values = [": 5 PLN", ": 2 PLN", ": 1 PLN", ": 50 groszy", ": 20 groszy",
              ": 10 groszy", ": 5 groszy", ": 2 grosze", ": 1 grosz"]
    amount = float(value)
    for coin, value in zip(coins, values):
        if amount > 0:
            if amount // coin > 0:
                print(amount // coin, value)
                amount = amount % coin
