# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

first_letter = ord(input("Enter the first letter -> "))
second_letter = ord(input("Enter the second letter -> "))
first_letter = first_letter - ord('a') + 1
second_letter = second_letter - ord('a') + 1
print(f'First letter position : {first_letter}\nSecond letter position : {second_letter}'
      f'\nNumber of characters between letters : {abs(first_letter - second_letter) - 1}')
