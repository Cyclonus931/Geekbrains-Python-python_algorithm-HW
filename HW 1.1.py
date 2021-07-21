# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# Линейный алгоритм
number = input("Enter a three-digit number: ")

a = int(number[0])
b = int(number[1])
c = int(number[2])

s_u_m = 0
product = 1


print("Sum of digits of a number -> ", a+b+c)
print("Product of the digits of a number -> ", a*b*c)

# Циклический алгоритм

# number = input("Enter a three-digit number: ")

# for digit in number:
#     s_u_m += int(digit)
#     product *= int(digit)

# print("Sum of digits of a number -> ", s_u_m)
# print("Product of the digits of a number -> ", product)
