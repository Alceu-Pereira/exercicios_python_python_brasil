def system_twelve(hours, minutes):
    pm = False
    am = False
    
    
    if hours > 12:
        pm = True
    else:
        am = True

    if pm:
        hours = hours - 12

    def input_twelve():
        if pm:
            print(f"It's {hours}:{minutes} PM")
        elif am:
            print(f"It's {hours}:{minutes} AM")

    return input_twelve()

while True:
    hours = int(input('Enter how many hours is it: '))
    minutes = int(input('Enter how many minutes is it: '))
    system_twelve(hours, minutes)
    repeat = input('Do you want to convert another time? (yes/no): ')
    if repeat.lower() != 'yes':
        break