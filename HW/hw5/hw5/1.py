a = int(input())
b = int(input())

def find_lcm(x, y): #НОК a и b
    greater = max(x, y)
    while True:
        if greater % x == 0 and greater % y == 0:
            return greater
        greater += 1

lcm = find_lcm(a, b)
print(lcm)
