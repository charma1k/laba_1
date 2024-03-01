#Вариант 15. Последовательности натуральных чисел, расположенных в порядке возрастания. Для каждой такой последовательности минимальное число вывести прописью.
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

with open("input.txt", "r") as file:
    block_size = 1024
    while True:
        block = file.read(block_size)
        if not block:
            break
        
        lines = block.split("\n")
        for line in lines:
            sequence = list(map(int, line.split()))
            sequence.sort()
            
            min_number = sequence[0]
            
            min_number_words = number_to_words(min_number)
            
            print(' '.join(map(str, sequence)) + f': {min_number_words} - минимальное число')
