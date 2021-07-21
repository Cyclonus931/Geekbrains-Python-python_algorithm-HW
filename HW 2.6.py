# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.


from random import random

n = round(random() * 100)
i = 1
print("Please guess the number from 0 to 100 ")
while i <= 10:
    u = int(input(str(i) + " try: "))
    if u > n:
        print('The number is too big')
    elif u < n:
        print('The number is too small')
    else:
        print("You're right! Great job!")
        break
    i += 1
else:
    print('You need to try harder! The right answer: ', n)