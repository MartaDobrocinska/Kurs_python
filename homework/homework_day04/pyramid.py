def pyramid(height):
    """Draws a pyramid with a given number of rows"""
    for row in range(height):
        print(' ' * (height - row - 1) + '#' * (2 * row + 1))


while True:
    rows = (input("Podaj wysokość piramidy: "))
    try:
        int(rows)
        break
    except ValueError:
        print("Nieprawidłowe dane, podaj wysokość piramidy jako liczbę całkowitą.")
pyramid(int(rows))
