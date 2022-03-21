from abc import ABCMeta, abstractmethod


class Cloneable(metaclass=ABCMeta):
    @abstractmethod
    def clone(self):
        pass
