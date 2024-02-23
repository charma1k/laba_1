import random

def number_to_words(number):
    words = {
        '0': 'ноль',
        '1': 'один',
        '2': 'два',
        '3': 'три',
        '4': 'четыре',
        '5': 'пять',
        '6': 'шесть',
        '7': 'семь',
        '8': 'восемь',
        '9': 'девять'
    }
    return ' '.join(words[digit] for digit in str(number))

with open("input.txt", "w") as file:
    for _ in range(10):
        sequence = [random.randint(1, 9999) for _ in range(5)]
        sequence.sort()

        min_number = sequence[0]

        min_number_words = number_to_words(min_number)

        file.write(' '.join(map(str, sequence)) + f': {min_number_words} - минимальное число\n')
        print(' '.join(map(str, sequence)) + f': {min_number_words} - минимальное число')
