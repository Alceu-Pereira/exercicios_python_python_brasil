work_shift = input('Options:\n[M - morning]\n[A - afternoon]\n[N - night]\nWhat shift do you work? ').upper().strip()

if work_shift == 'M':
    print('Good morning!')

elif work_shift == 'A':
    print('Good afternoon!')

elif work_shift == 'N':
    print('Good evening!')

else:
    print('Invalid value')