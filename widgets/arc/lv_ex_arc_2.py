from machine import I2C, Pin
import lvgl as lv
import ttgo
from axp_constants import *

watch = ttgo.Watch()
tft = watch.tft
power = watch.pmu

def init():
    power.adc1Enable(  AXP202_VBUS_VOL_ADC1
                     | AXP202_VBUS_CUR_ADC1
                     | AXP202_BATT_CUR_ADC1
                     | AXP202_BATT_VOL_ADC1, True)
    watch.lvgl_begin()

def interface():
    # Create a screen and load it
    scr = lv.obj()
    lv.scr_load(scr)
    
    def arc_loader(task):
        arc.set_end_angle
    
        # create an arc
        arc = lv.arc(lv.scr_act(),None)
        arc.set_bg_angles(0,360)
        arc.setangles(270,270)
        arc.align(None,lv.ALIGN.CENTER,0,0)
        watch.tft.backlight_fade(100)
init()
interface()
