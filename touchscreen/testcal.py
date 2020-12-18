#!/opt/bin/lv_micropython
import lvgl as lv
import display_driver
import time
from micropython import const

CIRCLE_SIZE = const(20)
TP_MAX_VALUE = const(10000)

def check():
    point = lv.point_t()
    indev = lv.indev_get_act()
    indev.get_point(point)
    print("click position: x: %d, y: %d"%(point.x,point.y))
    circ_area.set_pos(point.x - CIRCLE_SIZE // 2,
                      point.y - CIRCLE_SIZE // 2)
    
def show_text(txt):
    label_main.set_text(txt)
    label_main.set_align(lv.label.ALIGN.CENTER)
    label_main.set_pos((HRES - label_main.get_width() ) // 2,
                       (VRES - label_main.get_height()) // 2)
    
disp = lv.scr_act().get_disp()
HRES = disp.driver.hor_res
VRES = disp.driver.ver_res

# Create a big transparent button screen to receive clicks
style_transp = lv.style_t()
style_transp.init()
style_transp.set_bg_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
big_btn = lv.btn(lv.scr_act(), None)
big_btn.set_size(TP_MAX_VALUE, TP_MAX_VALUE)
big_btn.add_style(lv.btn.PART.MAIN,style_transp)
big_btn.set_layout(lv.LAYOUT.OFF)

label_main = lv.label(lv.scr_act(), None)

style_circ = lv.style_t()
style_circ.init()

show_text("Click/drag on screen\n" + \
               "to check calibration")
big_btn.set_event_cb(lambda obj, event: check() if event == lv.EVENT.PRESSING else None)


circ_area = lv.obj(lv.scr_act(), None)
circ_area.set_size(CIRCLE_SIZE, CIRCLE_SIZE)
circ_area.add_style(lv.STATE.DEFAULT,style_circ)
circ_area.set_click(False)

while True:
    pass
