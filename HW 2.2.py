# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

n = int(input("Enter a natural number -> "))
even_numbers = 0
odd_numbers = 0
while n > 0:
    if n%2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1
    n = n//10
print(f'Quantity of even_numbers = {even_numbers}')
print(f'Quantity of odd_numbers = {odd_numbers}')



