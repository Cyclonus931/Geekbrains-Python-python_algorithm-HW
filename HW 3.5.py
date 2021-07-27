# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import randint

arr = []
for i in range(10):
    j = randint(-50, 50)
    arr.append(j)

print(arr)

max_negative = -51
el_num = 0
for j in range(len(arr)):
    if 0 > arr[j] > max_negative:
        max_negative = arr[j]
        el_num = j + 1
if max_negative == -51:
    print("There is no negative numbers in the array")
elif max_negative < 0:
    print(f'The maximal negative number - "{max_negative}" and number of its element in the array is - "{el_num}"')
