number_1 = input('Type the first number: ')
number_2 = input('Type the second number: ')
number_3 = input('Type the third number: ')

bigger = float(number_1)

if float(number_2) > bigger:
    bigger = float(number_2)

if float(number_3) > bigger:
    bigger = float(number_3)

print(f'The bigger number is {bigger}')