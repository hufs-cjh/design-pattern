from prototype import Cloneable


class CloneableManager(object):
    def __init__(self):
        self.showcase = {}

    def register(self, name: str, proto: Cloneable):
        self.showcase[name] = proto

    def create(self, protoName: str) -> Cloneable:
        p: Cloneable = self.showcase[protoName]
        return p.clone()
