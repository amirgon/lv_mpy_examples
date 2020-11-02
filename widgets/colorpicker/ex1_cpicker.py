#!/opt/bin/lv_micropython
import lvgl as lv
import init_gui
import time

cpicker = lv.cpicker(lv.scr_act(),None)
cpicker.set_size(200, 200)
cpicker.align(None, lv.ALIGN.CENTER, 0, 0)

while True:
    lv.task_handler()
    time.sleep_ms(5)
