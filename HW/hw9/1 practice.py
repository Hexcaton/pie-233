def count_numbers():
    counters = [0] * 9
    while 1:
        num = int(input('Введите числа от 1 до 9. Чтобы завершить, введите 0: '))
        if 1 <= num <= 9:
            counters[num - 1] += 1
        elif num == 0:
            break
    return counters
def main():
    result = count_numbers()
    for count in result:
        print(count, end=' ')

main()