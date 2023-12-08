import re

def extract_vowel_words(text):
    pattern = re.compile(r'\b[aeiouAEIOU][a-zA-Z]*\b')
    vowel_words = re.findall(pattern, text)
    return vowel_words

words = input()
result_vowel_words = extract_vowel_words(words)

print(result_vowel_words)
