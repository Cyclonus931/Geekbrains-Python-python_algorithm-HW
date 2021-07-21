# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

print("When '0' is entered, the program will be terminated")

while True:
    operation = input("Enter one of the following math. symbols : '+', '-', '*', '/' -> ")
    if operation == "0":
        break
    if operation in ('+', '-', '*', '/'):
        x = int(input("Enter first number -> "))
        y = int(input("Enter second number -> "))
        if operation == "+":
            print(f'{x} + {y} = {x + y}')
        elif operation == "-":
            print(f'{x} - {y} = {x - y}')
        elif operation == "*":
            print(f'{x} * {y} = {x * y}')
        elif operation == "/":
            if y != 0:
                print(f'{x} / {y} = {x / y}')
            else:
                print("Cannot be divided by zero!")
    else:
        print("Wrong symbol!")

