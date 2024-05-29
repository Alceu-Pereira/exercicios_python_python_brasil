gender_input = input('Type a gender (M/F): ').upper().strip()

if gender_input == 'M':
    print('You are of the male gender')
elif gender_input == 'F':
    print('You are of the feminine gender')
else:
    print('Invalid gender')
