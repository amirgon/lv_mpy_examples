#!/opt/bin/lv_micropython -i
import lvgl as lv
from display_driver_utils import driver,ORIENT_PORTRAIT
import time,sys
from os import stat
from lv_colors import lv_colors
from math import sqrt
from random import randint, seed
from utime import sleep_us, ticks_ms, ticks_us, ticks_diff
from micropython import const
driver(width=240,height=320,orientation=ORIENT_PORTRAIT)

# Display a raw image
SDL     = 0
ILI9341 = 1

SCREEN_WIDTH = lv.scr_act().get_disp().driver.hor_res
SCREEN_HEIGHT = lv.scr_act().get_disp().driver.ver_res
print("screen height: ",SCREEN_HEIGHT)
LV_ANIM_REPEAT_INFINITE = -1

def draw_background():
    try:
        with open('arkanoid_images/frame_top_240x10_argb8888.bin','rb') as f:
            frame_top_data = f.read()
            print("'arkanoid_images/frame_top_240x10_argb8888.bin successfully read")
            driver = SDL
    except:
        try:
            with open('images/frame_top_240x10_rgb565.bin','rb') as f:
                frame_top_data = f.read()
                print("images/frame_top_240x10_rgb565.bin successfully read")
                driver = ILI9341
        except:
            print("Could not open frame_top image file")
            sys.exit()

    try:
        with open('arkanoid_images/frame_right_9x310_argb8888.bin','rb') as f:
            frame_right_data = f.read()
            print("'arkanoid_images/frame_right_9x310_argb8888.bin successfully read")
    except:
        try:
            with open('images/frame_right_9x310_rgb565.bin','rb') as f:
                frame_right_data = f.read()
                print("images/frame_right_9x310_rgb565.bin successfully read")
        except:
            print("Could not open frame right image file")
            sys.exit()

    try:
        with open('arkanoid_images/frame_left_9x310_argb8888.bin','rb') as f:
            frame_left_data = f.read()
            print("'arkanoid_images/frame_left_9x310_argb8888.bin successfully read")
    except:
        try:
            with open('images/frame_left_9x310_rgb565.bin','rb') as f:
                frame_left_data = f.read()
                print("images/frame_left_9x310_rgb565.bin successfully read")
        except:
            print("Could not open frame left image file")
            sys.exit()


    scr_style = lv.style_t()
    scr_style.set_bg_color(lv.STATE.DEFAULT, lv_colors.BLACK)
    lv.scr_act().add_style(lv.obj.PART.MAIN,scr_style)

    frame_top_img = lv.img(lv.scr_act(),None)
    frame_top_img.set_x(0)
    frame_top_img.set_y(30)
    if driver == SDL:
        frame_top_img_dsc = lv.img_dsc_t(
            {
                "header": {"always_zero": 0, "w": 240, "h": 10, "cf": lv.img.CF.TRUE_COLOR_ALPHA},
                "data_size": len(frame_top_data),
                "data": frame_top_data,
            }
        )
    else:
        frame_top_img_dsc = lv.img_dsc_t(
            {
                "header": {"always_zero": 0, "w": 240, "h": 10, "cf": lv.img.CF.TRUE_COLOR},
                "data_size": len(frame_top_data),
                "data": frame_top_data,
            }
        )    
        
    frame_left_img = lv.img(lv.scr_act(),None)
    frame_left_img.set_x(0)
    frame_left_img.set_y(40)
    if driver == SDL:
        frame_left_img_dsc = lv.img_dsc_t(
            {
                "header": {"always_zero": 0, "w": 9, "h": 310, "cf": lv.img.CF.TRUE_COLOR_ALPHA},
                "data_size": len(frame_left_data),
                "data": frame_left_data,
            }
        )
    else:
        frame_left_img_dsc = lv.img_dsc_t(
            {
                "header": {"always_zero": 0, "w": 9, "h": 310, "cf": lv.img.CF.TRUE_COLOR},
                "data_size": len(frame_left_data),
                "data": frame_left_data,
            }
        )    
    frame_right_img = lv.img(lv.scr_act(),None)
    frame_right_img.set_x(231)
    frame_right_img.set_y(40)
    if driver == SDL:
        frame_right_img_dsc = lv.img_dsc_t(
            {
                "header": {"always_zero": 0, "w": 9, "h": 310, "cf": lv.img.CF.TRUE_COLOR_ALPHA},
                "data_size": len(frame_right_data),
                "data": frame_right_data,
            }
        )
    else:
        frame_right_img_dsc = lv.img_dsc_t(
            {
                "header": {"always_zero": 0, "w": 9, "h": 310, "cf": lv.img.CF.TRUE_COLOR},
                "data_size": len(frame_right_data),
                "data": frame_right_data,
            }
        )    
    
    frame_top_img.set_src(frame_top_img_dsc)
    frame_left_img.set_src(frame_left_img_dsc)
    frame_right_img.set_src(frame_right_img_dsc)
    print("Background Done")

brick_colors = ['Red','Yellow', 'Blue', 'Pink', 'Green']
bricks = [None]*len(brick_colors)
brick_img_dsc = [None]*len(brick_colors)
   
def create_brick_img_dscs(w=26,h=14):
    
    for index in range(len(brick_colors)):
        
        filename_argb8888 = 'Brick_' + brick_colors[index] + '26x14_argb8888.bin'
        filename_rgb656 = 'Brick_' + brick_colors[index] + '26x14_rgb565.bin'
        
        print("Filenames: %s %s"%('arkanoid_images/'+filename_argb8888,'images/'+filename_rgb656))
        try:
            with open('arkanoid_images/'+filename_argb8888,'rb') as f:
                brick_data = f.read()
            print('arkanoid_images/'+filename_argb8888 + ' successfully read')
            driver=SDL
        except:
            try:
                with open('images/'+ filename_rgb656,'rb') as f:
                    brick_data = f.read()
                print("images/" + filename_rgb656 + " successfully read")
                driver = ILI9341
            except:
                print("Could not open Brick "+ brick_colors[index] +"image file")
                sys.exit()
            
        if driver == SDL:
            brick_img_dsc[index] = lv.img_dsc_t(
                {
                    "header": {"always_zero": 0, "w": w, "h": h, "cf": lv.img.CF.TRUE_COLOR_ALPHA},
                    "data_size": len(brick_data),
                    "data": brick_data,
                }
            )
        else:
            brick_img_dsc[index] = lv.img_dsc_t(
                {
                    "header": {"always_zero": 0, "w": w, "h": h, "cf": lv.img.CF.TRUE_COLOR},
                    "data_size": len(brick_data),
                    "data": brick_data,
                }
            )
        
def load_level(level):
    """Load level brick coordinates and colors from bin file.

    Notes:
        Level file consists of 5 values for each brick:
            x, y, x2, y2, color(index)
    """
    bricks = []
    brick_colors = ['Red', 'Yellow', 'Blue', 'Pink', 'Green']
    path = 'levels/Level{0:03d}.asc'.format(level)
    level = []
    f= open(path, 'rb')
    i=0
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i].split()
        index =  brick_colors.index(line[2].decode('uft-8'))
        level.append((int(line[0]),int(line[1]),index))
        brick = Brick(level[i][0],level[i][1],level[i][2])
        i+=1
        bricks.append(brick)
    f.close()
    
    return bricks
    
class Ball():
    """Ball."""

    def __init__(self, x, y, x_speed, y_speed, w=14, h=14,
                 frozen=False):
        """Initialize ball.

        Args:
            x, y (int):  X,Y coordinates.
            x_speed, y_speed (int):  Initial XY speeds.
            w (Optional int): Ball width (default 7).
            h (Optional int): Ball height (default 7).
            frozen (boolean): Indicates if ball is frozen (default false).
        """
        self.x = x
        self.y = y
        self.x2 = x + w - 1
        self.y2 = y + h - 1
        # self.x2 = x - 1
        # self.y2 = y - 1
        print("ball x2: %d, y2: %d"%(self.x2,self.y2))
        self.prev_x = x
        self.prev_y = y
        self.width = w
        self.height = h
        self.center = w // 2
        self.max_x_speed = 5
        self.max_y_speed = 5
        self.frozen = frozen
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.x_speed2 = 0.0
        self.y_speed2 = 0.0
        self.created = ticks_ms()
        print("created: %d"%self.created)
        try:
            with open('arkanoid_images/Ball14x14_argb8888.bin','rb') as f:
                ball_data = f.read()
            print('arkanoid_images/Ball14x14_argb8888.bin successfully read')
            driver=SDL
        except:
            try:
                with open('images/Ball14x14_rgb565.bin','rb') as f:
                    ball_data = f.read()
                print('images/Ball14x14_rgb565.bin successfully read')
                driver = ILI9341
            except:
                print('Could not open ball image file')
                sys.exit()
        
        if driver == SDL:
            ball_dsc = lv.img_dsc_t(
                {
                    "header": {"always_zero": 0, "w": w, "h": h, "cf": lv.img.CF.TRUE_COLOR_ALPHA},
                    "data_size": len(ball_data),
                    "data": ball_data,
                }
            )
        else:
            ball_dsc = lv.img_dsc_t(
                {
                    "header": {"always_zero": 0, "w": w, "h": h, "cf": lv.img.CF.TRUE_COLOR},
                    "data_size": len(ball_data),
                    "data": ball_data,
                }
            )
            
        self.ball_img = lv.img(lv.scr_act())
        self.ball_img.set_src(ball_dsc)
        self.ball_img.set_x(self.x)
        self.ball_img.set_y(self.y)

    def clear(self):
        """Clear ball."""
        self.ball_img.delete()
    
    def set_position(self, paddle_x, paddle_y, paddle_width):
        """Set ball position."""
        paddle_x2 = paddle_x + paddle_width
        paddle_center = paddle_width//2
        self.prev_x = self.x
        self.prev_y = self.y
        print("set_position: paddle_x: %d, paddle_y: %d paddle_width: %d"%(paddle_x,paddle_y,paddle_width))
        # Check if frozen to paddle
        if self.frozen:

            # Freeze ball to top center of paddle
            self.x = paddle_x +  paddle_center - self.center + 10
            # self.y = paddle_y - self.height
            print("paddle x: %d, paddle_center: %d, ball center: %d"%(paddle_x,paddle_width//2, self.center))
            print("ball position, frozen: ",self.x)
            self.ball_img.set_x(self.x)
            print("time since creation: ", ticks_diff(ticks_ms(), self.created))
            if ticks_diff(ticks_ms(), self.created) >= 2000:
                # Release frozen ball after 2 seconds
                self.frozen = False
            else:
                return
            
        self.x += int(self.x_speed) + int(self.x_speed2)
        self.x_speed2 -= int(self.x_speed2)
        self.x_speed2 += self.x_speed - int(self.x_speed)

        self.y += int(self.y_speed) + int(self.y_speed2)
        self.y_speed2 -= int(self.y_speed2)
        self.y_speed2 += self.y_speed - int(self.y_speed)
        
        print("x: %d, y: %d"%(self.x,self.y))
        
        # Bounces off walls
        if self.y < 40:               # space for score (30) + width of border image (10)
            self.y = 40
            self.y_speed = -self.y_speed
        if self.x + self.width >= 231:
            self.x = 231 - self.width
            self.x_speed = -self.x_speed
        elif self.x < 9:
            self.x = 9
            self.x_speed = -self.x_speed

        # Check for collision with Paddle
        if (self.y2 >= paddle_y and
           self.x <= paddle_x2 and
           self.x2 >= paddle_x):
            # Ball bounces off paddle
            self.y = paddle_y - (self.height + 1)
            ratio = ((self.x + self.center) -
                     (paddle_x + paddle_center)) / paddle_center
            self.x_speed = ratio * self.max_x_speed
            self.y_speed = -sqrt(max(1, self.max_y_speed ** 2 -
                                     self.x_speed ** 2))

        self.ball_img.set_x(self.x)
        self.ball_img.set_y(self.y)
        self.x2 = self.x + self.width - 1
        self.y2 = self.y + self.height - 1
        
class Brick():
    """Brick."""

    def __init__(self, x, y, color_index, width=26, height=14):
        """Initialize brick.

        Args:
            x, y (int):  X,Y coordinates.
            color (string):  Blue, Green, Pink, Red or Yellow.
            w (Optional int): Block width (default 26).
            h (Optional int): Block height (default 14).
        """
        # print("x: %d, y: %d, color_index: %d"%(x,y,color_index))
        self.x = x
        self.y = y
        self.x2 = x + width - 1
        self.y2 = y + height - 1
        self.center_x = x + (width // 2)
        self.center_y = y + (height // 2)
        self.color_index = color_index
        self.width = width
        self.height = height
        self.img = lv.img(lv.scr_act(),None)
        self.img.set_src(brick_img_dsc[color_index])
        self.img.set_x(self.x)
        self.img.set_y(self.y)

    def bounce(self, ball_x, ball_y, ball_x2, ball_y2,
               x_speed, y_speed,
               ball_center_x, ball_center_y):
        """Determine bounce for ball collision with brick."""
        x = self.x
        y = self.y
        x2 = self.x2
        y2 = self.y2
        center_x = self.center_x
        center_y = self.center_y
        if ((ball_center_x > center_x) and
           (ball_center_y > center_y)):
            if (ball_center_x - x2) < (ball_center_y - y2):
                y_speed = -y_speed
            elif (ball_center_x - x2) > (ball_center_y - y2):
                x_speed = -x_speed
            else:
                x_speed = -x_speed
                y_speed = -y_speed
        elif ((ball_center_x > center_x) and
              (ball_center_y < center_y)):
            if (ball_center_x - x2) < -(ball_center_y - y):
                y_speed = -y_speed
            elif (ball_center_x - x2) > -(ball_center_y - y):
                x_speed = -x_speed
            else:
                x_speed = -x_speed
                y_speed = -y_speed
        elif ((ball_center_x < center_x) and
              (ball_center_y < center_y)):
            if -(ball_center_x - x) < -(ball_center_y - y):
                y_speed = -y_speed
            elif -(ball_center_x - x) > -(ball_center_y - y):
                y_speed = -y_speed
            else:
                x_speed = -x_speed
                y_speed = -y_speed
        elif ((ball_center_x < center_x) and
              (ball_center_y > center_y)):
            if -(ball_center_x - x) < (ball_center_y - y2):
                y_speed = -y_speed
            elif -(ball_center_x - x) > (ball_center_y - y2):
                x_speed = -x_speed
            else:
                x_speed = -x_speed
                y_speed = -y_speed

        return [x_speed, y_speed]

    def clear(self):
        """Clear brick."""
        self.img.delete()

class Life():
    """Life."""

    def __init__(self, index,  w=24, h=8):
        """Initialize life.

        Args:
            index (int): Life number (1-based).
            width (Optional int): Life width (default 24).
            height (Optional int): Life height (default 8).
        """
        margin = 5
        # self.display = display
        self.x = SCREEN_WIDTH - (index * (w + margin))
        self.y = 7
        self.width = w
        self.height = h
        try:
            with open('arkanoid_images/Paddle24x8_argb8888.bin','rb') as f:
                life_data = f.read()
            print('arkanoid_images/Paddle24x8_argb8888.bin successfully read')
            driver=SDL
        except:
            try:
                with open('images/Paddle24x8_rgb565.bin','rb') as f:
                    life_data = f.read()
                print('images/Paddle24x8_rgb565.bin successfully read')
                driver = ILI9341
            except:
                print('Could not open paddle 24x8 image file')
                sys.exit()
        
        if driver == SDL:
            life_dsc = lv.img_dsc_t(
                {
                    "header": {"always_zero": 0, "w": w, "h": h, "cf": lv.img.CF.TRUE_COLOR_ALPHA},
                    "data_size": len(life_data),
                    "data": life_data,
                }
            )
        else:
            life_dsc = lv.img_dsc_t(
                {
                    "header": {"always_zero": 0, "w": w, "h": h, "cf": lv.img.CF.TRUE_COLOR},
                    "data_size": len(life_data),
                    "data": life_data,
                }
            )
            
        self.life_img = lv.img(lv.scr_act())
        self.life_img.set_src(life_dsc)
        self.life_img.set_x(self.x)
        self.life_img.set_y(self.y)

    def clear(self):
        """Clear life."""
        self.life_img.delete()

class Paddle(lv.obj):
    """Paddle."""

    def __init__(self, parent, w=50, h=16):
        """Initialize paddle.

        Args:
            display (SSD1351): OLED display.
            width (Optional int): Paddle width (default 25).
            height (Optional int): Paddle height (default 8).
        """
        super().__init__(parent)
        self.x = 120 -35
        self.y = 300
        self.width = w
        self.height = h
        # Create a parent (gray rectangle)
        rect_style = lv.style_t()
        rect_style.set_bg_color(lv.STATE.DEFAULT,lv_colors.BLACK)
        rect_style.set_radius(lv.STATE.DEFAULT,0)
        rect_style.set_border_width(lv.STATE.DEFAULT,0)
        self.set_size(SCREEN_WIDTH-18, h)
        self.add_style(lv.obj.PART.MAIN,rect_style)
        self.align(None, lv.ALIGN.CENTER, 0, 0)
        self.set_x(10)
        self.set_y(300)
        
        try:
            with open('arkanoid_images/Paddle50x16_released_argb8888.bin','rb') as f:
                paddle_released_data = f.read()
            print('arkanoid_images/Paddle50x16_released_argb8888.bin successfully read')
            driver=SDL
        except:
            try:
                with open('images/Paddle50x16_released_rgb565.bin','rb') as f:
                    paddle_released_data = f.read()
                print('images/Paddle50x16_released_rgb565.bin successfully read')
                driver = ILI9341
            except:
                print('Could not open Paddle_50x16_released image file')
                sys.exit()
        
        if driver == SDL:
            paddle_released_dsc = lv.img_dsc_t(
                {
                    "header": {"always_zero": 0, "w": w, "h": h, "cf": lv.img.CF.TRUE_COLOR_ALPHA},
                    "data_size": len(paddle_released_data),
                    "data": paddle_released_data,
                }
            )
        else:
            paddle_released_dsc = lv.img_dsc_t(
                {
                    "header": {"always_zero": 0, "w": w, "h": h, "cf": lv.img.CF.TRUE_COLOR},
                    "data_size": len(paddle_released_data),
                    "data": paddle_released_data,
                }
            )
        try:
            with open('arkanoid_images/Paddle50x16_pressed_argb8888.bin','rb') as f:
                paddle_pressed_data = f.read()
            print('arkanoid_images/Paddle50x16_pressed_argb8888.bin successfully read')
            driver=SDL
        except:
            try:
                with open('images/Paddle50x16_pressed_rgb565.bin','rb') as f:
                    paddle_pressed_data = f.read()
                print('images/Paddle50x16_pressed_rgb565.bin successfully read')
                driver = ILI9341
            except:
                print('Could not open Paddle_50x16_pressed image file')
                sys.exit()
        
        if driver == SDL:
            paddle_pressed_dsc = lv.img_dsc_t(
                {
                    "header": {"always_zero": 0, "w": w, "h": h, "cf": lv.img.CF.TRUE_COLOR_ALPHA},
                    "data_size": len(paddle_pressed_data),
                    "data": paddle_pressed_data,
                }
            )
        else:
            paddle_pressed_dsc = lv.img_dsc_t(
                {
                    "header": {"always_zero": 0, "w": w, "h": h, "cf": lv.img.CF.TRUE_COLOR},
                    "data_size": len(paddle_pressed_data),
                    "data": paddle_pressed_data,
                }
            )
            
        self.paddle_btn = lv.imgbtn(self,None)
        self.paddle_btn.set_src(lv.btn.STATE.RELEASED,paddle_released_dsc)
        self.paddle_btn.set_src(lv.btn.STATE.PRESSED,paddle_pressed_dsc)        
        self.paddle_btn.set_x(self.x-self.width//2)
        self.paddle_btn.set_y(self.y)

        self.paddle_btn.set_drag(True)                                      # Enable dragging
        self.paddle_btn.set_size(self.width, self.height)                   # Set the size
        self.paddle_btn.align(self, lv.ALIGN.CENTER, 0, 0)                  # Align to the center of the parent
        self.paddle_btn.add_protect(lv.PROTECT.PRESS_LOST)                  # To prevent press lost on fast drags
        self.old_btn_signal_cb = self.paddle_btn.get_signal_cb()            # Save to old signal function
        self.paddle_btn.set_signal_cb(self.new_btn_signal_cb)               # Set a new signal function
        
    def new_btn_signal_cb(self, btn, sign, param):
        # MANDATORY: Include the ancient signal function
        res = self.old_btn_signal_cb(btn, sign, param)
        if res != lv.RES.OK:
            return res

        # Limit the horizontal movement if the coordinates are changed

        if sign == lv.SIGNAL.COORD_CHG:
            # print("coord change")
            x = btn.get_x()
            w = btn.get_width()
            parent = btn.get_parent()
            parent_w = parent.get_width()                
            if x < 0:
                x = 0
            elif x + w > parent_w:
                x = parent_w - w
            self.x = x
            # Align vertically to the middle and use the limited x coordinate
            
            self.paddle_btn.align(self, lv.ALIGN.IN_LEFT_MID, x, 0)
        return lv.RES.OK
    
    def clear(self):
        """Clear paddle."""
        self.paddle_img.delete()

class Powerup(object):
    """Power-up."""

    def __init__(self, x, y, w=32, h=32):
        """Initialize power-up.

        Args:
            x, y (int):  X,Y coordinates.
            display (SSD1351): OLED display.
            width (Optional int): Power-up width (default 32).
            height (Optional int): Power-up height (default 32).
        """
        if x > SCREEN_WIDTH - (9 + w):
            x = SCREEN_WIDTH - (9 + w)
        self.x = x
        self.y = y
        self.x2 = x + w - 1
        self.y2 = y + h - 1
        self.prev_y = y
        self.width = w
        self.height = h
        self.y_speed = 2
        self.collected = False
        try:
            with open('arkanoid_images/Pi32x32_argb8888.bin','rb') as f:
                pi_data = f.read()
            print('arkanoid_images/Pi32x32_argb8888.bin successfully read')
            driver=SDL
        except:
            try:
                with open('images/Pi32x32_rgb565.bin','rb') as f:
                    pi_data = f.read()
                print('images/Pi32x32_rgb565.bin successfully read')
                driver = ILI9341
            except:
                print('Could not open pi image file')
                sys.exit()
        
        if driver == SDL:
            pi_dsc = lv.img_dsc_t(
                {
                    "header": {"always_zero": 0, "w": w, "h": h, "cf": lv.img.CF.TRUE_COLOR_ALPHA},
                    "data_size": len(pi_data),
                    "data": pi_data,
                }
            )
        else:
            pi_dsc = lv.img_dsc_t(
                {
                    "header": {"always_zero": 0, "w": w, "h": h, "cf": lv.img.CF.TRUE_COLOR},
                    "data_size": len(pi_data),
                    "data": pi_data,
                }
            )
        self.pi_img = lv.img(lv.scr_act())
        self.pi_img.set_src(pi_dsc)
        self.pi_img.set_x(self.x)
        self.pi_img.set_y(self.y)
        
    def clear(self):
        """Clear power-up."""
        self.pi_img.delete()

    def set_position(self, paddle_x, paddle_y, paddle_width):
        """Set power-up position."""
        paddle_x2 = paddle_x + paddle_width
        paddle_center = paddle_x + paddle_width // 2
        self.prev_y = self.y
        self.y += self.y_speed

        # Check for collision with Paddle
        if (self.y2 >= paddle_y and
           self.x <= paddle_x2 and
           self.x2 >= paddle_x):
            self.collected = True

        self.y2 = self.y + self.height - 1
        self.pi_img.set_x(self.x)
        self.pi_img.set_y(self.y)

class Score():
    """Initialize score.
    
    Args:
       display (SSD1351): OLED display.
    """
    def __init__(self):

        self.value = 0
        canvas_style = lv.style_t()
        canvas_style.init()       
        canvas_style.set_bg_color(lv.STATE.DEFAULT,lv_colors.WHITE)

        cbuf=bytearray(SCREEN_WIDTH * 30 * 4)
        canvas = lv.canvas(lv.scr_act(),None)
        canvas.set_buffer(cbuf,SCREEN_WIDTH,30,lv.img.CF.TRUE_COLOR)
        # canvas.add_style(lv.canvas.PART.MAIN,canvas_style)
        canvas.align(None,lv.ALIGN.IN_TOP_LEFT,0,0)
        
        p1=lv.point_t()
        p2=lv.point_t()
        point_array=[p1,p2]
        p1.x=0
        p1.y=0
        p2.x=15
        p2.y=p1.y
        
        # style for horizontal lines
        line_dsc = lv.draw_line_dsc_t()
        line_dsc.init()
        line_dsc.color = lv_colors.BLUE
        line_dsc.opa = lv.OPA.COVER
        line_dsc.width = 5

        # draw the horizontal lines
        
        canvas.draw_line(point_array,2,line_dsc)
        p1.x=130
        p2.x=SCREEN_WIDTH
        canvas.draw_line(point_array,2,line_dsc)

        # draw the vertical lines

        p1.x = 0
        p2.x = p1.x
        p2.y = 30
        canvas.draw_line(point_array,2,line_dsc)
        
        p1.x = SCREEN_WIDTH-3
        p2.x = p1.x
        canvas.draw_line(point_array,2,line_dsc)

        text_style = lv.style_t()
        text_style.init()
        text_style.set_text_font(lv.STATE.DEFAULT,lv.font_montserrat_18)
        text_style.set_bg_color(lv.STATE.DEFAULT,lv_colors.BLACK)
        text_style.set_bg_opa(lv.STATE.DEFAULT, lv.OPA.COVER)
            
        self.label = lv.label(canvas,None)
        self.label.add_style(lv.label.PART.MAIN,text_style)
        self.label.set_recolor(True)
        
        self.reset()
        self.label.align(None, lv.ALIGN.OUT_TOP_MID, -60, 25)
        
    def reset(self):
        self.value=0
        self.label.set_text("#ff0000 Score:# #ffffff " + str(self.value) + "#")

    def increment(self,points):
        self.value += points
        self.label.set_text("#ff0000 Score:# #ffffff " + str(self.value) + "#")

    def game_over(self):
        """Display game over."""
        print("game_over")
        label_style = lv.style_t()
        label_style.init()
        label_style.set_text_color(lv.STATE.DEFAULT,lv_colors.RED)
        label_style.set_text_font(lv.STATE.DEFAULT,lv.font_montserrat_24)
        
        game_over_label = lv.label(lv.scr_act())
        game_over_label.add_style(lv.label.PART.MAIN,label_style)
        game_over_label.set_text("Game over!")        
        game_over_label.align(None,lv.ALIGN.CENTER,0,0)
        
class Arkanoid():

    def __init__(self):
        self.game_over=False
        # Draw background image
        draw_background()

        # create the brick images
        create_brick_img_dscs()

        # Generate bricks
        self.MAX_LEVEL = const(9)
        self.level = 1
        self.bricks = load_level(self.level)

        self.paddle = Paddle(lv.scr_act())
        print('paddle x: %d, y: %d'%(self.paddle.x,self.paddle.y))
        self.balls = []

        # Initialze the score
        self.score = Score()

        # Initialize balls
        print("ball position: %d.%d"%(120-9,300-self.paddle.height))
        self.balls.append(Ball(120-9,300-self.paddle.height,-3,-2,frozen=True))

        # Initialize lives
        self.lives = []
        for i in range(1, 3):
            self.lives.append(Life(i))
    
        # Initialize power-ups
        self.powerups = []
        
        anim = lv.anim_t()
        anim.init()
        anim.set_custom_exec_cb(lambda a, obj: self.anim_cb())
        anim.set_repeat_count(LV_ANIM_REPEAT_INFINITE)
        lv.anim_t.start(anim)
        
    def anim_cb(self):
        score_points = 0
        for ball in self.balls:
            print("paddle x: %d, paddle y: %d, paddle width: %d"%(self.paddle.x,self.paddle.y, self.paddle.width))
            ball.set_position(self.paddle.x,self.paddle.y, self.paddle.width)

            if not ball.frozen:
                prior_collision = False
                ball_x = ball.x
                ball_y = ball.y
                ball_x2 = ball.x2
                ball_y2 = ball.y2
                ball_center_x = ball.x + ((ball.x2 + 1 - ball.x) // 2)
                ball_center_y = ball.y + ((ball.y2 + 1 - ball.y) // 2)
                # Check for hits
                for brick in self.bricks:
                    # print(brick)
                    if(ball_x2 >= brick.x and
                       ball_x <= brick.x2 and
                       ball_y2 >= brick.y and
                       ball_y <= brick.y2):
                        # Hit
                        if not prior_collision:
                            ball.x_speed, ball.y_speed = brick.bounce(
                                ball.x,
                                ball.y,
                                ball.x2,
                                ball.y2,
                                ball.x_speed,
                                ball.y_speed,
                                ball_center_x,
                                ball_center_y)
                            prior_collision = True
                            score_points += 1
                            brick.clear()
                            self.bricks.remove(brick)

                        # Generate random power-ups
                        if score_points > 0 and randint(1, 20) == 7:
                            self.powerups.append(Powerup(ball.x, 120))

                    # Check for missed
                    if ball.y2 > SCREEN_HEIGHT - 3:
                        print("y of ball: ", ball.y2)
                        print("clear ball")
                        ball.clear()
                        self.balls.remove(ball)
                        print(self.balls)
                        if not self.balls:
                            # Clear powerups
                            self.powerups.clear()
                            # Lose life if last ball on screen
                            if len(self.lives) == 0:
                                print("lives: ",len(self.lives))
                                self.score.game_over()
                                self.game_over=True
                            else:
                                # Subtract Life
                                self.lives.pop().clear()
                                # Add ball
                                print("Create new ball")
                                self.balls.append(Ball(self.paddle.x+self.paddle.width//2,300-self.paddle.height,-2,-1,frozen=True))
                            # balls.append(Ball(59, 112, 2, -3, frozen=True))
                        return

                # Update score if changed
                if score_points:
                    self.score.increment(score_points)
                # Handle power-ups
                for powerup in self.powerups:
                    powerup.set_position(self.paddle.x, self.paddle.y,
                                         self.paddle.width)
                    if powerup.collected:
                        # Power-up collected
                        powerup.clear()
                        # Add ball
                        self.balls.append(Ball(powerup.x, 112, 2, -1, frozen=False))
                        self.powerups.remove(powerup)
                    elif powerup.y2 > SCREEN_HEIGHT - 3:
                        # Power-up missed
                        powerup.clear()
                        self.powerups.remove(powerup)

                # Check for level completion
                if not self.bricks:
                    for ball in self.balls:
                        ball.clear()
                    self.balls.clear()
                    for powerup in self.powerups:
                        powerup.clear()
                    self.powerups.clear()
                    print("no of balls: ",len(self.balls))
                    self.level += 1
                    if self.level > self.MAX_LEVEL:
                        self.level = 1
                    self.bricks = load_level(self.level)
                    print("New level")
                    print("No of bricks: ",len(bricks))
                    self.balls.append(Ball(self.paddle.x+self.paddle.width//2,300-self.paddle.height,-2,-1,frozen=True))
                    return
                # Attempt to set framerate to 30 FPS
                # timer_dif = 33333 - ticks_diff(ticks_us(), timer)
                # if timer_dif > 0:
                # sleep_us(timer_dif)
    
arkanoid = Arkanoid()
while True:
    if not arkanoid.game_over:
        time-sleep(1)
