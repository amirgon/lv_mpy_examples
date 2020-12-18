#!/opt/bin/lv_micropython
import time
import lvgl as lv
import display_driver

def event_handler(source,evt):
    if  evt == lv.EVENT.VALUE_CHANGED:
        print("Value:",slider.get_value())
            
# create a slider
slider = lv.slider(lv.scr_act(),None)
slider.set_width(200)
slider.align(None,lv.ALIGN.CENTER,0,0)
slider.set_event_cb(event_handler)

while True:
    lv.task_handler()
    time.sleep_ms(5)    
