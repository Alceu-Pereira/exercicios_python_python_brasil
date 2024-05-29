year_informed = input('Inform an year: ')
is_leap = False

if int(year_informed) % 100 == 0:
    is_leap = False
else:
    if int(year_informed) % 4 == 0:
        is_leap = True
    if int(year_informed) % 400 == 0:
        is_leap = True

if is_leap:
    print('It is a leap year')

else:
    print('It is not a leap year')