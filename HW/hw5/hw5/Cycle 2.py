N = int(input("Введите целое число:"))

for i in range(1, N + 1):
    squared = i**2
    if squared <= N:
        print(squared)
    else:
        break