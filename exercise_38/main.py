print('Lojas Quase Dois - Tabela de preços')
price = 1.99

for n in range(1, 51):
    print(f'{n} - R$ {price:.2f}')
    price += 1.99