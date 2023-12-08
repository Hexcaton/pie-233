import re
def split_string(input_string, separators):
    pattern = '|'.join(map(re.escape, separators))
    result_list = re.split(pattern, input_string)
    return result_list

words = input('Введите слова. Чтобы разделить слова вводите символы , ; |')
separators = [',', ';', '|']
result_split = split_string(words, separators)

print(result_split)
