#!/opt/bin/lv_micropython -i
import lvgl as lv
import display_driver
import time

# create an arc
arc = lv.arc(lv.scr_act(),None)
arc.set_end_angle(200)
arc.set_size(150,150)
arc.align(None,lv.ALIGN.CENTER,0,0)

