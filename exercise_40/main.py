product_value_list = []
total = 0
money = 0
change = 0
product_key = 0


while True:
    product_key += 1
    product_value = float(input(f'How much is the Product {product_key}: '))
    if product_value == 0:
        print()
        money = float(input('Enter the value paid by the customer: '))
        break
    product_value_list.append(product_value)
    total += product_value
    
print()
for k, v in enumerate(product_value_list):
    print(f'Produto {k + 1}: R$ {v:.2f}')


print(f'Total: R$ {total:.2f}')
print(f'Dinheiro: R$ {money:.2f}')
print(f'Troco: R$ {(money - total):.2f}')
