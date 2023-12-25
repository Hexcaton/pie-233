import os
def merge_files(file_names, output_file):
    with open(output_file, 'w', encoding='utf-8') as output:
        for file_name in file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                output.write(file.read())
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
    if not file_names:
        print("Не введено ни одного файла. Завершение программы.")
        return

    output_file = input("Введите название файла для объединения содержимого: ")
    merge_files(file_names, output_file)
    print(f"Содержимое файлов объединено в '{output_file}'.")

if __name__ == "__main__":
    main()
    