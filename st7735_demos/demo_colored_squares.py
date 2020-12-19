#!/opt/bin/lv_micropython -i
import lvgl as lv
import display_driver
import time
import math
from lv_colors import lv_colors, LV_COLOR_MAKE

CANVAS_WIDTH  = 240
CANVAS_HEIGHT = 240

DARKGREEN = LV_COLOR_MAKE (0, 128, 0)
DEEP_PINK = LV_COLOR_MAKE (255, 0, 128)
CHARTREUSE = LV_COLOR_MAKE (128, 255, 0)
SPRING_GREEN = LV_COLOR_MAKE (0, 255, 128)
INDIGO = LV_COLOR_MAKE (128, 0, 255)
DODGER_BLUE = LV_COLOR_MAKE (0, 128, 255)
PINK = LV_COLOR_MAKE (255, 128, 255)
LIGHT_YELLOW = LV_COLOR_MAKE (255, 255, 128)
LIGHT_CORAL = LV_COLOR_MAKE (255, 128, 128)
LIGHT_GREEN = LV_COLOR_MAKE (128, 255, 128)
LIGHT_SLATE_BLUE = LV_COLOR_MAKE (128, 128, 255)


colors= [lv_colors.RED,lv_colors.GREEN,lv_colors.BLUE,lv_colors.YELLOW,
         lv_colors.MAGENTA,lv_colors.AQUA,lv_colors.MAROON,DARKGREEN,
         lv_colors.NAVY,lv_colors.TEAL,lv_colors.PURPLE,lv_colors.OLIVE,
         lv_colors.ORANGE,DEEP_PINK,CHARTREUSE,SPRING_GREEN,
         INDIGO,DODGER_BLUE,lv_colors.CYAN,PINK,LIGHT_YELLOW,LIGHT_CORAL,LIGHT_GREEN,
         LIGHT_SLATE_BLUE,lv_colors.WHITE]

def test():    
    """Test code."""
    cbuf=bytearray(CANVAS_WIDTH * CANVAS_HEIGHT * 4)
    # create a canvas
    canvas = lv.canvas(lv.scr_act(),None)
    canvas.set_buffer(cbuf,CANVAS_WIDTH,CANVAS_HEIGHT,lv.img.CF.TRUE_COLOR)
    canvas.align(None,lv.ALIGN.CENTER,0,0)
    
    c = 0
    rect_dsc = lv.draw_rect_dsc_t()
    rect_dsc.init()
    rect_dsc.bg_opa = lv.OPA.COVER

    for x in range(0, CANVAS_WIDTH, 48):
        for y in range(0, CANVAS_HEIGHT, 48):
            rect_dsc.bg_color = colors[c]
            canvas.draw_rect(x, y, 48, 48, rect_dsc)
            c += 1
    time.sleep(9)

test()
