grade_1 = input('Type your first grade: ')
grade_2 = input('Type your second grade: ')

grade_average = (float(grade_1) + float(grade_2)) / 2

if grade_average >= 7:
    print(f'Your grade average is {grade_average:.2f}')
    print('Approved')

elif grade_average == 10:
    print(f'Your grade average is {grade_average:.2f}')
    print('Approved with distinction')

else:
    print(f'Your grade average is {grade_average:.2f}')
    print('Disapproved')