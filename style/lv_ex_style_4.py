#!/opt/bin/micropython
# change the above to the path of your lv_micropython unix binary
#
import time
#
# initialize lvgl
#
import lvgl as lv
import init_gui
from lv_colors import *

style = lv.style_t()
style.init()
# Set a background color and a radius
style.set_radius(lv.STATE.DEFAULT, 5)
style.set_bg_opa(lv.STATE.DEFAULT, lv.OPA.COVER)
style.set_bg_color(lv.STATE.DEFAULT, LV_COLOR_SILVER)

# Add a shadow
style.set_shadow_width(lv.STATE.DEFAULT, 8)
style.set_shadow_color(lv.STATE.DEFAULT, LV_COLOR_BLUE)
style.set_shadow_ofs_x(lv.STATE.DEFAULT, 10)
style.set_shadow_ofs_y(lv.STATE.DEFAULT, 20)

# Create an object with the new style
obj = lv.obj(lv.scr_act(), None)
obj.add_style(lv.obj.PART.MAIN, style)
obj.align(None, lv.ALIGN.CENTER, 0, 0)

while True:
    lv.task_handler()
    time.sleep_ms(10)