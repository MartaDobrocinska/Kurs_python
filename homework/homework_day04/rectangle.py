def rectangle():
    """Draws a rectangle of a given height and width"""
    while True:
        width = (input("Podaj szerokość prostokąta: "))
        try:
            int(width)
            break
        except ValueError:
            print("Nieprawidłowe dane, podaj szerokość prostokąta jako liczbę całkowitą.")
    while True:
        height = (input("Podaj wysokość prostokąta: "))
        try:
            int(height)
            break
        except ValueError:
            print("Nieprawidłowe dane, podaj wysokość prostokąta jako liczbę całkowitą.")
    print("+" + ("-" * int(width)) + "+")
    middle = "|" + (" " * int(width)) + "|\n"
    for user in range(0, int(height)):
        print(middle, end="")
    print("+" + ("-" * int(width)) + "+")
