from manager import Manager
from product import *


manager = Manager()

m1 = MessageBox("*")
m2 = MessageBox("#")
p1 = UnderlinePen()

manager.register("msg*", m1)
manager.register("msg#", m2)
manager.register("pen", p1)

msg1 = manager.create("msg*")
msg2 = manager.create("msg#")
pen = manager.create("pen")

word = "hello"
msg1.use(word)
word = "world"
msg2.use(word)
pen.use(word)

# code for check singleton
print(m1, m2)       # it will print same address
print(msg1, msg2)   # it will print different address because it just copied but not initialized
