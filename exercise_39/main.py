bread_price_unit = float(input('What is the price per unit of bread? '))
bread = bread_price_unit
for n in range(1, 51):
    print(f'{n} - R$ {bread_price_unit:.2f}')
    bread_price_unit = bread + bread_price_unit