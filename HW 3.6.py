# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint

arr = []
for i in range(10):
    j = randint(0, 20)
    arr.append(j)
print(arr)
minimum = 0
maximum = 0
for j in range(len(arr)):
    if arr[j] < arr[minimum]:
        minimum = j
    elif arr[j] > arr[maximum]:
        maximum = j
if minimum > maximum:
    b = maximum
    maximum = minimum
    minimum = b


s_u_m = 0
for i in range(minimum+1, maximum):
    s_u_m = s_u_m + arr[i]
print(s_u_m)
