choiced_number = input('Choose a number: ')
try:
    choiced_number_converted_to_float = float(choiced_number)
    print(f'The number choiced was {choiced_number_converted_to_float}')
except:
    print(f"{choiced_number} isn't a number")