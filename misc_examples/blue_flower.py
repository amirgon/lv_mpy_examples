#!/opt/bin/lv_micropython
import lvgl as lv
import init_gui
import time,sys

# Display a raw image

try:
  with open('blue_flower_32.bin','rb') as f:
    img_data = f.read()
except:
  try:
    with open('images/img_hand_rgb565.bin','rb') as f:
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

while True:
    lv.task_handler()
    time.sleep_ms(5)

