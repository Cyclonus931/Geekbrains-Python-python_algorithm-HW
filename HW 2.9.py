# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

n = int(input("Enter first number -> "))
max_sum = 0
max_num = 0
while n != 0:
    num = n
    s_u_m = 0
    while n > 0:
        s_u_m += n % 10
        n //= 10
    if s_u_m > max_sum:
        max_sum = s_u_m
        max_num = num
    n = int(input("Enter next number , for finish enter '0' -> "))
print(f'number {max_num} has the greatest sum of digits -> {max_sum}')
