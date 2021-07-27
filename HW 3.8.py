# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.


column = 5
row = 4
a = []
for i in range(row):
    b = []
    last_el = 0
    print(f'{i} row -> ')
    for j in range(column - 1):
        number = int(input())
        last_el += number
        b.append(number)
    b.append(last_el)
    a.append(b)
print(a)
for i in a:
    print(i)