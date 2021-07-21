# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a, b, c = [int(i) for i in input("Enter three numbers to compare -> ").split()]

if b < a < c or c < a < b:
    print(f'The middle number is : {a}')
elif a < b < c or c < b < a:
    print(f'The middle number is : {b}')
else:
    print(f'The middle number is : {c}')
