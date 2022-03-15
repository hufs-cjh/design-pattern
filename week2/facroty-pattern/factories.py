from abc import ABCMeta
from components import *


# Factory Interface
class UIFactory(metaclass=ABCMeta):
    def get_button(self) -> Button:
        raise NotImplementedError

    def get_scroll(self) -> Scroll:
        raise NotImplementedError

    def get_check_box(self) -> CheckBox:
        raise NotImplementedError

    def get_slider(self) -> Slider:
        raise NotImplementedError

    def get_text_box(self) -> TextBox:
        raise NotImplementedError


class DarkUIFactory(UIFactory):
    def get_button(self) -> Button:
        return Button("dark")

    def get_scroll(self) -> Scroll:
        return Scroll("dark")

    def get_check_box(self) -> CheckBox:
        return CheckBox("dark")

    def get_slider(self) -> Slider:
        return Slider("dark")

    def get_text_box(self) -> TextBox:
        return TextBox("dark")


class LightUIFactory(UIFactory):
    def get_button(self) -> Button:
        return Button("light")

    def get_scroll(self) -> Scroll:
        return Scroll("light")

    def get_check_box(self) -> CheckBox:
        return CheckBox("light")

    def get_slider(self) -> Slider:
        return Slider("light")

    def get_text_box(self) -> TextBox:
        return TextBox("light")


class RedUIFactory(UIFactory):
    def get_button(self) -> Button:
        return Button("red")

    def get_scroll(self) -> Scroll:
        return Scroll("red")

    def get_check_box(self) -> CheckBox:
        return CheckBox("red")

    def get_slider(self) -> Slider:
        return Slider("red")

    def get_text_box(self) -> TextBox:
        return TextBox("red")


class BlueUIFactory(UIFactory):
    def get_button(self) -> Button:
        return Button("blue")

    def get_scroll(self) -> Scroll:
        return Scroll("blue")

    def get_check_box(self) -> CheckBox:
        return CheckBox("blue")

    def get_slider(self) -> Slider:
        return Slider("blue")

    def get_text_box(self) -> TextBox:
        return TextBox("blue")
