#!/opt/bin/lv_micropython -i
import lvgl as lv
from display_driver_utils import driver,ORIENT_LANDSCAPE
drv = driver(width=320,height=240,orientation=ORIENT_LANDSCAPE)

from lv_colors import lv_colors
from time import sleep
from meterClass import Meter

value = 23.7

SCREEN_WIDTH  = lv.scr_act().get_disp().driver.hor_res
SCREEN_HEIGHT = lv.scr_act().get_disp().driver.ver_res
print("screen width: ",SCREEN_WIDTH)

text_style = lv.style_t()
text_style.init()
text_style.set_text_color(lv.STATE.DEFAULT,lv_colors.GREEN)
text_style.set_text_font(lv.STATE.DEFAULT,lv.font_montserrat_24)

label = lv.label(lv.scr_act())
label.set_text('SHT30 Measurements')
label.align(None, lv.ALIGN.OUT_TOP_MID, -50, 30)
label.add_style(lv.label.PART.MAIN,text_style)

m1 = Meter(max_value=50,x=60,y=120,
           value=value,legend=('0','10','20','30','40','50'),
           label_text='Temperature',value_text_format="{:4.1f} °C")

value = 65.3    
m2 = Meter(x=220, y=120,
           value=value,legend=('0','20','40','60','80','100'),
           label_text='Humidity',value_text_format="{:4.1f} %")

