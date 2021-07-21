# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ..Количество элементов (n) вводится с клавиатуры.

n = int(input())
element = 1
s_u_m = 0
for i in range(n):
    s_u_m += element
    element /= -2
print(s_u_m)
