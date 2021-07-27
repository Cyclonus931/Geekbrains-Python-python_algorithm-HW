# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import randint

arr = []
for i in range(10):
    j = randint(0, 100)
    arr.append(j)

print(arr)

if arr[0] > arr[1]:
    m1 = 0
    m2 = 1
else:
    m1 = 1
    m2 = 0

for i in range(2, len(arr)):
    if arr[i] < arr[m1]:
        b = m1
        m1 = i
        if arr[b] < arr[m2]:
            m2 = b
    elif arr[i] < arr[m2]:
        m2 = i

print(f'"Minimal element number 1 is "{arr[m1]}"  and its index is "{m1+1}"')
print(f'"Minimal element number 2 is "{arr[m2]}"  and its index is "{m2+1}"')