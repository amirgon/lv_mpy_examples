#!/opt/bin/lv_micropython -i
# This creates a custom "temperature button" which print a temperature value.
# Once you set a new temperature the button label is automatically updated

import lvgl as lv
import display_driver
import time

class TempButton(lv.btn):

    def __init__(self,parent):
        self.label=None
        self.temp=30          # current temperature value
        super().__init__(parent)
        print("temp: ",self.temp)
        self.old_btn_design_cb = parent.get_design_cb()
        if callable(self.old_btn_design_cb):
            print("old_btn_design_cb is callable")
        else:
            print("old_btn_design_cb is not callable")
        
        self.set_design_cb(self.new_btn_design)
        print("new design callback set")
        
    def set_temp(self,temp):
        self.temp=temp
        self.invalidate()
        
    def new_btn_design(self,btn,clip_area,mode):
        print(btn)
        print("Clip area: ",clip_area)
        print("mode: ",mode)
        if mode == lv.DESIGN.COVER_CHK:
            return lv.DESIGN_RES.NOT_COVER
        if mode == lv.DESIGN.DRAW_MAIN:
            self.old_btn_design_cb(self,clip_area,mode)
            print("parent successfully redrawn")
        # Draw a label
        temp_txt= "Temp: %d °C" %self.temp
        print("temp text: " + temp_txt)
        if self.label:
            self.label.delete()
        self.label=lv.label(btn,None)
        print("label created")
        self.label.set_text(temp_txt) 
        print("new_btn_design done")
        return lv.RES.OK
        
btn = TempButton(lv.scr_act())
temperature = 25
for i in range(10):
    btn.set_temp(temperature)
    temperature += 1
    time.sleep(1)

