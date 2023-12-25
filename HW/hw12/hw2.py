import os
import shutil
def transliterate(text, direction):
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh',
        'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
        'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts',
        'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
        'я': 'ya',
        'a': 'а', 'b': 'б', 'c': 'с', 'd': 'д', 'e': 'е', 'f': 'ф', 'g': 'г', 'h': 'х',
        'i': 'и', 'j': 'й', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п',
        'q': 'к', 'r': 'р', 's': 'с', 't': 'т', 'u': 'у', 'v': 'в', 'w': 'в', 'x': 'кс',
        'y': 'ы', 'z': 'з',
    }

    result = ''
    for char in text:
        result += translit_dict.get(char.lower(), char)
    if text.islower():
        return result
    elif text.isupper():
        return result.upper()
    else:
        return result.title()
def main():
    os.chdir(r"C:\Repo\pie-233\HW\hw12")

    input_file_name = "input.txt"
    output_file_name = "output.txt"

    with open(input_file_name, "w", encoding='utf-8') as input_file:
        input_file.write("Пример текста для транслитерации.")

    print("Выберите направление транслитерации:")
    print("1. Русский -> Английский")
    print("2. Английский -> Русский")
    choice = input("Введите номер направления (1 или 2): ")

    with open(input_file_name, 'r', encoding='utf-8') as input_file, open(output_file_name, 'w',
                                                                          encoding='utf-8') as output_file:
        text_to_transliterate = input_file.read()
        if choice == '1':
            transliterated_text = transliterate(text_to_transliterate, 'ru-en')
        elif choice == '2':
            transliterated_text = transliterate(text_to_transliterate, 'en-ru')
        else:
            print("Неверный выбор. Завершение программы.")
            return

        output_file.write(transliterated_text)

    with open(output_file_name, 'r', encoding='utf-8') as result_file:
        print("\nРезультат транслитерации:")
        print(result_file.read())


if __name__ == "__main__":
    main()