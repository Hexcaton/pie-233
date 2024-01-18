class Stadium:
    def __init__(self):
        self.name = ""
        self.opening_date = ""
        self.country = ""
        self.city = ""
        self.capacity = 0

    def input_data(self):
        self.name = input("Введите название стадиона: ")
        self.opening_date = input("Введите дату открытия: ")
        self.country = input("Введите страну: ")
        self.city = input("Введите город: ")
        self.capacity = int(input("Введите вместимость: "))

    def display_data(self):
        print("Название стадиона:", self.name)
        print("Дата открытия:", self.opening_date)
        print("Страна:", self.country)
        print("Город:", self.city)
        print("Вместимость:", self.capacity)

    def get_name(self):
        return self.name

    def get_opening_date(self):
        return self.opening_date

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity


if __name__ == "__main__":
    stadium1 = Stadium()
    stadium1.input_data()

    print("\nИнформация о стадионе:")
    stadium1.display_data()

    print("\nДоступ к отдельным полям:")
    print("Название стадиона:", stadium1.get_name())
    print("Дата открытия:", stadium1.get_opening_date())
    print("Страна:", stadium1.get_country())
    print("Город:", stadium1.get_city())
    print("Вместимость:", stadium1.get_capacity())
