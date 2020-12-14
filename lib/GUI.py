import lvgl as lv
lv.init()

class driver:
    
    def __init__(self):
        self.orientation = "LANDSCAPE"
        self.disp = None
        self.touch = None
        self.type = None
        self.width = 240
        self.height = 240
        
    def set_orientation(self,orientation):
        if self.type:
            print("set_orientation must be called before init_gui")
        if orientation != "LANDSCAPE" and orientation != "PORTRAIT":
            return
        else:
            self.orientation = orientation
        print("orientation: ",orientation)
        
    # Setting width and height only works on the SDL driver
    
    def set_width(self,width):
        if self.type:
            print("set_width must be called before init_gui")
        self.width = width

    def set_height(self,height):
        if self.type:
            print("set_height must be called before init_gui")
        self.height = height
        
    def init_gui_SDL(self):

        import SDL
        SDL.init(w=self.width,h=self.height)
        print("SDL version")
        # Register SDL display driver.

        disp_buf1 = lv.disp_buf_t()
        buf1_1 = bytearray(self.width*10)
        disp_buf1.init(buf1_1, None, len(buf1_1)//4)
        disp_drv = lv.disp_drv_t()
        disp_drv.init()
        disp_drv.buffer = disp_buf1
        disp_drv.flush_cb = SDL.monitor_flush
        disp_drv.hor_res = self.width
        disp_drv.ver_res = self.height
        disp_drv.register()

        # Register SDL mouse driver

        indev_drv = lv.indev_drv_t()
        indev_drv.init() 
        indev_drv.type = lv.INDEV_TYPE.POINTER;
        indev_drv.read_cb = SDL.mouse_read;
        indev_drv.register();
        self.type = "SDL"
        print("Running the Unix version")
        
    def init_gui_esp32(self):

        import lvesp32

        # Initialize ILI9341 display

        from ili9XXX import ili9341,COLOR_MODE_BGR,LANDSCAPE,PORTRAIT
        from xpt2046 import xpt2046
        import espidf as esp
        if self.orientation == "PORTRAIT":
            print ("ili9341 initialized in portait mode")
            # Initialize ILI9341 display in prtrait mode
            self.disp = ili9341(miso=19,mosi=23,clk=18, cs=26, dc=5, rst=-1, power=-1, backlight=-1, backlight_on=0, power_on=0,
                                spihost=esp.VSPI_HOST, mhz=40, factor=4, hybrid=True, width=240, height=320,
                                colormode=COLOR_MODE_BGR, rot=PORTRAIT, invert=False, double_buffer=True, half_duplex=True)
            self.touch = xpt2046(spihost=esp.VSPI_HOST,cal_x0=3751, cal_x1 = 210, cal_y0=3906, cal_y1 = 283, transpose=True)
            # self.touch = xpt2046()
        else:
            print ("ili9341 initialized in landscape mode")
            # Initialize ILI9341 display
            self.disp = ili9341(miso=19,mosi=23,clk=18, cs=26, dc=5, rst=-1, power=-1, backlight=-1, backlight_on=0, power_on=0,
                                spihost=esp.VSPI_HOST, mhz=40, factor=4, hybrid=True, width=320, height=240,
                                colormode=COLOR_MODE_BGR, rot=LANDSCAPE, invert=False, double_buffer=True, half_duplex=True)
            
            # Register xpt2046 touch driver
            self.touch = xpt2046(spihost=esp.VSPI_HOST,cal_x0=3799, cal_x1 = 353, cal_y0=220, cal_y1 = 3719, transpose=False)
            # self.touch = xpt2046(transpose = False)
            print("Running on the ili9341 module")
            self.type="ili9341"
        # self.disp = ili9341()
        
        # Register raw resistive touch driver
        '''
        import rtch
        touch = rtch.touch(xp = 32, yp = 33, xm = 25, ym = 26, touch_rail = 27, touch_sense = 33)
        touch.init()
        indev_drv = lv.indev_drv_t()
        lv.indev_drv_init(indev_drv) 
        indev_drv.type = lv.INDEV_TYPE.POINTER;
        indev_drv.read_cb = touch.read;
        lv.indev_drv_register(indev_drv);
        '''

        # from xpt2046 import xpt2046
        # self.touch = xpt2046()
    
    def init_gui(self):
        
        # Identify platform and initialize it

        try:
            self.init_gui_esp32()
        except ImportError:
            pass
    
        try:
            self.init_gui_SDL()
        except ImportError:
            pass

        try:
            # check if we are running on a t-watch
            import ttgo
            from axp_constants import AXP202_VBUS_VOL_ADC1,AXP202_VBUS_CUR_ADC1,AXP202_BATT_CUR_ADC1,AXP202_BATT_VOL_ADC1
                
            watch = ttgo.Watch()
            tft = watch.tft
            power = watch.pmu
            power.adc1Enable(AXP202_VBUS_VOL_ADC1
                             | AXP202_VBUS_CUR_ADC1 
                             | AXP202_BATT_CUR_ADC1
                             | AXP202_BATT_VOL_ADC1, True)
            watch.lvgl_begin()
            watch.tft.backlight_fade(100)
            self.type="t-watch"            
            print("Running on the LilyGo t-watch 2020")
        except:
            pass

