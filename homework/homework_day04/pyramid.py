def pyramid(height):
    """Draws a pyramid with a given number of rows"""
    for row in range(height):
        print(' ' * (height - row - 1) + '#' * (2 * row + 1))


pyramid(3)
