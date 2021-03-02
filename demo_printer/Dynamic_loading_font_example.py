#!/opt/bin/lv_micropython -i
#
# Command line for running this example on the unix port from examples directory:
# MICROPYPATH=./:../lib ../../../ports/unix/micropython -i Dynamic_loading_font_example.py
#

import lvgl as lv
import fs_driver

lv.init()

# display driver init...

import display_driver # Default implementation. Replace by your driver


scr = lv.scr_act()
# scr.clean()

myfont_en = lv.font_load("font/font-PHT-en-20.bin")
print(myfont_en)
style2 = lv.style_t()
style2.init()

label2 = lv.label(scr)
style2.set_text_font(lv.STATE.DEFAULT, myfont_en)  # set font
label2.add_style(label2.PART.MAIN, style2)

label2.set_text("Hello LVGL!")
label2.align(None, lv.ALIGN.CENTER, 0, 0)
