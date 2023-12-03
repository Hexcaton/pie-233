def max_users_in_archive(free_space, user_count, user_data):
    user_data.sort()
    total_space_used = 0
    users_count = 0

    for data in user_data:
        total_space_used += data
        if total_space_used <= free_space:
            users_count += 1
        else:
            break
    return users_count

input_line = input("Введите размер свободного места и количество пользователей: ")
free_space, user_count = map(int, input_line.split())

user_data = []
for _ in range(user_count):
    data = int(input("Введите объем данных пользователя: "))
    user_data.append(data)

result = max_users_in_archive(free_space, user_count, user_data)
print(result)