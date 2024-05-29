n1 = input('Text a number: ')
n2 = input('Text another number: ')
if float(n1) > float(n2):
    print(f'{float(n1):.0f} is greather than {float(n2):.0f}')
else:
    if float(n1) == float(n2):
        print('The numbers are the same')
    else:
        print(f'{float(n2):.0f} is grather than {float(n1):.0f}')
