def main():
    N = int(input("Введите размер списка: "))
    numbers = list(map(int, input("Введите ячейки списка через пробел и нажмите Enter: ").split()))

    odd_numbers = [num for num in numbers if num % 2 != 0]
    even_numbers = [num for num in numbers if num % 2 == 0]

    print(*odd_numbers)
    print(*even_numbers)
    print("YES" if len(odd_numbers) > len(even_numbers) else "NO")

if __name__ == "__main__":
    main()