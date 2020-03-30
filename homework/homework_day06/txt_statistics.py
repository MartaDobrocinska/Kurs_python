import re
import homework.homework_day06.txt_statistics_modules.character_counter as character_counter
import homework.homework_day06.txt_statistics_modules.count_words as count_words

with open('lorem.txt', 'r') as file:
    words = file.read()

    count_words.count_words(words)

    capital_letters = re.compile('[A-Z]')
    print('Liczba poszczególnych wielkich liter:')
    character_counter.char_counter(capital_letters, 'lorem.txt')

    lowercase_letters = re.compile('[a-z]')
    print('Liczba poszczególnych małych liter:')
    character_counter.char_counter(lowercase_letters, 'lorem.txt')

    numbers = re.compile('[0-9]')
    print('Liczba poszczególnych cyfr:')
    character_counter.char_counter(numbers, 'lorem.txt')

    sentences = re.split(r'[.!?]+', words)
    blank = sentences.count('')
    newline = sentences.count('\n')
    print('Liczba zdań:', len(sentences) - blank - newline)
