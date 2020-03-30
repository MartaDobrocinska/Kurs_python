def binary():
    """Converts a 6 digit binary number into a decimal """
    question = input("Podaj 6-znakową liczbę w systemie binarnym: ")
    while True:
        try:
            int(question, 2) and len(question) == 6
            break
        except:
            print("Podana liczba nie jest 6-znakową liczbą binarną.")
            question = (input("Podaj 6-znakową liczbę w systemie binarnym: "))
    binary = [int(question[0]), int(question[1]), int(question[2]), int(question[3]), int(question[4]),
              int(question[5])]
    multipliers = (32, 16, 8, 4, 2, 1)
    list_3 = []
    for num1, num2 in zip(binary, multipliers):
        list_3.append(num1 * num2)
    result = sum(list_3)
    print("Liczba w systemie dziesiętnym: ", end="")
    print(result)

