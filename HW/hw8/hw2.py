def SelectionSort(A):
    input_list.sort(reverse=True)
input_str = input("Введите список целых чисел через пробел: ")
input_list = list(map(int, input_str.split()))
SelectionSort(input_list)
print(input_list)