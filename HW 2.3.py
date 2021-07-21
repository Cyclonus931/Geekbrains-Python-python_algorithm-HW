# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

n = (int(input("Enter the number -> ")))

new_n = 0
while n > 0:
    new_n = new_n * 10 + n % 10
    n = n // 10
print(new_n)


def recursion(n):
    if n in range(0, 9):
        return n
    if n > 9:
        return str(n % 10) + str(recursion(n // 10))


print(recursion(1234))
# print(recursion(int(input("Enter the number -> "))))
