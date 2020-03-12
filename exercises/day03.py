## Formatowanie ##

# tytul = "Książka pt.: \"Kot w butach\"."
# tytul = 'Książka pt.: "Kot w butach".'
# print(tytul)

# liczba = 2.3
# liczba_2 = 4.5
# print(f'Wprowadziłeś liczbę: {liczba}')
#
# print('Wprowadziłeś liczbę: {}, {a}, {a}'.format(liczba, a=liczba_2))

## range() ## (typ niemutowalny; iterowalny)

# range(3) -> jeden parametr = ilość elementów
# range(3)
# <0, 1, 2>
# range(4, 8) -> dwa parametry = od 4 do 8 (bez 8)
# range(0, 10, 3) -> trzy parametry = od, do, skok (-> można ujemny)

## lista ## (typ mutowalny)
# lista1 = [1,2,3]
# lista2 = [1,'dwa',3.0]
# lista3 = list(range(2,5))

zestaw_liczb = range(0, 10000000)
# print(zestaw_liczb)

#lazy loading - element jest wyliczany dopiero w momencie żądania - nie jest przechowywany w pamięci

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  -> w nawiasach [] jest indeks (zawsze int)
# print(lista)
# lista_2 = list('dwa') #element iterowalny
# print(lista_2)
# lista_3 = ['dwa'] #def kolejne elementy
# print(lista_3)

# lista_4 = list(range(0, 10))
# print(lista_4)

lista_5 = ['zero', 1, 'trzeci', 'dom123']       #kolejność w liście zachowana -> dopóki nie zmodyfikujemy
# print(lista_5[::-1])

lista_5[1] = 'jeden'

# print(zestaw_liczb[23] == 23)
# print(zestaw_liczb[23] == 25)

##dodawanie

lista_5.append('nowy element')
lista_5.append('kolejny')
lista_5.append(['jeszcze', 'jeden'])

##usuwanie

# del(lista_5[0])
# if 'dom123' in lista_5:
#     lista_5.remove('dom123')
#     print("Element usunięty.")
# elif 'dom' in lista_5:
#     lista_5.remove('dom')
#     print("Element usunięty.")
# else:
#     print("Nie znaleziono elementu.")

# print(lista_5)

##listy zagnieżdżone

# lista = [[1,2,3],[4,5,6],[7,8,9]]
# print(lista[1][2])  # -> 6

## krotka (tuple) ## (niemutowalny typ danych, iterowalny) -> nawiasy zwykłę ()

krotka1 = ('jeden', 'dwa', 'trzy')

## rozpakowywanie ##

a, b, c = krotka1

# print(krotka1)
# print(type(krotka1))
# print(len(krotka1))
# print(krotka1[0])

## Pętle ##

#1. pętla while
# kod wykonuje się tak długo, dopóki spełniona jest wartość logiczna
# ! dać szansę na przerwanie pętli - warunek musi kiedyś być False
# a) pass: nic nie robi (-> żeby składnia się zgadzałą)
# b) continue: pominięcie iteracji
# c) break: przerwanie pętli

# iteracja = 1 obrót pętli

# czy_kontynuowac = "T"
# while czy_kontynuowac == "T":
#    print(".")
#    czy_kontynuowac = input("Czy kontynuować [T/N]? ")

# licznik = 0
# while licznik <= 10:
#     licznik += 1  #licznik = licznik + 1
#     if licznik in [5, 8]:
#         continue
#     print(licznik)
# print("Koniec")

#2. pętla for

#for wykonuje się tyle razy, ile jest elementów w zbiorze
# tak samo jak w while: pass, continue, break

zdanie = "Ala ma kota"

# for litera in zdanie:                       # litera = ostatnia wartość z pętli == "a"
#     if litera in ["a", "A"]:
#         continue
#     print(litera, end = "")

for i in range(0, 100, 2):
    print(i)