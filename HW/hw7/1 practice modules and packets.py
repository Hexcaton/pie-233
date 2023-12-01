import random
array = [[random.randint(1, 100) for i in range(10)] for i in range(10)]

min_value = min(min(row) for row in array)
max_value = max(max(row) for row in array)

print("Массив:")
for row in array:
    print(row)

print("Минимальное значение: ", min_value)
print("Максимальное значение: ", max_value)