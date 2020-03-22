def lists_merge(list_1, list_2):
    """Multiplies elements from two lists and then adds the results up"""
    list_3 = []
    for num1, num2 in zip(list_1, list_2):
        list_3.append(num1 * num2)
    result = sum(list_3)
    print(result)


while True:
    question = (input("Podaj 6-znakową liczbę w systemie binarnym: "))
    try:
        int(question)
        break
    except ValueError:
        print("Nieprawidłowe dane, podaj wartość liczbową.")
while len(question) != 6:
    print("Podana liczba nie jest 6-znakową liczbą binarną.")
    question = (input("Podaj 6-znakową liczbę w systemie binarnym: "))
options = [1, 0]
binary = [int(question[0]), int(question[1]), int(question[2]), int(question[3]), int(question[4]), int(question[5])]
while False:
    check = all(item in options for item in binary)
    print("Podana liczba nie jest liczbą binarną.")
    question = (input("Podaj 6-znakową liczbę w systemie binarnym: "))
multipliers = [32, 16, 8, 4, 2, 1]
print("Liczba w systemie dziesiętnym: ", end="")
lists_merge(binary, multipliers)
