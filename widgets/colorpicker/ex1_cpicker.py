#!/opt/bin/lv_micropython -i
import lvgl as lv
import display_driver
import time

cpicker = lv.cpicker(lv.scr_act(),None)
cpicker.set_size(200, 200)
cpicker.align(None, lv.ALIGN.CENTER, 0, 0)

