class MainClass:
    def __init__(self, text_field):
        self.text_field = text_field

    def set_text_field(self, text_value=""):
        self.text_field = text_value


class SubClass(MainClass):
    def __init__(self, text_field, numeric_field):
        super().__init__(text_field)
        self.numeric_field = numeric_field


if __name__ == "__main__":
    main_obj = MainClass("Hello, World!")
    main_obj.set_text_field()
    main_obj.set_text_field("New Text Value")

    sub_obj = SubClass("Subclass Text", 42)
    print("Subclass Text Field:", sub_obj.text_field)
    print("Subclass Numeric Field:", sub_obj.numeric_field)
