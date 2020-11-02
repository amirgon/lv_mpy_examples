#!/opt/bin/lv_micropython
import lvgl as lv
import init_gui
import time
from lv_colors import *

LV_IMG_PX_SIZE_ALPHA_BYTE=3

with open('imgbtn_green_map.bin','rb') as f:
    img_data = f.read()

# Create a screen with a draggable image

img = lv.img(lv.scr_act(),None)
img.align(lv.scr_act(), lv.ALIGN.CENTER, 0, 0)
img_dsc = lv.img_dsc_t(
    {
        "header": {"always_zero": 0, "w": 125, "h": 40, "cf": lv.img.CF.TRUE_COLOR_ALPHA},
        "data": img_data,
        "data_size": len(img_data),
    }
)

img.set_src(img_dsc)
img.set_drag(True)
print("Image size: ",img_dsc.data_size)

while True:
    lv.task_handler()
    time.sleep_ms(5)
