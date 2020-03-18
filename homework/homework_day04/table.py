def table(data):
    """Prints a given list in a table format"""
    longest = len(max(data, key=len))
    top_bottom = ("+" + "-" + ("-" * longest)) * len(data) + "+"
    top_bottom_30 = ("+" + ("-" * 35)) * len(data) + "+"
    if longest <= 30:
        print(top_bottom)
        for i in data:
            spaces = longest - len(i)
            print("|" + i + (spaces * " ") + " ", end="")
        print("|\n" + top_bottom)
    else:
        print(top_bottom_30)
        for i in data:
            spaces_30 = 34 - len(i)
            if len(i) > 30:
                print("| " + i[0:31] + "...", end="")
            else:
                print("|" + i + (spaces_30 * " ") + " ", end="")
        print("|\n" + top_bottom_30)


cells = ["2345", "34534567654", "234567"]
table(cells)
