from math import pi

radius = input('Type the circle radius: ')
radius_to_float = float(radius)
area = pi * (radius_to_float ** 2)
print(f'The area of the circle with a radius equal {radius_to_float} is {round(area, 2)} m²')