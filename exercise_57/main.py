from random import choice

# Read the file
with open('exercise_57\\words.txt', 'r', encoding='UTF-8') as words_file:
    words_list = list(words_file)


# Choice an word in the file
secret_word = choice(words_list).strip().upper()


# Variables
correctly_words = set()
attempts = 0


# Loop principal
while attempts < 6:

    

    showed_word = ''
    for letter in secret_word:
        if letter in correctly_words:
            showed_word += letter.upper().strip()
        else:
            showed_word += ' _ '
    print(f'A palavra é: {showed_word}')



    if showed_word == secret_word:
            print('Você ganhou!')
            break

    
    letter = str(input('Digite uma letra: ')).upper().strip()
    


    if letter in secret_word:
        correctly_words.add(letter)


    else:
        attempts += 1
        print(f'Você errou pela {attempts} vez. Tente de novo!')
        continue


    
    
    

