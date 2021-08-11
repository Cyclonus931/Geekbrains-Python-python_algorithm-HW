# Пользователь вводит данные о количестве предприятий,  их наименования и прибыль за квартал для каждого.
# Программа должна определить среднюю прибыль и  вывести наименования предприятий, чья прибыль выше среднего.
# Отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple

QUARTERS = 4
Company = namedtuple('Company', ['name', 'quarters', 'profit'])
all_companies = set()

num = int(input("Enter the number of companies: "))
total_profit = 0
for i in range(1, num + 1):
    profit = 0
    quarters = []
    name = input(f'Enter the company name {i}: ')

    for j in range(QUARTERS):
        quarters.append(int(input(f'Profit for {j + 1} quater: ')))
        profit += quarters[j]

    comp = Company(name=name, quarters=tuple(quarters), profit=profit)

    all_companies.add(comp)
    total_profit += profit

average = total_profit / num

print(f'\nAverage profit = {average}')


print(f'\nCompany with profit higher then average:')
for comp in all_companies:
    if comp.profit > average:
        print(f'Company {comp.name} earned {comp.profit}')


print(f'\nCompany with profit lower then average:')
for comp in all_companies:
    if comp.profit < average:
        print(f'Company {comp.name} earned  {comp.profit}')