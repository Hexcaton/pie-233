from itertools import permutations
def genWords(a_str):
    symbols = list(a_str)
    combinations = set(''.join(s) for s in permutations(symbols))
    def is_valid(word):
        return all(word.count(c) <= symbols.count(c) for c in set(word))
    words = [word for word in combinations if is_valid(word)]
    return sorted(words, key=len)

a_str = input('Введите символы: ')
result = genWords(a_str)
print(len(result))
for word in result:
    print(word)