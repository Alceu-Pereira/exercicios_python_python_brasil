MONTH = ['1 - January', '2 - February', '3 - Março', '4 - April', '5 - May',
         '6 - June', '7 - July', '8 - August', '9 - September', '10 - October', 
         '11 - November', '12 - December']


temperature_average_month = []


for month in MONTH:
    temperature = float(input(f'What is the temperature average in {month} ? '))
    temperature_average_month.append(temperature)


for k, v in enumerate(temperature_average_month):
    print(f'{MONTH[k]}: {v:.1f}°C')
   
    