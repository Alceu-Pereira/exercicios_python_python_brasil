number_1 = input('Type the first number: ')
number_2 = input('Type the second number: ')
number_3 = input('Type the third number: ')

bigger = float(number_1)
smaller = float(number_1)

if float(number_2) > bigger:
    bigger = float(number_2)

if float(number_3) > bigger:
    bigger = float(number_3)

if float(number_2) < smaller:
    smaller = float(number_2)

if float(number_3) < smaller:
    smaller = float(number_3)

    
print(f'The bigger number is {bigger}')
print(f'The smaller number is {smaller}')