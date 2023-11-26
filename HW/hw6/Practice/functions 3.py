def print_stars(n):
    if n > 0:
        print("*", end=" ")
        print_stars(n - 1)

n = int(input("Enter amount of stars: "))

print_stars(n)