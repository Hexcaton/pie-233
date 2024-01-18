class Book:
    def __init__(self):
        self.title = ""
        self.year = 0
        self.publisher = ""
        self.genre = ""
        self.author = ""
        self.price = 0.0

    def input_data(self):
        self.title = input("Введите название книги: ")
        self.year = int(input("Введите год выпуска: "))
        self.publisher = input("Введите издателя: ")
        self.genre = input("Введите жанр: ")
        self.author = input("Введите автора: ")
        self.price = float(input("Введите цену: "))

    def display_data(self):
        print("Название книги:", self.title)
        print("Год выпуска:", self.year)
        print("Издатель:", self.publisher)
        print("Жанр:", self.genre)
        print("Автор:", self.author)
        print("Цена:", self.price)

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price


if __name__ == "__main__":
    book1 = Book()
    book1.input_data()

    print("\nИнформация о книге:")
    book1.display_data()

    print("\nДоступ к отдельным полям:")
    print("Название книги:", book1.get_title())
    print("Год выпуска:", book1.get_year())
    print("Издатель:", book1.get_publisher())
    print("Жанр:", book1.get_genre())
    print("Автор:", book1.get_author())
    print("Цена:", book1.get_price())
