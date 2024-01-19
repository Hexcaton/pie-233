class MainClass:
    def __init__(self, text_field):
        self._text_field = text_field

    def set_text_field(self, text_value=""):
        self._text_field = text_value


class SubClass(MainClass):
    def __init__(self, text_field, numeric_field):
        super().__init__(text_field)
        self._numeric_field = numeric_field

    def set_numeric_field(self, numeric_value):
        self._numeric_field = numeric_value


if __name__ == "__main__":
    main_obj = MainClass("Hello, World!")
    main_obj.set_text_field()
    main_obj.set_text_field("New Text Value")

    sub_obj = SubClass("Subclass Text", 42)
    print("Subclass Text Field:", sub_obj._text_field)
    print("Subclass Numeric Field:", sub_obj._numeric_field)
