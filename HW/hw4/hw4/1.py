print('Введите три целых числа через Enter:')

int_a = int(input())
int_b = int(input())
int_c = int(input())

if ((int_b + int_c) > int_a) and ((int_a + int_c) > int_b) and ((int_a + int_b) > int_c):
    print(True)
else:
    print(False)