salaries = []
salary_bonus = []


while True:
    salary = float(input('How much is the employees salary? '))


    if salary == 0:
        break


    salaries.append(salary)

    
    if salary >= 500:
        salary_bonus.append(salary * 0.2)
    else:
        salary_bonus.append(100)


print()
print('Projection of Allowance Spending')
print('=' * 32)


for salary in salaries:
    print(f'Salary: R$ {salary:.2f}')

print()

print(f'{"Salary":>12}', f"{'Bonus':>16}")
for k, v in enumerate(salaries):
    print(f'Salary: R$ {v:>8.2f} - R$ {salary_bonus[k]:.2f}')

print()
print(f'{len(salaries)} employees were sued')
print(f'Total spent on allowances: R$ {sum(salary_bonus):.2f}')
print(f'Minimum amount paid to {salary_bonus.count(100)} employees')
print(f'Highest amount of bonus paid: R$ {max(salary_bonus):.2f}')