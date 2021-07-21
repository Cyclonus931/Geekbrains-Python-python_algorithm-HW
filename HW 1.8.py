# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

year = int(input("Enter the year to check -> "))

if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print("It's a regular year")
else:
    print("It's an intercalary year")
