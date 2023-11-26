def get_even_numbers():
    numbers = []
    for num in range(4, 31, 2):
        numbers.append(num)
    return numbers


result = get_even_numbers()
print(result)

def distance(x1, y1, x2, y2):
    distance_squared = (x2 - x1)**2 + (y2 - y1)**2
    distance_result = distance_squared**0.5
    return distance_result

x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))

result = distance(x1, y1, x2, y2)

print(result)