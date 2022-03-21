import copy
from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):
    @abstractmethod
    def use(self, s: str):
        pass

    @abstractmethod
    def clone(self):
        pass


class UnderlinePen(Product):
    def use(self, s: str):
        n = len(s)
        print(s)
        for i in range(n):
            print("~", end="")
        print()

    def clone(self):
        return copy.deepcopy(self)


class MessageBox(Product):
    def __init__(self, deco: str):
        self.deco = deco

    def use(self, s:str):
        n = len(s) + 4

        for i in range(n):
            print(self.deco, end="")
        print()
        print(self.deco, s, self.deco)
        for i in range(n):
            print(self.deco, end="")
        print()

    def clone(self):
        return copy.deepcopy(self)
