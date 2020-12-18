#!/opt/bin/lv_micropython -i -i
import lvgl as lv
import display_driver
import time,sys

# Display a raw image

try:
  with open('../assets/blue_flower_argb.bin','rb') as f:
    img_data = f.read()
except:
  try:
    with open('images/blue_flower_rgb565.bin','rb') as f:
      img_data = f.read()
  except:
    print("Could not open image file")
    sys.exit()
    
scr = lv.scr_act()
img = lv.img(scr)
img.align(scr, lv.ALIGN.CENTER, 0, 0)
img_dsc = lv.img_dsc_t(
    {
        "header": {"always_zero": 0, "w": 100, "h": 75, "cf": lv.img.CF.TRUE_COLOR_ALPHA},
        "data_size": len(img_data),
        "data": img_data,
    }
)

img.set_src(img_dsc)
img.set_drag(True)


