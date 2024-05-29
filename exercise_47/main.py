cars = ['Fusca', 'Gol', 'Uno', 'Vectra', 'Peugeout']
km_per_liter = [7, 10, 12.5, 9, 14.5]
lowest = max(km_per_liter)

lowest_consumption = ''




print('Comparativo de consumo de combustível')
print()
for k, v in enumerate(cars):
    print(f'Veículo {k + 1}')
    print(f'Nome: {v}')
    print(f'Km por litro: {km_per_liter[k]}')




print()
print('Relatório Final')

for k, v in enumerate(cars):
    print(f'{k + 1} - {v}   -   {km_per_liter[k]}   -   {(1000 / km_per_liter[k]):.1f} litros  - R$ {(1000 / km_per_liter[k]) * 2.25:.2f}')
    if km_per_liter[k] == lowest:
        lowest_consumption = v

print(f'O menor consumo é do {lowest_consumption}')