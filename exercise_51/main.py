def print_n_line(number):
    for n in range(1, number + 1):
        subtractor = 1
        while subtractor <= n:
            if subtractor == n:
                print(subtractor, end='\n')
            else:
                print(subtractor, end='   ')
            subtractor += 1


print_n_line(5)