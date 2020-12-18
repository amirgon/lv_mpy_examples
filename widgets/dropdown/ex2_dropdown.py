#!/opt/bin/lv_micropython
import lvgl as lv
import display_driver
import time

# Create a drop down list
ddlist = lv.dropdown(lv.scr_act())
ddlist.set_options("\n".join([
                    "Apple",
                    "Banana",
                    "Orange",
                    "Melon",
                    "Grape",
                    "Raspberry"]))

ddlist.set_dir(lv.dropdown.DIR.LEFT);
ddlist.set_symbol(None)
ddlist.set_show_selected(False)
ddlist.set_text("Fruits")
# It will be called automatically when the size changes
ddlist.align(None, lv.ALIGN.IN_TOP_RIGHT, 0, 20)

# Copy the drop LEFT list
ddlist = lv.dropdown(lv.scr_act(), ddlist)
ddlist.align(None, lv.ALIGN.IN_TOP_RIGHT, 0, 100)

while True:
    lv.task_handler()
    time.sleep_ms(5)
