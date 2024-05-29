number = int(input('Digite um número: '))
odd = 1
sum_number_and_odd = 0

for n in range(1, number + 1):
    print(f'{n} / {odd}')
    sum_number_and_odd += (n / float(odd))
    odd += 2
print(sum_number_and_odd)