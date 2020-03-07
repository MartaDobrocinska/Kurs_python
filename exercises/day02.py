#komentarz - co ta funkcja robi?
#komentarz do kilku linijek - zaznaczenie, ctrl+/

#imie = input("Jak masz na imie? ")
#nazwisko = "Dobrocinska"
#print(imie + '\n\n\n' + nazwisko)

#'\n\n\n' = 3 * '\n'

#print(imie + '\n\t' + nazwisko)


#wynik_dzialania = imie.capitalize()
#print(wynik_dzialania)

liczba_1 = 123
liczba_2 = 4.5
liczba_3 = int("1")
liczba_4 = "Ala"
zmienna_1 = "Ala"
zmienna_2 = " ma kota"

#print(liczba_1 / liczba_3)
#print(liczba_1 * liczba_4)
#print(zmienna_1 + zmienna_2)

zdanie = "\nowy folder \tatry"
#ścieżka do pliku c:\\documents\nowy folder\tatry
sciezka_do_pliku = "c:\\\documents\\nowy folder\\tatry"
#\ escapowanie znaku
#albo przedrostek r(raw) - bez interpretacji
sciezka_do_pliku = r"c\\documents\nowy folder ..."
# print(zdanie)
# print(sciezka_do_pliku)

#zmienna = input("Wpisz coś: ")
#typ = type(zmienna)
#print(typ)
#wszystko co przychodzi od użytkownika jest stringiem

#int(parametr) zamienia parametr na int
#str(parametr) zamienia parametr na string

#wartosc1 = input("Podaj liczbę 1 ")
#wartosc2 = input("Podaj liczbę 2 ")

#liczba_1 = float(wartosc1)
#liczba_2 = float(wartosc2)

#print(liczba_1 + liczba_2)

#print(float(wartosc1) + float(wartosc2))

#indeksowanie
#nazwisko = "Kowalski"
#            01234567
#nazwisko[0] -> K
#nazwisko[1] -> o

zdanie = "Ala ma kota."
#print(zdanie[1:8])   #przedział do 8 bez 8
#print(zdanie[1:8:2]) #od l do k co drugi parametr -> trzeci parametr = skok
#print(len(zdanie[1:8:2]))
#print(zdanie[1:-8])
#print(zdanie[-1])
dlugosc = len(zdanie)
#print(zdanie[dlugosc-1])

#blok kodu
#wcięcia - standard: 4 spacje

ostatni_znak = zdanie[-1]

if ostatni_znak == '!':
    print("Nie krzycz na mnie")
else:
    print("Dziękuję.")