def LinearSearch(numList, num):
    for i in range(len(numList)):
        if numList[i] == num:
            return i
    return -1

numList = [7, 9, 5, 6, -99, -32, 10, -6, 45, 14]
print('Введите число из списка ', numList, 'которое хотите найти: ')
num = int(input())
result = LinearSearch(numList, num)

if result != -1:
    print(f'Число {num} найдено в списке с индексом {result}.')
else:
    print(f'Число {num} не найдено в списке.')
