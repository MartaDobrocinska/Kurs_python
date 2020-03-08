rok = int(input("Podaj rok: "))
if rok % 4 == 0 and rok % 100 != 0:
    print("Podany rok",rok,"jest przestępny.")
elif rok % 400 == 0:
    print("Podany rok", rok, "jest przestępny.")
else:
    print("Podany rok",rok,"nie jest przestępny.")
