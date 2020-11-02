from machine import I2C, Pin
from wifi_connect import *
import lvgl as lv
import ttgo
from axp_constants import *

watch = ttgo.Watch()
tft = watch.tft
power = watch.pmu

def init():
    connect()        # connect to wifi
    power.adc1Enable(AXP202_VBUS_VOL_ADC1
                     | AXP202_VBUS_CUR_ADC1 |
                     AXP202_BATT_CUR_ADC1 | AXP202_BATT_VOL_ADC1, True)
    watch.lvgl_begin()
    
def interface():
    
    def event_handler(source,evt):
        if  evt == lv.EVENT.VALUE_CHANGED:
            date = lv.calendar.get_pressed_date(source)
            if date:
                print("Clicked date: %02d.%02d.%02d"%(date.day, date.month, date.year))
            
    # Create a screen and load it
    scr = lv.obj()
    lv.scr_load(scr)

    # create a calendar
    calendar = lv.calendar(lv.scr_act(),None)
    calendar.set_size(235,235)
    calendar.align(None,lv.ALIGN.CENTER,0,0)
    calendar.set_event_cb(event_handler)
    
    # Make the date number smaller to be sure they fit into their area
    calendar.set_style_local_text_font(lv.calendar.PART.DATE,lv.STATE.DEFAULT,lv.theme_get_font_small())
    today = lv.calendar_date_t()
    date = cetTime()
    today.year=date[0]
    today.month=date[1]
    today.day=date[2]
    
    calendar.set_today_date(today)
    calendar.set_showed_date(today)
    
    watch.tft.backlight_fade(100)
    
init()
interface()
