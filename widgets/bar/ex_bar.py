#!/opt/bin/lv_micropython -i
import time
import lvgl as lv
import display_driver
            
# create a simple bar
bar1 = lv.bar(lv.scr_act(),None)
bar1.set_size(200,20)
bar1.align(None,lv.ALIGN.CENTER,0,0)
bar1.set_anim_time(2000)
bar1.set_value(100,lv.ANIM.ON)

