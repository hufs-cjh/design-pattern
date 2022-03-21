from product import *


class Manager:
    def __init__(self):
        self.showcase = {"a": 1}

    def register(self, name: str, proto: Product):
        self.showcase[name] = proto

    def create(self, protoName: str) -> Product:
        p: Product = self.showcase[protoName]
        return p.clone()
