with open("todos.json", "r") as json_file:
    todos_array = json.load(json_file)
    print(todos_array[0])