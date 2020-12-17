#!//opt/bin/lv_micropython
"""SSD1351 demo (shapes)."""

import lvgl as lv
import display_driver
from utime import sleep
from math import cos, sin, pi, radians, floor
from lv_colors import lv_colors,LV_COLOR_MAKE
disp = lv.scr_act().get_disp()
CANVAS_WIDTH = disp.driver.hor_res
CANVAS_HEIGHT = disp.driver.ver_res
print("canvas width: %d, canvas_height: %d"%(CANVAS_WIDTH,CANVAS_HEIGHT))

def clear(color=lv_colors.BLACK):
    canvas.fill_bg(color, lv.OPA.COVER)

def draw_lines(canvas,points,color):
    line_dsc = lv.draw_line_dsc_t()
    line_dsc.init()
    line_dsc.color = color
    line_dsc.opa = lv.OPA.COVER
    
    print(len(points))
    for i in range(len(points)-1):
        point_array = [points[i],points[i+1]]
        canvas.draw_line(point_array,2,line_dsc)
        
def draw_filledCircle(canvas, x0, y0, r, color):
    """Draw a filled circle.

        Args:
            x0 (int): X coordinate of center point.
            y0 (int): Y coordinate of center point.
            r (int): Radius.
            color (int): RGB565 color value.
    """
    print("Draw filled circle: x0: %d, y0: %d, r: %d" % (x0, y0, r))
    f = 1 - r
    dx = 1
    dy = -r - r
    x = 0
    y = r
    line_dsc = lv.draw_line_dsc_t()
    line_dsc.init()
    line_dsc.color = color
    line_dsc.opa = lv.OPA.COVER
    p1=lv.point_t()
    p2=lv.point_t()
    point_array=[p1,p2]
    p1.x = x0
    p1.y = y0 - r
    p2.x = p1.x 
    p2.y = p1.y + 2 * r + 1
    print("x1: %d, y1: %d, x2: %d, y2: %d" % (p1.x,p1.y,p2.x,p2.y))
    canvas.draw_line(point_array, 2, line_dsc)
    while x < y:
        if f >= 0:
            y -= 1
            dy += 2
            f += dy
        x += 1
        dx += 2
        f += dx
        p1.x = x0 + x
        p1.y = y0 - y
        p2.x = p1.x
        p2.y = p1.y + 2 * y + 1
        canvas.draw_line(point_array,2,line_dsc)
        p1.x = x0 - x
        p2.x = p1.x
        canvas.draw_line(point_array,2,line_dsc)
        p1.x = x0 - y
        p1.y = y0 - x
        p2.x = p1.x 
        p2.y = p1.y + 2 * x + 1
        canvas.draw_line(point_array,2,line_dsc)
        p1.x = x0 + y
        p2.x = p1.x
        canvas.draw_line(point_array,2,line_dsc)

def draw_ellipse(canvas, x0, y0, a, b, color):
    """Draw an ellipse.
    
       Args:
            x0, y0 (int): Coordinates of center point.
            a (int): Semi axis horizontal.
            b (int): Semi axis vertical.
            color (int): RGB565 color value.
        Note:
            The center point is the center of the x0,y0 pixel.
            Since pixels are not divisible, the axes are integer rounded
            up to complete on a full pixel.  Therefore the major and
            minor axes are increased by 1.
    """
    a2 = a * a
    b2 = b * b
    twoa2 = a2 + a2
    twob2 = b2 + b2
    x = 0
    y = b
    px = 0
    py = twoa2 * y
    # Plot initial points
    canvas.set_px(x0 + x, y0 + y, color)
    canvas.set_px(x0 - x, y0 + y, color)
    canvas.set_px(x0 + x, y0 - y, color)
    canvas.set_px(x0 - x, y0 - y, color)
    # Region 1
    p = round(b2 - (a2 * b) + (0.25 * a2))
    while px < py:
        x += 1
        px += twob2
        if p < 0:
            p += b2 + px
        else:
            y -= 1
            py -= twoa2
            p += b2 + px - py
        canvas.set_px(x0 + x, y0 + y, color)
        canvas.set_px(x0 - x, y0 + y, color)
        canvas.set_px(x0 + x, y0 - y, color)
        canvas.set_px(x0 - x, y0 - y, color)
    # Region 2
    p = round(b2 * (x + 0.5) * (x + 0.5) +
              a2 * (y - 1) * (y - 1) - a2 * b2)
    while y > 0:
        y -= 1
        py -= twoa2
        if p > 0:
            p += a2 - py
        else:
            x += 1
            px += twob2
            p += a2 - py + px
        canvas.set_px(x0 + x, y0 + y, color)
        canvas.set_px(x0 - x, y0 + y, color)
        canvas.set_px(x0 + x, y0 - y, color)
        canvas.set_px(x0 - x, y0 - y, color)

def draw_filledEllipse(canvas, x0, y0, a, b, color):
    """Draw a filled ellipse.

       Args:
            x0, y0 (int): Coordinates of center point.
            a (int): Semi axis horizontal.
            b (int): Semi axis vertical.
            color (int): RGB565 color value.
        Note:
            The center point is the center of the x0,y0 pixel.
            Since pixels are not divisible, the axes are integer rounded
            up to complete on a full pixel.  Therefore the major and
            minor axes are increased by 1.
    """
    a2 = a * a
    b2 = b * b
    twoa2 = a2 + a2
    twob2 = b2 + b2
    x = 0
    y = b
    px = 0
    py = twoa2 * y
    # Plot initial points
    line_dsc = lv.draw_line_dsc_t()
    line_dsc.init()
    line_dsc.color = color
    line_dsc.opa = lv.OPA.COVER
    p1=lv.point_t()
    p2=lv.point_t()
    point_array=[p1,p2]
    p1.x = x0
    p1.y = y0 - y
    p2.x = x0
    p2.y = y0 + y
    canvas.draw_line(point_array, 2, line_dsc)
    # Region 1
    p = round(b2 - (a2 * b) + (0.25 * a2))
    while px < py:
        x += 1
        px += twob2
        if p < 0:
            p += b2 + px
        else:
            y -= 1
            py -= twoa2
            p += b2 + px - py
        p1.x = x0 + x
        p1.y = y0 - y
        p2.x = p1.x
        p2.y = y0 + y
        canvas.draw_line(point_array, 2, line_dsc)
        p1.x = x0 - x
        p2.x = p1.x
        canvas.draw_line(point_array, 2, line_dsc)
    # Region 2
    p = round(b2 * (x + 0.5) * (x + 0.5) +
              a2 * (y - 1) * (y - 1) - a2 * b2)
    while y > 0:
        y -= 1
        py -= twoa2
        if p > 0:
            p += a2 - py
        else:
            x += 1
            px += twob2
            p += a2 - py + px
        p1.x = x0 + x
        p1.y = y0 - y
        p2.x = p1.x
        p2.y = y0 + y
        canvas.draw_line(point_array, 2, line_dsc)
        p1.x = x0 - x
        p2.x = p1.x
        canvas.draw_line(point_array, 2, line_dsc)
            
def test(canvas):
    """Test code."""
    print('display started')
    #
    # green background
    # 
    clear(lv_colors.GREEN)
    sleep(1)
    clear()
    #
    # colored lines and filled rectangle
    #
    p1=lv.point_t()
    p2=lv.point_t()
    point_array=[p1,p2]
    
    line_dsc = lv.draw_line_dsc_t()
    line_dsc.init()
    line_dsc.color = lv_colors.MAGENTA
    line_dsc.opa = lv.OPA.COVER

    p1.x = 10
    p1.y = CANVAS_HEIGHT-1
    p2.x = p1.x + CANVAS_WIDTH //2
    p2.y = p1.y
    canvas.draw_line(point_array, 2, line_dsc)
    sleep(1)

    p1.y = 0
    p2.x = p1.x
    p2.y = CANVAS_HEIGHT-1
    line_dsc.color = lv_colors.CYAN
    canvas.draw_line(point_array, 2, line_dsc)
    sleep(1)
    
    rect_dsc = lv.draw_rect_dsc_t()
    rect_dsc.init()
    rect_dsc.bg_opa = lv.OPA.COVER
    rect_dsc.bg_color = lv_colors.WHITE

    canvas.draw_rect(round(CANVAS_WIDTH/5.56),round(CANVAS_HEIGHT/2.56),
                     round(CANVAS_WIDTH/4.2),round(CANVAS_HEIGHT/1.7),rect_dsc)
    sleep(1)

    p1.x = 0
    p1.y = 0
    p2.x = CANVAS_WIDTH-1
    p2.y = p1.y
    line_dsc.color = lv_colors.RED
    canvas.draw_line(point_array, 2, line_dsc)
    
    sleep(1)
    p1.x = CANVAS_WIDTH-1
    p1.y = 0
    p2.x = CANVAS_WIDTH//2
    p2.y = CANVAS_HEIGHT
    line_dsc.color = lv_colors.YELLOW
    canvas.draw_line(point_array, 2, line_dsc)
    sleep(1)
    clear() 
    #
    # line polygon
    #
    coords = [{"x":0,                        "y":round(CANVAS_HEIGHT*0.65)},
              {"x":round(CANVAS_WIDTH*0.52), "y":round(CANVAS_HEIGHT*0.83)},
              {"x":round(CANVAS_WIDTH*0.95), "y":round(CANVAS_HEIGHT*0.96)},
              {"x":round(CANVAS_WIDTH*0.41), "y":round(CANVAS_HEIGHT*0.52)},
              {"x":round(CANVAS_WIDTH*0.61), "y":round(CANVAS_HEIGHT*0.15)},
              {"x":0,                        "y":round(CANVAS_HEIGHT*0.65)}]
    
    draw_lines(canvas,coords,lv_colors.YELLOW)
    sleep(1)
    clear()
    #
    # filled polygon and filled rectangle
    #
    offset = (CANVAS_WIDTH-CANVAS_HEIGHT)//2 
    sides = 7
    rotate = 0
    x0 = CANVAS_HEIGHT//2    # center position
    y0 = x0
    r = 3*CANVAS_HEIGHT//8   # radius
    theta = radians(rotate)
    n = sides + 1
    point_array=[]
    for s in range(n):
        t = 2.0 * pi * s / sides + theta
        point = lv.point_t()
        point.x = int(r * cos(t) + x0) + offset
        point.y = int(r * sin(t) + y0)
        point_array.append(point)
        
        # coords.append([int(r * cos(t) + x0), int(r * sin(t) + y0)])
        
    rect_dsc.bg_color = lv_colors.GREEN
    canvas.draw_polygon(point_array,8,rect_dsc)
    rect_dsc.bg_color = lv_colors.RED        
    canvas.draw_rect(0, 0, 30, 239, rect_dsc)
    sleep(1)
    clear()
    #
    # rectangles and triangle
    #
    offset = (CANVAS_WIDTH-CANVAS_HEIGHT)//2
    rect_dsc.bg_color=LV_COLOR_MAKE(128, 128, 255)
    # print("x1: %d, y1: %d, w: %d, h: %d" %(offset, 0, CANVAS_HEIGHT//2 - 1, CANVAS_HEIGHT//2-1))
    canvas.draw_rect(offset, 0, CANVAS_HEIGHT//2-1, CANVAS_HEIGHT//2-1,
                       rect_dsc)
    sleep(1)

    rect_dsc.bg_color=lv_colors.MAGENTA
    # print("x1: %d, y1: %d, w: %d, h: %d" %(offset+CANVAS_HEIGHT//2, 0, CANVAS_HEIGHT//2 -1, CANVAS_HEIGHT//2-1))
    canvas.draw_rect(offset+CANVAS_HEIGHT//2, 0, CANVAS_HEIGHT//2-1, CANVAS_HEIGHT//2-1,
                       rect_dsc)
    sleep(1)
    
    rect_dsc.bg_color=lv_colors.BLACK
    rect_dsc.bg_opa = lv.OPA.TRANSP
    rect_dsc.border_width = 2
    rect_dsc.border_color = lv_colors.MAGENTA
    rect_dsc.border_opa = lv.OPA.COVER
    # print("x1: %d, y1: %d, w: %d, h: %d" %(offset, CANVAS_HEIGHT//2, CANVAS_HEIGHT//2-1, CANVAS_HEIGHT//2-1))    
    canvas.draw_rect(offset, CANVAS_HEIGHT//2, CANVAS_HEIGHT//2-1, CANVAS_HEIGHT//2-1,
                       rect_dsc)
    sleep(1)
    
    sides = 3
    x0 = 3*CANVAS_HEIGHT//4          # center position
    y0 = 3*CANVAS_HEIGHT//4
    r = round(0.233*CANVAS_HEIGHT)   # radius
    rotate = 15
    # print("triangle center x: %d, y: %d" %(x0,y0))
    theta = radians(rotate)
    n = sides + 1
    point_array=[]    
    for s in range(n):
        t = 2.0 * pi * s / sides + theta
        point = lv.point_t()
        point.x = int(r * cos(t) + x0) + offset
        point.y = int(r * sin(t) + y0)
        # print("point: x: %d, y: %d" % (point.x,point.y))
        point_array.append(point)

    line_dsc.color = LV_COLOR_MAKE(0, 64, 255)
    for i in range(sides):
        # print("x0: %d, y0: %d, x1: %d, y1: %d" % (point_array[0].x,point_array[0].y,
        #                                           point_array[1].x,point_array[1].y))
        canvas.draw_line(point_array,2,line_dsc)
        point_array.pop(0)
    sleep(1)
    clear()
    #
    # circles and ellipses
    #
    draw_filledCircle(canvas,CANVAS_HEIGHT//4 + offset -1, CANVAS_HEIGHT//4 -1, CANVAS_HEIGHT//4 - 5,
                      lv_colors.GREEN)
    sleep(1)
    
    line_dsc.color = lv_colors.BLUE
    canvas.draw_arc(CANVAS_HEIGHT//4 + offset -1, 3*CANVAS_HEIGHT//4 -1 , CANVAS_HEIGHT//4 - 5, 0, 360, line_dsc)
    sleep(1)
    
    draw_filledEllipse(canvas, 3* CANVAS_HEIGHT//4 + offset -1, CANVAS_HEIGHT//4 -1, CANVAS_HEIGHT//4 - 5, CANVAS_HEIGHT//8 , lv_colors.RED)
    sleep(1)

    draw_ellipse(canvas, 3*CANVAS_HEIGHT//4 + offset -1, 3*CANVAS_HEIGHT//4 -1, CANVAS_HEIGHT//4 - 5, CANVAS_HEIGHT//8, lv_colors.YELLOW)

    sleep(5)


cbuf=bytearray(CANVAS_WIDTH * CANVAS_HEIGHT * 4)

# create a canvas
canvas = lv.canvas(lv.scr_act(),None)
canvas.set_buffer(cbuf,CANVAS_WIDTH,CANVAS_HEIGHT,lv.img.CF.TRUE_COLOR)
canvas.align(None,lv.ALIGN.CENTER,0,0)
test(canvas)
