# 4. Определить, какое число в массиве встречается чаще всего.


from random import randint

arr = []
for i in range(10):
    j = randint(0, 5)
    arr.append(j)

print(arr)

number = 0
max_quantity = 1

for i in range(len(arr)):
    quantity = 1
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            quantity += 1
        if quantity > max_quantity:
            max_quantity = quantity
            number = arr[i]


print(f'There is number "{number}" - {max_quantity} times in this array')
