#!/opt/bin/lv_micropython -i
# change the above to the path of your lv_micropython -i unix binary
import sys
#
# initialize lvgl
#
import lvgl as lv
import display_driver
from lv_colors import lv_colors

SDL     = 0
ILI9341 = 1
# create the cogwheel image data
try:
    with open('../assets/img_cogwheel_argb8888.bin','rb') as f:
        cogwheel_img_data = f.read()
        driver = SDL
except:
    try:
        with open('images/img_cogwheel_rgb565.bin','rb') as f:
            cogwheel_img_data = f.read()
            driver = ILI9341
    except:
        print("Could not find img_cogwheel_xxx.bin")
        sys.exit()
        
if driver == SDL:
    cogwheel_img_dsc = lv.img_dsc_t(
        {
            "header": {"always_zero": 0, "w": 100, "h": 100, "cf": lv.img.CF.TRUE_COLOR_ALPHA},
            "data": cogwheel_img_data,
            "data_size": len(cogwheel_img_data),
        }
    )
else:
    cogwheel_img_dsc = lv.img_dsc_t(
        {
            "header": {"always_zero": 0, "w": 100, "h": 100, "cf": lv.img.CF.TRUE_COLOR},
            "data": cogwheel_img_data,
            "data_size": len(cogwheel_img_data),
        }
    )    
style = lv.style_t()
style.init()
# Set a background color and a radius
style.set_radius(lv.STATE.DEFAULT, 5)
style.set_bg_opa(lv.STATE.DEFAULT, lv.OPA.COVER)
style.set_bg_color(lv.STATE.DEFAULT, lv_colors.SILVER)
style.set_border_width(lv.STATE.DEFAULT, 2)
style.set_border_color(lv.STATE.DEFAULT, lv_colors.BLUE)
style.set_pad_top(lv.STATE.DEFAULT, 10)
style.set_pad_bottom(lv.STATE.DEFAULT, 10)
style.set_pad_left(lv.STATE.DEFAULT, 10)
style.set_pad_right(lv.STATE.DEFAULT, 10)

style.set_image_recolor(lv.STATE.DEFAULT, lv_colors.BLUE)
style.set_image_recolor_opa(lv.STATE.DEFAULT, lv.OPA._50)

# Create an object with the new style
obj = lv.img(lv.scr_act(), None)
lv.img.cache_set_size(2)

obj.add_style(lv.img.PART.MAIN, style)
obj.set_src(cogwheel_img_dsc)
obj.align(None, lv.ALIGN.CENTER, 0, 0)

