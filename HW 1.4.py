# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.


from random import random

print("Random integer generator!!!")
symbol1 = int(input("Enter the start integer of the range -> "))
symbol2 = int(input("Enter the last integer of the range -> "))
n = int(random() * (symbol2 - symbol1 + 1)) + symbol1
print(n)

print("Random number generator!!!")
symbol1 = float(input("Enter the start number of the range -> "))
symbol2 = float(input("Enter the last number of the range -> "))
n = random() * (symbol2 - symbol1) + symbol1
print(round(n, 2))

print("Random symbol generator!!!")
symbol1 = ord(input("Enter the start symbol of the range -> "))
symbol2 = ord(input("Enter the last symbol of the range -> "))
n = int(random() * (symbol2 - symbol1 + 1)) + symbol1
print(chr(n))


