#!//opt/ucc/micros/esp32/lv_micropython/ports/unix/lv_micropython
import lvgl as lv
import init_gui
import time
from l_colors import *

CANVAS_WIDTH  = 240
CANVAS_HEIGHT = 240
    
rect_dsc = lv.draw_rect_dsc_t()
rect_dsc.init()
rect_dsc.radius = 10
rect_dsc.bg_opa = lv.OPA.COVER
rect_dsc.bg_grad_dir = lv.GRAD_DIR.HOR
rect_dsc.bg_color = LV_COLOR_RED;
rect_dsc.bg_grad_color = LV_COLOR_BLUE
rect_dsc.border_width = 2
rect_dsc.border_opa = lv.OPA._90
rect_dsc.border_color = LV_COLOR_WHITE
rect_dsc.shadow_width = 5
rect_dsc.shadow_ofs_x = 5
rect_dsc.shadow_ofs_y = 5

line_dsc = lv.draw_line_dsc_t()
line_dsc.init()
line_dsc.color = LV_COLOR_BLACK;
line_dsc.opa = lv.OPA.COVER

def clear():
    canvas.fill_bg(LV_COLOR_BLACK, lv.OPA.COVER)

def testlines(canvas,color):
    print("Test lines")
    p1=lv.point_t()
    p2=lv.point_t()
    line_dsc = lv.draw_line_dsc_t()
    line_dsc.init()
    line_dsc.color = color;
    line_dsc.opa = lv.OPA.COVER
    
    clear()
    
    # from top left corner
    for x in range(0, CANVAS_WIDTH, 6):
        p1.x = 0
        p1.y = 0
        p2.x = x
        p2.y = CANVAS_HEIGHT - 1
        point_array=[p1,p2]
        canvas.draw_line(point_array,2,line_dsc)
        
        for y in range(0, CANVAS_HEIGHT, 6):
            p2.x = CANVAS_WIDTH- 1
            p2.y = y
            canvas.draw_line(point_array,2,line_dsc)
        time.sleep(1)
        clear()
        
        # from bottom left corner
        for x in range(0, CANVAS_WIDTH, 6):
            p1.x = 0
            p1.y = CANVAS_HEIGHT- 1
            p2.x = x
            p2.y = 0
            canvas.draw_line(point_array,2,line_dsc)

        for y in range(0, CANVAS_HEIGHT, 6):
            p2.x = CANVAS_WIDTH- 1
            p2.y = y
            canvas.draw_line(point_array,2,line_dsc)
            
        time.sleep(1)
        clear()

        # from bottom right corner 
        for x in range(0, CANVAS_WIDTH, 6):
            p1.x = CANVAS_WIDTH-1
            p1.y = CANVAS_HEIGHT-1
            p2.x = x
            p2.y = 0
            canvas.draw_line(point_array,2,line_dsc)

        for y in range(0, CANVAS_HEIGHT, 6):
            p2.x = 0
            p2.y = y
            canvas.draw_line(point_array,2,line_dsc)
            
        time.sleep(1)
        clear()

        # from top right corner
        for x in range(0, CANVAS_WIDTH, 6):
            p1.x = CANVAS_WIDTH-1
            p1.y = 0
            p2.x = x
            p2.y = CANVAS_HEIGHT-1
            canvas.draw_line(point_array,2,line_dsc)

        for y in range(0, CANVAS_HEIGHT, 6):
            p2.x = 0
            p2.y = y
            canvas.draw_line(point_array,2,line_dsc)
            
    cbuf=bytearray(CANVAS_WIDTH * CANVAS_HEIGHT * 4)
        
    # create a canvas
    canvas = lv.canvas(lv.scr_act(),None)
    canvas.set_buffer(cbuf,CANVAS_WIDTH,CANVAS_HEIGHT,lv.img.CF.TRUE_COLOR)
    canvas.align(None,lv.ALIGN.CENTER,0,0)

    # test lines
    testlines(canvas,LV_COLOR_GREEN)
    
while True:
    pass
