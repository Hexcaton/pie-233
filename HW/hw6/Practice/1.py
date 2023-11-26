def calculate_sum_and_difference(num1, num2):
    return num1 + num2, num1 - num2

str = input('Enter two numbers in one line: ')
numbers = [int(num) for num in str.split()]

if len(numbers) == 2:
    sum, diff = calculate_sum_and_difference(numbers[0], numbers[1])
    print(f'The sum of numbers is {sum}, the difference of numbers is {diff}')
else:
    print('Incorrect input. Please enter two numbers.')