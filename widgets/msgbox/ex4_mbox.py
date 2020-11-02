#!/opt/bin/lv_micropython
import lvgl as lv
import time
import init_gui

welcome_info = "Welcome to the modal message box demo!\nPress the button to display a message box."
in_msg_info = "Notice that you cannot touch the button again while the message box is open."

class Modal(lv.msgbox):
    """msgbox with semi-transparent background"""
    def __init__(self, parent, *args, **kwargs):
        # Create a base object for the modal background
        obj = lv.obj()
        obj.reset_style_list(lv.obj.PART.MAIN)
        modal_style = lv.style_t()
        modal_style.init()
        # Set the background's style
        modal_style.set_bg_color(lv.STATE.DEFAULT,lv.color_make(0,0,0))
        modal_style.set_bg_grad_color(lv.STATE.DEFAULT,lv.color_make(0,0,0))
        modal_style.set_bg_color(lv.STATE.DEFAULT,lv.color_make(0,0,0))
        modal_style.set_bg_grad_color(lv.STATE.DEFAULT,lv.color_make(0,0,0))
        modal_style.set_bg_opa(lv.STATE.DEFAULT,lv.OPA._50)
        # Create a base object for the modal background
        self.bg = lv.obj(parent)
        self.bg.add_style(lv.btn.PART.MAIN,modal_style)
        self.bg.set_pos(0, 0)
        self.bg.set_size(parent.get_width(), parent.get_height())

        super().__init__(self.bg, *args, **kwargs)
        self.align(None, lv.ALIGN.CENTER, 0, 0)

        # Fade the message box in with an animation
        a = lv.anim_t()
        a.init()
        a.set_time(500)
        a.set_var(obj)
        a.set_values(lv.OPA.TRANSP, lv.OPA.COVER)
        super().set_event_cb(self.default_callback)
        
    def set_event_cb(self, callback):
        self.callback = callback

    def get_event_cb(self):
        return self.callback

    def default_callback(self, obj, evt):
        if evt == lv.EVENT.DELETE:# and obj == self:
            # Delete the parent modal background
            self.get_parent().del_async()
        elif evt == lv.EVENT.VALUE_CHANGED:
            # A button was clicked
            self.start_auto_close(0)
        # Call user-defined callback
        if self.callback is not None:
            self.callback(obj, evt)

def mbox_event_cb(obj, evt):
    if evt == lv.EVENT.DELETE:
        info.set_text(welcome_info)
        info.align(None, lv.ALIGN.IN_BOTTOM_LEFT, 5, -15)
        
def btn_event_cb(btn, evt):
    if evt == lv.EVENT.CLICKED:
        # Create a full-screen background 
        print("btn_event_cb")
        btns2 = ["Ok", "Cancel", ""]

        # Create the message box as a child of the modal background
        mbox = Modal(lv.scr_act())
        mbox.add_btns(btns2)
        mbox.set_text("Hello world!")
        mbox.set_event_cb(mbox_event_cb)
        mbox.align(None,lv.ALIGN.CENTER, 0, 0)
        info.set_text(in_msg_info)
        info.align(None, lv.ALIGN.IN_BOTTOM_LEFT, 5, -5)

# Get active screen
scr = lv.scr_act()

# Create a button, then set its position and event callback
btn = lv.btn(scr)
btn.set_size(200, 60)
btn.set_event_cb(btn_event_cb)
btn.align(None, lv.ALIGN.IN_TOP_LEFT, 20, 20)

# Create a label on the button
label = lv.label(btn)
label.set_text("Display a message box!")

# Create an informative label on the screen
info = lv.label(scr)
info.set_text(welcome_info)
info.set_long_mode(lv.label.LONG.BREAK) # Make sure text will wrap
info.set_width(scr.get_width() - 10)
info.align(None, lv.ALIGN.IN_BOTTOM_LEFT, 5, -15)

while True:
    lv.task_handler()
    time.sleep_ms(5)
