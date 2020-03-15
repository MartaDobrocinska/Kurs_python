pytanie1 = input("Podaj wysokość prostokąta: ")
wysokosc = int(pytanie1)
pytanie2 = input("Podaj szerokość prostokąta: ")
szerokosc = int(pytanie2)
srodek = "|" + (" " * szerokosc) + "|\n"
print("+" + ("-" * szerokosc) + "+")
print(wysokosc * srodek, end = "")
print("+" + ("-"*szerokosc) + "+")

# for user in range(0, wysokosc):
#     print("|"," "*szerokosc,"|")
# print("+",("-"*szerokosc),"+")
