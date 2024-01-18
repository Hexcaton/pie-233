class Car:
    def __init__(self):
        self.model = ""
        self.year = 0
        self.manufacturer = ""
        self.engine_volume = 0.0
        self.color = ""
        self.price = 0.0

    def input_data(self):
        self.model = input("Введите название модели: ")
        self.year = int(input("Введите год выпуска: "))
        self.manufacturer = input("Введите производителя: ")
        self.engine_volume = float(input("Введите объем двигателя: "))
        self.color = input("Введите цвет машины: ")
        self.price = float(input("Введите цену: "))

    def display_data(self):
        print("Название модели:", self.model)
        print("Год выпуска:", self.year)
        print("Производитель:", self.manufacturer)
        print("Объем двигателя:", self.engine_volume)
        print("Цвет машины:", self.color)
        print("Цена:", self.price)

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_manufacturer(self):
        return self.manufacturer

    def get_engine_volume(self):
        return self.engine_volume

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price


if __name__ == "__main__":
    car1 = Car()
    car1.input_data()

    print("\nИнформация о машине:")
    car1.display_data()

    print("\nДоступ к отдельным полям:")
    print("Название модели:", car1.get_model())
    print("Год выпуска:", car1.get_year())
    print("Производитель:", car1.get_manufacturer())
    print("Объем двигателя:", car1.get_engine_volume())
    print("Цвет машины:", car1.get_color())
    print("Цена:", car1.get_price())