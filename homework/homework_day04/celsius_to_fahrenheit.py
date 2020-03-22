# def cels_to_fahr(cel):
#     """converts celsius degrees to fahrenheit"""
#     print(cel * 9 / 5 + 32)
#
#
# while True:
#     celsius = input("Podaj temperaturę w stopniach Celsjusza: ")
#     try:
#         int(celsius)
#         break
#     except ValueError:
#         try:
#             float(celsius)
#             break
#         except ValueError:
#             print("Nieprawidłowe dane, podaj temperaturę jako wartość liczbową.")
# print('''Wzór na przeliczanie stopni Celsjusza na stopnie Fahrenheita:
# [\u00b0F] = [\u00b0C] * 9/5 + 32''')
# print("Podana temperatura przeliczona na stopnie Fahnrenheita: ", end="")
# cels_to_fahr(float(celsius))
import random
choice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
question = random.choice(choice)
print(question)