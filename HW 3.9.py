# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы


from random import randint

column = 5
row = 5
a = []
for i in range(row):
    b = []
    for j in range(column):
        z = randint(0, 100)
        b.append(z)
        print(f'{z} | ', end='')
    a.append(b)
    print()

mx = -1
for j in range(column):
    mn = 100
    for i in range(row):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print("The maximal element among the minimal elements of the columns of the matrix: ", mx)