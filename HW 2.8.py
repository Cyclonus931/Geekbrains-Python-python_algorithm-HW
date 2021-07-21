# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

digit = int(input("What digit do you want to count? -> "))
quantity = int(input("How many numbers? -> "))
count = 0
for i in range(1, quantity + 1):
    m = int(input(f'Number {i} -> '))
    while m > 0:
        if m % 10 == digit:
            count += 1
        m = m // 10

print(f'There were {count} digits - "{digit}"')
