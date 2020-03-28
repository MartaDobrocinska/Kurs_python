def pyramid():
    """Draws a pyramid with a given number of rows"""
    while True:
        height = (input("Podaj wysokość piramidy: "))
        try:
            int(height)
            break
        except ValueError:
            print("Nieprawidłowe dane, podaj wysokość piramidy jako liczbę całkowitą.")
    for row in range(int(height)):
        print(' ' * (int(height) - row - 1) + '#' * (2 * row + 1))
