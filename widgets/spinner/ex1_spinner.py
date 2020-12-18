#!/opt/bin/lv_micropython
import lvgl as lv
import display_driver
import time

# create a Preloader object
preload = lv.spinner(lv.scr_act(), None)
preload.set_size(100, 100)
preload.align(None, lv.ALIGN.CENTER, 0, 0)

while True:
    lv.task_handler()
    time.sleep_ms(5)
