# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9

res_list = [0] * 8

for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            res_list[j - 2] += 1
i = 2
for n in res_list:
    print(f'{i} - {n}')
    i += 1
