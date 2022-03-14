from factories import *

dark = DarkUIFactory()
light = LightUIFactory()
red = RedUIFactory()
blue = BlueUIFactory()

dark.get_button().click()
light.get_scroll().scroll()
red.get_slider().slide()
blue.get_text_box().type()
