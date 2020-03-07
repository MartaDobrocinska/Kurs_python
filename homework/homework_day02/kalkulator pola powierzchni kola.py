dane = input("Podaj promień koła: r = ")
wzor = '''Wzór na pole powierzchni koła:
P = \u03C0 * r\N{SUPERSCRIPT TWO}'''
pi = 3.14
if type(dane) == int:
    r = int(dane)
else:
    r = float(dane)
print()
print(wzor)
print("\u03C0 =", pi)
print()
print("P =", pi * r ** 2)