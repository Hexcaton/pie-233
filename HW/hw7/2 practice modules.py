import random

random_vector = [random.randint(1, 100) for _ in range(30)]
average_value = sum(random_vector) / len(random_vector)

print("Случайный вектор:", random_vector)
print("Среднее значение:", average_value)
