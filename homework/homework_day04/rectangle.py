def rectangle(width, height):
    """Draws a rectangle of a given height and width"""
    print("+" + ("-" * width) + "+")
    middle = "|" + (" " * width) + "|\n"
    for user in range(0, height):
        print(middle, end="")
    print("+" + ("-" * width) + "+")


while True:
    user_width = (input("Podaj szerokość prostokąta: "))
    try:
        int(user_width)
        break
    except ValueError:
        print("Nieprawidłowe dane, podaj szerokość prostokąta jako liczbę całkowitą.")
while True:
    user_height = (input("Podaj wysokość prostokąta: "))
    try:
        int(user_height)
        break
    except ValueError:
        print("Nieprawidłowe dane, podaj wysokość prostokąta jako liczbę całkowitą.")
rectangle(int(user_width), int(user_height))
