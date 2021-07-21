# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

letter_number = int(input("Enter the letter number -> "))
print(f'Number "{letter_number}" is equal to letter "{chr(letter_number + ord("a") - 1)}"')

