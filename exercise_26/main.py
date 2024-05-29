product_1 = input('How much is the product 1? ')
product_2 = input('How much is the product 2? ')
product_3 = input('How much is the product 3? ')

cheaper = float(product_1)

if float(product_2) < cheaper:
    cheaper = float(product_2)

if float(product_3) < cheaper:
    cheaper = float(product_3)

print(f'The cheaper product costs R$ {cheaper:.2f}')