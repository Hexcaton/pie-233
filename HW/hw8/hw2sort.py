numbers = list(map(int, input('Введите числа через пробел, затем нажмите Enter: ').split()))
sorted_numbers = sorted(numbers)
closest_pair = min(zip(sorted_numbers, sorted_numbers[1:]), key=lambda x: x[1] - x[0])
print(closest_pair[0], closest_pair[1])