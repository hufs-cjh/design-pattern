class Component:
    def __init__(self, color):
        self.color = color


class Button(Component):
    def __init__(self, color):
        super().__init__(color)

    def click(self):
        print(f"{self.color} button clicked")


class Scroll(Component):
    def __init__(self, color):
        super().__init__(color)

    def scroll(self):
        print(f"{self.color} scroll bar scrolled")


class CheckBox(Component):
    def __init__(self, color):
        super().__init__(color)

    def check(self):
        print(f"{self.color} check box checked")


class Slider(Component):
    def __init__(self, color):
        super().__init__(color)

    def slide(self):
        print(f"{self.color} slider slided")


class TextBox(Component):
    def __init__(self, color):
        super().__init__(color)

    def type(self):
        print(f"text typed in {self.color} text box")