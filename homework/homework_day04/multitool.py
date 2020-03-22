import random
print('''Witaj w Multitool Python Program by iSA - wersja beta ;)
Wybierz program który cię interesuje:
   1) Rysowanie prostokąta o zadanych parametrach
   2) Rysowanie piramidy o określonej wysokości
   3) Rozmienianie pieniędzy
   4) Przeliczanie stopni Fahrenheita na Celsjusza
   5) Przeliczanie stopni Celsjusza na Fahrenheita 
   6) Przeliczanie liczby z systemu binarnego na dziesiętny
   7) Kalkulator pola powierzchni koła
   8) Liczba parzysta czy nieparzysta?
   9) Znajdź pierwszą i ostatnią cyfrę podanej liczby
   10) Czy podana liczba jest podzielna przez 3, 5 lub 7?
   11) Czy podana liczba jest podzielna przez 3, 5 i 7?
   12) Czy podany rok jest przestępny?
   13) Kalkulator wieku psa
   14) Wybierz program losowo bo nie wiem czego szukam:)
   15) Wyjście z programu''')
question = input("Podaj numer programu: ")
options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
while question not in options:
    print("Nieprawdiłowy numer, podaj numer programu z listy powyżej")
    question = input("Podaj numer programu: ")
if question == "1":
    import homework.homework_day04.rectangle
elif question == "2":
    import homework.homework_day04.pyramid
elif question == "3":
    import homework.homework_day04.change
elif question == "4":
    import homework.homework_day04.fahrenheit_to_celsius
elif question == "5":
    import homework.homework_day04.celsius_to_fahrenheit
elif question == "6":
    import homework.homework_day04.bi_to_dec
elif question == "7":
    import homework.homework_day04.circle_area
elif question == "8":
    import homework.homework_day04.even_odd
elif question == "9":
    import homework.homework_day04.first_last
elif question == "10":
    import homework.homework_day04.divisible_by_either
elif question == "11":
    import homework.homework_day04.divisible_by_all
elif question == "12":
    import homework.homework_day04.leap_year
elif question == "13":
    import homework.homework_day04.dog
elif question == "14":
    choice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    question = str(random.choice(choice))
    if question == "1":
        print("Program 1")
        import homework.homework_day04.rectangle
    elif question == "2":
        print("Program 2")
        import homework.homework_day04.pyramid
    elif question == "3":
        print("Program 3")
        import homework.homework_day04.change
    elif question == "4":
        print("Program 4")
        import homework.homework_day04.fahrenheit_to_celsius
    elif question == "5":
        print("Program 5")
        import homework.homework_day04.celsius_to_fahrenheit
    elif question == "6":
        print("Program 6")
        import homework.homework_day04.bi_to_dec
    elif question == "7":
        print("Program 7")
        import homework.homework_day04.circle_area
    elif question == "8":
        print("Program 8")
        import homework.homework_day04.even_odd
    elif question == "9":
        print("Program 9")
        import homework.homework_day04.first_last
    elif question == "10":
        print("Program 10")
        import homework.homework_day04.divisible_by_either
    elif question == "11":
        print("Program 11")
        import homework.homework_day04.divisible_by_all
    elif question == "12":
        print("Program 12")
        import homework.homework_day04.leap_year
    elif question == "13":
        print("Program 13")
        import homework.homework_day04.dog
elif question == "15":
    print("Koniec")
