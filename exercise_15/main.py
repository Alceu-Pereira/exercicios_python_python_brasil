earn_hour = float(input('Quanto você ganha por hora trabalhada? '))
work_hour_month = int(input('Você trabalha quantas horas por mês? '))
total_gross_month = earn_hour * work_hour_month
tax_ir = 0.11 * total_gross_month
tax_inss = 0.08 * total_gross_month
tax_sindcate = 0.05 * total_gross_month
total_neto_month = total_gross_month - tax_ir - tax_inss - tax_sindcate

print(f'Salário BRUTO: R$ {total_gross_month:.2f}')
print(f'Taxa IR: R$ {tax_ir:.2f}')
print(f'Taxa INSS: R$ {tax_inss:.2f}')
print(f'Taxa SINDICATO: R$ {tax_sindcate:.2f}')
print(f'Salário LÍQUIDO: R$ {total_neto_month:.2f}')

