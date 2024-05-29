from random import choice, sample


with open('exercise_58\\words.txt', 'r', encoding='UTF-8') as words_file:
    words_list = list(words_file)

secret_word = choice(words_list).strip().lower()

secret_word_shuffle = sample(list(secret_word), len(secret_word))

while True:
    print('Descubra a palavra embaralhada:', end=' ')
    for letter in secret_word_shuffle:
        print(letter, end=' ')
    print()
    user_word = input('Escolha uma palavra: ')

    if user_word == secret_word:
        print('Parabéns, você venceu!')
        break