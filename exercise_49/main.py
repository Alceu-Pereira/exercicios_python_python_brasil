from random import randint

results = []

for launch in range(0, 100):
    results.append(randint(1, 6))

print(f'Results 1: {results.count(1)}')
print(f'Results 2: {results.count(2)}')
print(f'Results 3: {results.count(3)}')
print(f'Results 4: {results.count(4)}')
print(f'Results 5: {results.count(5)}')
print(f'Results 6: {results.count(6)}')
