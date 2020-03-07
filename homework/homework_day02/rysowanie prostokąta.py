pytanie1 = input("Podaj wysokość prostokąta: ")
wysokosc = int(pytanie1)
pytanie2 = input("Podaj szerokość prostokąta: ")
szerokosc = int(pytanie2)
print("+",("-"*szerokosc),"+")
for user in range(0, szerokosc):
    print("|"," "*wysokosc,"|")
print("+",("-"*szerokosc),"+")