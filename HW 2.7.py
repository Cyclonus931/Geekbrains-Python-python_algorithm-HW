# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

n = int(input())
right_part = n * (n + 1) // 2
left_part = 0

for i in range(1, n + 1):
    left_part += i

if left_part == right_part:
    print(f'Equality satisfied -> {left_part} = {right_part}')
else:
    print(f'Equality is not satisfied" -> {left_part} != {right_part}')





