number = int(input('Digite um número: '))
odd = 1

for n in range(1, number + 1):
    print(f'{n} / {odd}')
    odd += 2