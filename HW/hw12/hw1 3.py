import os
import shutil

def copy_files_from_list(file_list, source_directory, destination_directory):
    os.makedirs(destination_directory, exist_ok=True)

    with open(file_list, 'r') as list_file:
        for line in list_file:
            file_name = line.strip()
            source_path = os.path.join(source_directory, file_name)

            destination_path = os.path.join(destination_directory, file_name)

            if os.path.isfile(source_path):
                shutil.copy2(source_path, destination_path)
                print(f"Скопирован файл: {file_name}")
            else:
                print(f"Файл не найден: {file_name}")

if __name__ == "__main__":
    current_directory = os.getcwd()

    list_filename = "list.tsv"
    destination_folder = "list"
    copy_files_from_list(list_filename, current_directory, destination_folder)
