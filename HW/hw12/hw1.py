import os
import shutil

os.chdir(r"C:\Repo\pie-233\HW\hw12")

words_file_name = "words.txt"
newFile_file_name = "newFile.txt"

with open(words_file_name, "w", encoding='utf-8') as words_file:
    words_file.write("Слова, 1 2 3 4 5")

with open(newFile_file_name, "w", encoding='utf-8') as newFile_file:
    newFile_file.write('Слова, 1 2 3 4 5 6')

temp_file_name = "temp.txt"

with open(words_file_name, 'r', encoding='utf-8') as first, open(newFile_file_name, 'r',
                                                                 encoding='utf-8') as second, open(temp_file_name, 'w',
                                                                                                   encoding='utf-8') as temp_file:
    secondContent = second.read()
    firstContent = first.read()

    temp_file.write(secondContent.replace(firstContent, ''))

shutil.move(temp_file_name, newFile_file_name)

with open(newFile_file_name, 'r', encoding='utf-8') as file:
    print(file.read())
