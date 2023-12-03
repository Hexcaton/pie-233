def InsertionSort(A):
    input_list.sort()
input_str = input("Введите список целых чисел через пробел: ")
input_list = list(map(int, input_str.split()))
InsertionSort(input_list)
print(input_list)