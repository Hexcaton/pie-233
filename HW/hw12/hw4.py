import os

def common_characters(file_names, output_file):
    common_chars = set()

    with open(file_names[0], 'r', encoding='utf-8') as first_file:
        common_chars.update(set(first_file.read()))

    for file_name in file_names[1:]:
        with open(file_name, 'r', encoding='utf-8') as file:
            common_chars.intersection_update(set(file.read()))

    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(''.join(sorted(common_chars)))
def main():
    os.chdir(r"C:\Repo\pie-233\HW\hw12")
    file_names = []

    while True:
        file_name = input("Введите название файла (или 'quit' для завершения): ")
        if file_name.lower() == 'quit':
            break
        elif os.path.isfile(file_name):
            file_names.append(file_name)
        else:
            print(f"Файл '{file_name}' не найден. Попробуйте снова.")

    if len(file_names) < 2:
        print("Необходимо ввести как минимум два файла. Завершение программы.")
        return
    output_file = input("Введите название файла для записи общих символов: ")
    common_characters(file_names, output_file)

    print(f"Общие символы записаны в файл '{output_file}'.")

if __name__ == "__main__":
    main()