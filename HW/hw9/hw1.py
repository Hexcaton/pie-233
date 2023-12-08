def LinearSort(strings):
    max_length = max(len(s) for s in strings)

    for s in strings:
        stars = max_length - len(s)
        aligned_string = '*' * stars + s
        print(aligned_string)

word_list = []
while True:
    words = input('Введите ваши символы. Чтобы завершить, введите пустую строку: ')
    if words == '':
        break
    else:
        word_list.append(words)

LinearSort(word_list)