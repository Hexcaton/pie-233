import requests
import json

url = "https://jsonplaceholder.typicode.com/todos/"
response = requests.get(url)

if response.status_code == 200:
    todos_data = response.json()
    with open("todos.json", "w") as json_file:
        json.dump(todos_data, json_file, indent=2)
    print("JSON файл успешно создан.")
else:
    print(f"Не удалось получить данные. Код ответа: {response.status_code}")

with open("todos.json", "r") as json_file:
    todos_array = json.load(json_file)

print(todos_array[0])

for index, todo in enumerate(todos_array):
    filename = f"todo_{index + 1}.json"
    with open(filename, "w") as json_file:
        json.dump(todo, json_file, indent=2)
    print(f"JSON файл {filename} успешно создан.")
