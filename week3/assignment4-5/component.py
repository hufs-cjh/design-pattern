import copy
from prototype import Cloneable


class Division(Cloneable):
    def __init__(self):
        self.inner = ""

    def __str__(self):
        return self.to_html()

    def clone(self):
        return copy.deepcopy(self)

    def to_html(self):
        return f"<div>\n\t{self.inner}\n</div>"

    def set_inner(self, html: str):
        self.inner = html


class Button(Cloneable):
    def __init__(self):
        self.text = ""
        self.onclick = ""
        self.size = "0"
        self.color = "white"

    def __str__(self):
        return self.to_html()

    def clone(self):
        return copy.deepcopy(self)

    def to_html(self):
        return \
            f"<button onclick=\"{self.onclick}\"" + \
            f"style=\"color: {self.color}; " + \
            f"width={self.size}\">{self.text}</button>"

    def set_text(self, text: str):
        self.text = text

    def set_onclick(self, js: str):
        self.onclick = js

    def set_size(self, size: str):
        self.size = size

    def set_color(self, color: str):
        self.color = color


class Paragraph(Cloneable):
    def __init__(self):
        self.text = ""
        self.color = "black"

    def __str__(self):
        return self.to_html()

    def clone(self):
        return copy.deepcopy(self)

    def to_html(self):
        return f"<p style=\"color: {self.color}\">{self.text}</p>"

    def set_text(self, text: str):
        self.text = text

    def set_color(self, color: str):
        self.color = color
