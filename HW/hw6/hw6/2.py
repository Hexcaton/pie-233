def create_nested_list():
    return [list(map(int, input("Enter a row of 3 elements separated by space: ").split())) for _ in range(3)]

def main():
    nested_list = create_nested_list()

    diagonal_sum = sum(nested_list[i][i] for i in range(3))
    print("Diagonals :", " + ".join(map(str, [nested_list[i][i] for i in range(3)])), "=", diagonal_sum)

if __name__ == "__main__":
    main()