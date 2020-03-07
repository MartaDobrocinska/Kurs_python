fahrenheit = input("Podaj temperaturę w stopniach Fahrenheita ")
wzor = '''Wzór na przeliczanie stopni Fahrenheita na stopnie Celsjusza:
[\u00b0C] = ([\u00b0F] - 32) / 1.8'''
if type(fahrenheit) == int:
    temperatura = int(fahrenheit)
else:
    temperatura = float(fahrenheit)
print()
print(wzor)
print()
krok1 = temperatura - 32
print("Działanie 1: ",fahrenheit, "- 32 =", krok1)
wynik_krok1 = temperatura - 32
krok2 = krok1 / 1.8
print("Działanie 2: ",wynik_krok1," / 1.8 =", krok2)
print()
print("Wynik - temperatura w stopniach Celsjusza: ",(temperatura - 32) / 1.8)