letter = input('Type a letter: ')
if 0 < len(letter) <= 1:
    if letter.upper().strip() in 'AEIOU':
        print(f'{letter.upper()} is a vowel')
    else:
        if letter.upper().strip().isalpha():
            print(f'{letter.upper()} is a consonant')
        else:
            print(f"{letter} isn't a letter")
else:
    print('Write one letter, please.')