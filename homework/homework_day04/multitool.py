import random
import homework.homework_day04.rectangle as rectangle
import homework.homework_day04.pyramid as pyramid
import homework.homework_day04.change as change
import homework.homework_day04.fahrenheit_to_celsius as f_to_c
import homework.homework_day04.celsius_to_fahrenheit as c_to_f
import homework.homework_day04.bi_to_dec as bi_to_dec
import homework.homework_day04.circle_area as circle
import homework.homework_day04.even_odd as even_odd
import homework.homework_day04.first_last as first_last
import homework.homework_day04.divisible_by_either as div_either
import homework.homework_day04.divisible_by_all as div_all
import homework.homework_day04.leap_year as leap
import homework.homework_day04.dog as dog
import homework.homework_day06.data_import as data_import


def exit_multi():
    print('Koniec')


def random_multi():
    options = [*funkcje]
    result = str(random.choice(options))
    print(funkcje[result]['nazwa'])
    funkcje[result]['call']()


def menu():
    print('''Witaj w Multitool Python Program by iSA - wersja beta ;)
Wybierz program który cię interesuje:''')
    for index, funkcja in funkcje.items():
        print(index, funkcja['nazwa'])


funkcje = {'1':  {'nazwa': 'Rysowanie prostokąta o zadanych parametrach', 'call': rectangle.rectangle},
           '2':  {'nazwa': 'Rysowanie piramidy o określonej wysokości', 'call': pyramid.pyramid},
           '3':  {'nazwa': 'Rozmienianie pieniędzy', 'call': change.change},
           '4':  {'nazwa': 'Przeliczanie stopni Fahrenheita na Celsjusza', 'call': f_to_c.fahr_to_cels},
           '5':  {'nazwa': 'Przeliczanie stopni Celsjusza na Fahrenheita', 'call': c_to_f.cels_to_fahr},
           '6':  {'nazwa': 'Przeliczanie liczby z systemu binarnego na dziesiętny', 'call': bi_to_dec.binary},
           '7':  {'nazwa': 'Kalkulator pola powierzchni koła', 'call': circle.circ_area},
           '8':  {'nazwa': 'Liczba parzysta czy nieparzysta?', 'call': even_odd.even_odd},
           '9':  {'nazwa': 'Znajdź pierwszą i ostatnią cyfrę podanej liczby', 'call': first_last.first_last},
           '10':  {'nazwa': 'Czy podana liczba jest podzielna przez 3, 5 lub 7?', 'call': div_either.div_by_either},
           '11':  {'nazwa': 'Czy podana liczba jest podzielna przez 3, 5 i 7?', 'call': div_all.div_all_3},
           '12':  {'nazwa': 'Czy podany rok jest przestępny?', 'call': leap.leap},
           '13':  {'nazwa': 'Kalkulator wieku psa', 'call': dog.dog},
           '14':  {'nazwa': 'Rysowanie tabeli z pliku Excel', 'call': data_import.data_import},
           'R':  {'nazwa': 'Zaskocz mnie :)', 'call': random_multi},
           'X':  {'nazwa': 'Wyjście z programu', 'call': exit_multi}
           }
menu()
program = input('Co chcesz zrobić? ')
if program == 'r' or program == 'x':
    program = program.capitalize()
else:
    pass
while True:
    try:
        funkcje[program]['call']()
        break
    except:
        print('Nie ma takiego programu')
        program = input('Co chcesz zrobić? ')
