#!/opt/bin/lv_micropython
import lvgl as lv
import time
import init_gui
from lv_colors import *

welcome_info = "Welcome to the modal message box demo!\nPress the button to display a message box."
in_msg_info = "Notice that you cannot touch the button again while the message box is open."

LV_HOR_RES=240
LV_VER_RES=240

def opa_anim(bg,v):
    lv.obj.set_style_local_bg_opa(bg, lv.obj_.PART.MAIN, lv.STATE.DEFAULT, v)
    
def btn_event_cb(btn,evt):
    if evt == lv.EVENT.CLICKED:
        # Create a full-screen background 

        #Create a base object for the modal background 
        obj = lv.obj(lv.scr_act(), None)
        obj.reset_style_list(lv.obj.PART.MAIN)
        obj.add_style(lv.obj.PART.MAIN, style_modal)
        obj.set_pos(0, 0)
        obj.set_size(LV_HOR_RES, LV_VER_RES);

        btns2 = ["Ok", "Cancel", ""]

        # Create the message box as a child of the modal background 
        mbox = lv.msgbox(obj, None)
        mbox.add_btns(btns2);
        mbox.set_text("Hello world!")
        mbox.align(None, lv.ALIGN.CENTER, 0, 0)
        # mbox.set_event_cb(mbox_event_cb)

        # Fade the message box in with an animation 
        a=lv.anim_t()
        a.init()
        a.set_var(obj)
        a.set_time(500)
        a.set_values(lv.OPA.TRANSP, lv.OPA._50)
        a.set_exec_cb(lambda a: opa_anim)
        a.start()

        info.set_text(in_msg_info)
        info.align(None, lv.ALIGN.IN_BOTTOM_LEFT, 5, -5)

style_modal = lv.style_t()
style_modal.init()
style_modal.set_bg_color(lv.STATE.DEFAULT, LV_COLOR_BLACK)

# Create a button, then set its position and event callback */
btn = lv.btn(lv.scr_act(), None)
btn.set_size(200, 60)
btn.set_event_cb(btn_event_cb)
btn.align(None, lv.ALIGN.IN_TOP_LEFT, 20, 20)

# Create a label on the button 
label = lv.label(btn,None)
label.set_text("Display a message box!")

# Create an informative label on the screen 
info = lv.label(lv.scr_act(), None)
info.set_text(welcome_info)
info.set_long_mode(lv.label.LONG.BREAK)       # Make sure text will wrap 
info.set_width(LV_HOR_RES - 10)
info.align(None, lv.ALIGN.IN_BOTTOM_LEFT, 5, -5)
    
while True:
    lv.task_handler()
    time.sleep_ms(5)
