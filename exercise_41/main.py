number = int(input('Write the factorial number to be showed: '))
factorial = 1

for n in range(number, 0, -1):
    factorial *= n
    if n == 1:
        print(n, end=' = ')
    else:
        if n == number:
            print(f'{n}! = ', n, end=' * ')
        else:
            print(n, end=' * ')

print(factorial)
