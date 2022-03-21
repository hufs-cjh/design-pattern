from manager import CloneableManager
from component import *

c_manager = CloneableManager()      # init manager

# init prototype instances
proto_div = Division()
proto_p = Paragraph()
proto_button = Button()

# set attributes: Paragraph
proto_p.set_text("Hello World!")
proto_p.set_color("red")

# set attributes: Button
proto_button.set_text("button")
proto_button.set_size("30px")
proto_button.set_onclick("alert(\"Button Clicked!\")")

# set attributes: Division
proto_div.set_inner(f"{proto_p}\t{proto_button}")

# register components on manager
c_manager.register("p", proto_p)
c_manager.register("button", proto_button)
c_manager.register("div", proto_div)

# copy components from prototype
p1: Paragraph = c_manager.create("p")
button1: Button = c_manager.create("button")
div1: Division = c_manager.create("div")

# before attribute changes
print("==========")
print("BEFORE ATTRIBUTE CHANGES")
print("proto:")
print(proto_div)
print("copied:")
print(div1)
print(f"addr of proto: {hex(id(proto_div))} / copied: {hex(id(div1))}")
print("==========")

print()


# change attributes
p1.set_text("attribute changed paragraph (copied)")
button1.set_text("btn1")
div1.set_inner(f"{p1}{button1}")

# after attribute changes

print("==========")
print("AFTER ATTRIBUTE CHANGES")
print("proto:")
print(proto_div)
print("copied:")
print(div1)
print(f"addr of proto: {hex(id(proto_div))} / copied: {hex(id(div1))}")
print("==========")
