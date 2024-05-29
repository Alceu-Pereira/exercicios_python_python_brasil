value_per_hour = input('How much do you gain per hour worked? ')
hour_per_month = input('How many hours do you work per month? ')


gross_salary = float(value_per_hour) * float(hour_per_month)
net_salary = float(gross_salary)

tax_ir = 0


SYNDICATE = 0.03


fgts = 0.11 * gross_salary


inss = 0.1 * gross_salary



if gross_salary <= 900:
    tax_ir = 0

elif 900 < gross_salary <= 1500:
    tax_ir = 5
    net_salary = float(gross_salary) - float(gross_salary * (tax_ir / 100)) - inss

elif 1500 < gross_salary <= 2500:
    tax_ir = 10
    net_salary = float(gross_salary) - float(gross_salary * (tax_ir / 100)) - inss

else:
    tax_ir = 20
    net_salary = float(gross_salary) - float(gross_salary * (tax_ir / 100)) - inss


padding = 30

print(f'Salário Bruto: (R$ {float(value_per_hour):.2f} * {float(hour_per_month):.0f}) {": R$":>{padding}} {gross_salary:>8.2f}')
print(f'(-) IR ({tax_ir} %) {": R$":>{padding + 18}} {float((tax_ir / 100) * gross_salary):>8.2f}')
print(f'(-) INSS (10 %) {": R$":>{padding + 15}} {(0.1 * gross_salary):>8.2f}')
print(f'FGTS (11 %) {": R$":>{padding + 19}} {(fgts):>8.2f}')
print(f'Total de descontos {": R$":>{padding + 12}} {(float((tax_ir / 100) * gross_salary) + inss):>8.2f}')
print(f'Salário líquido {": R$":>{padding + 15}} {net_salary:>8.2f}')
