def lists_merge(list_1, list_2):
    """Multiplies elements from two lists and then adds the results up"""
    list_3 = []
    for num1, num2 in zip(list_1, list_2):
        list_3.append(num1 * num2)
    result = sum(list_3)
    print("Liczba w systemie dziesiętnym: ", result)


question = (input("Podaj 6-znakową liczbę w systemie binarnym: "))
binary = [int(question[0]), int(question[1]), int(question[2]), int(question[3]), int(question[4]), int(question[5])]
multipliers = [32, 16, 8, 4, 2, 1]
lists_merge(binary, multipliers)
