#!/opt/bin/lv_micropython
import lvgl as lv
import display_driver
import os

def event_handler(source,evt):
    if  evt == lv.EVENT.VALUE_CHANGED:
        date = lv.calendar.get_pressed_date(source)
        if date:
            print("Clicked date: %02d.%02d.%02d"%(date.day, date.month, date.year))

# create a calendar
calendar = lv.calendar(lv.scr_act(),None)
calendar.set_size(235,235)
calendar.align(None,lv.ALIGN.CENTER,0,0)
calendar.set_event_cb(event_handler)

# Make the date number smaller to be sure they fit into their area
calendar.set_style_local_text_font(lv.calendar.PART.DATE,lv.STATE.DEFAULT,lv.theme_get_font_small())

try:
    osVersion=os.uname()
    print("Running: ",osVersion)
    from wifi_connect import *
    # connect to the Internet and get the current time
    connect()
    now = cetTime()
except:
    print("Running on Unix")
    import time
    now=time.localtime()
    
today = lv.calendar_date_t()
today.year = now[0]
today.month = now[1]
today.day = now[2]

calendar.set_today_date(today)
calendar.set_showed_date(today)

while True:
    pass
