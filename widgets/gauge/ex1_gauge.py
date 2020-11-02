#!/opt/bin/lv_micropython
import time
import lvgl as lv
import init_gui

LV_COLOR_BLUE=lv.color_hex3(0xf)
LV_COLOR_ORANGE=lv.color_hex3(0xf80)
LV_COLOR_PURPLE=lv.color_hex3(0x808)

# needle colors
needle_colors=[LV_COLOR_BLUE,LV_COLOR_ORANGE,LV_COLOR_PURPLE]

# create the gauge
gauge1=lv.gauge(lv.scr_act(),None)
gauge1.set_needle_count(3, needle_colors)
gauge1.set_size(200,200)
gauge1.align(None,lv.ALIGN.CENTER,0,0)

# Set the values
gauge1.set_value(0, 10)
gauge1.set_value(1, 20)
gauge1.set_value(2, 50)

while True:
    lv.task_handler()
    time.sleep(5)
