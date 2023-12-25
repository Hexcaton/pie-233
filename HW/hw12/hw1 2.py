import os
def rename_files(directory="."):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    for file_name in files:
        parts = os.path.splitext(file_name)
        name, extension = parts[0], parts[1]

        name_parts = name.split("_")
        if len(name_parts) == 2:
            first_name, last_name = name_parts
            new_name = f"{last_name}_{first_name}{extension}"
            current_path = os.path.join(directory, file_name)
            new_path = os.path.join(directory, new_name)
            os.rename(current_path, new_path)


if __name__ == "__main__":
    current_directory = os.getcwd()
    rename_files(current_directory)
