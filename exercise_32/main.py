side_1 = float(input('Write the size of the first side of a triangle: '))
side_2 = float(input('Write the size of the second side of a triangle: '))
side_3 = float(input('Write the size of the third side of a triangle: '))

is_triangle = False

if ((side_1 + side_2) > side_3) and ((side_1 + side_3) > side_2) and ((side_2 + side_3) > side_1):
    is_triangle = True


if is_triangle:
    if side_1 == side_2 and side_2 == side_3:
        print('The triangle is equilateral')

    elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
        print('The triangle is isosceles')
    
    else:
        print('The triangle is escalene')

else:
    print('With these sides size the triangle doesnt exist')