grade_1 = input('Enter the grade from the first two-month period: ')
grade_2 = input('Enter the grade from the second two-month period: ')
grade_3 = input('Enter the grade from the third two-month period: ')
grade_4 = input('Enter the grade from the fourth two-month period: ')
try:
    sum_of_grades = float(grade_1) + float(grade_2) + float(grade_3) + float(grade_4)
    arithmetic_average = sum_of_grades / 4
    print(f'Your arithmetic average in the four two-month period was {arithmetic_average}')
except:
    print('You typed something different from a number.')