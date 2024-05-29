test_if_is_number = False
try:
    height = float(input('Type your height in meters: '))
    test_if_is_number = True
    gender = str(input('What is your gender? (M/F): ')).strip().upper()
except:
    print("Height typed isn't a number")
if test_if_is_number:
    if gender == 'M':
        ideal_weight = (72.7 * height) - 58
        print(f'Your ideal weight is {ideal_weight:.2f} kg')
    elif gender == 'F':
        ideal_weight = (62.1 * height) - 44.7
        print(f'Your ideal weight is {ideal_weight:.2f} kg')
    else:
        print('You typed a wrong command')