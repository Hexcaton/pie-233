import os
import shutil

current_directory = os.getcwd()

new_folder_name = "watch_me"

new_folder_path = os.path.join(current_directory, new_folder_name)

os.makedirs(new_folder_path, exist_ok=True)

folders_to_move = ["video", "sub"]

for folder in folders_to_move:
    source_path = os.path.join(current_directory, folder)
    destination_path = os.path.join(new_folder_path, folder)

    shutil.move(source_path, destination_path)

print(f"Содержимое папок {', '.join(folders_to_move)} перемещено в новую папку {new_folder_name}.")
