print("Введите целое число через Enter:")
string = input()
int_1 = int(string)

if (-15 < int_1 <= 12) or (14 < int_1 < 17) or (19 <= int_1):
    print(True)
else:
    print(False)