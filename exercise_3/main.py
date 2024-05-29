print(f'{"SUM BETWEEN TWO NUMBERS":-^60}')
number_1 = input('Type a number: ')
number_2 = input('Type another number: ')
try:
    sum = float(number_1) + float(number_2)
    print(f'The sum between {number_1} and {number_2} is {sum}')
except:
    print('Type valid numbers')