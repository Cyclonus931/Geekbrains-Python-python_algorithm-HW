# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

arr = []
for i in range(10):
    j = randint(0, 20)
    arr.append(j)
print(f'array before swap - {arr}')
minimum = 0
maximum = 0
for j in range(len(arr)):
    if arr[j] < arr[minimum] :
        minimum = j
    elif arr[j] > arr[maximum]:
        maximum = j
b = arr[maximum]
arr[maximum] = arr[minimum]
arr[minimum] = b
print(f'array after swap  - {arr}')
print(f'min - {arr[minimum]} | max - {arr[maximum]}')

