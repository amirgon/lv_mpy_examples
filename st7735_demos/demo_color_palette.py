#!//opt/bin/lv_micropython -i
"""ST7735 demo (color palette) running on lvgl."""
import lvgl as lv
import display_driver
from utime import sleep
from math import cos, sin, pi, radians, floor
from lv_colors import lv_colors,LV_COLOR_MAKE
disp = lv.scr_act().get_disp()
CANVAS_WIDTH = disp.driver.hor_res
CANVAS_HEIGHT = disp.driver.ver_res
    
def hsv_to_rgb(h, s, v):
    """
    Convert HSV to RGB (based on colorsys.py).

        Args:
            h (float): Hue 0 to 1.
            s (float): Saturation 0 to 1.
            v (float): Value 0 to 1 (Brightness).
    """
    if s == 0.0:
        return v, v, v
    i = int(h * 6.0)
    f = (h * 6.0) - i
    p = v * (1.0 - s)
    q = v * (1.0 - s * f)
    t = v * (1.0 - s * (1.0 - f))
    i = i % 6

    v = int(v * 255)
    t = int(t * 255)
    p = int(p * 255)
    q = int(q * 255)

    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q

def draw_filledCircle(canvas, x0, y0, r, color):
    """Draw a filled circle.

        Args:
            x0 (int): X coordinate of center point.
            y0 (int): Y coordinate of center point.
            r (int): Radius.
            color (int): RGB565 color value.
    """
    # print("Draw filled circle: x0: %d, y0: %d, r: %d" % (x0, y0, r))
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
    # print("x1: %d, y1: %d, x2: %d, y2: %d" % (p1.x,p1.y,p2.x,p2.y))
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


def test():
    """Test code."""
    # create a canvas
    cbuf=bytearray(CANVAS_WIDTH * CANVAS_HEIGHT * 4)
    canvas = lv.canvas(lv.scr_act(),None)
    canvas.set_buffer(cbuf,CANVAS_WIDTH,CANVAS_HEIGHT,lv.img.CF.TRUE_COLOR)
    canvas.align(None,lv.ALIGN.CENTER,0,0)
    radius = CANVAS_HEIGHT//16
    offset = (CANVAS_WIDTH-CANVAS_HEIGHT)//2
    c = 0
    for x in range(0, CANVAS_HEIGHT, 2*radius):
        for y in range(0, CANVAS_HEIGHT, 2*radius):
            color = LV_COLOR_MAKE(*hsv_to_rgb(c / 64, 1, 1))
            draw_filledCircle(canvas,x+radius+offset ,y+radius, radius, color)
            c += 1

test()
