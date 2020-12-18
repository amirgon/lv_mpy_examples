#!/opt/bin/lv_micropython
import time
import lvgl as lv
import display_driver

def close_win_cb():
    nonlocal win
    if win:
        win.delete()
        win = None
            
# create a window
win = lv.win(lv.scr_act(),None)
win.set_title("Window title")                   # Set the title

win_style = lv.style_t()
win_style.init()
win_style.set_margin_right(lv.STATE.DEFAULT, 50)
win.add_style(lv.win.PART.CONTENT_SCROLLABLE,win_style)

# Add control button to the header
close_btn = win.add_btn_right(lv.SYMBOL.CLOSE)  # Add close button and use built-in close action
close_btn.set_event_cb(lambda obj,e:  e == lv.EVENT.RELEASED and close_win_cb())

win.add_btn_right(lv.SYMBOL.SETTINGS)           # Add a setup button

# Add some dummy content
txt = lv.label(win)
txt.set_text(
"""This is the content of the window

You can add control buttons to
the window header

The content area becomes automatically 
scrollable is it's large enough.

You can scroll the content
See the scroll bar on the right!"""
)

while True:
    lv.task_handler()
    time.sleep_ms(5)
