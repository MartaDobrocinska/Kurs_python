celsjusz = input("Podaj temperaturę w stopniach Celsjusza ")
wzor = '''Wzór na przeliczanie stopni Celsjusza na stopnie Fahrenheita:
[\u00b0F] = [\u00b0C] * 9/5 + 32'''
if type(celsjusz) == int:
    temperatura = int(celsjusz)
else:
    temperatura = float(celsjusz)
print()
print(wzor)
print()
krok1 = temperatura * 9
print("Działanie 1: ",celsjusz, "* 9 =", krok1)
krok2 = krok1 / 5
print("Działanie 2: ",krok1," / 5 =", krok2)
krok3 = krok2 + 32
print("Działanie 3: ", krok2, "+ 32 =", krok3)
print()
print("Wynik - temperatura w stopniach Fahrenheita: ",temperatura * 9 / 5 + 32)