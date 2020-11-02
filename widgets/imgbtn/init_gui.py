import lvgl as lv
import sys
import os
lv.init()

try:    
    osVersion=os.uname()
    print("Running: ",osVersion)
    try:
        # check if we are running on a t-watch
        import ttgo
        from axp_constants import *
        
        watch = ttgo.Watch()
        tft = watch.tft
        power = watch.pmu
        power.adc1Enable(AXP202_VBUS_VOL_ADC1
                         | AXP202_VBUS_CUR_ADC1 
                         | AXP202_BATT_CUR_ADC1
                         | AXP202_BATT_VOL_ADC1, True)
        watch.lvgl_begin()
        watch.tft.backlight_fade(100)
    except:    
        try:
            # check if we are running onf an ili9431
            import lvesp32
            from ili9XXX import ili9431
            from xpt2046 import xpt2046
            
            # Initialize ILI9341 display
            disp = ili9431()
            
            # Register xpt2046 touch driver
            touch = xpt2046()
        except:
            print("Not running a supported lvgl enabled version of Micropython. Giving up...")
            sys.exit()

except:        
    try:
        import SDL
        SDL.init(w=240,h=240)

        # Register SDL display driver.
        
        disp_buf1 = lv.disp_buf_t()
        buf1_1 = bytes(240 * 10)
        disp_buf1.init(buf1_1, None, len(buf1_1)//4)
        disp_drv = lv.disp_drv_t()
        disp_drv.init()
        disp_drv.buffer = disp_buf1
        disp_drv.flush_cb = SDL.monitor_flush
        disp_drv.hor_res = 240
        disp_drv.ver_res = 240
        disp_drv.register()
        
        # Register SDL mouse driver
        
        indev_drv = lv.indev_drv_t()
        indev_drv.init() 
        indev_drv.type = lv.INDEV_TYPE.POINTER
        indev_drv.read_cb = SDL.mouse_read
        indev_drv.register()
        print("Running the Unix version")
    except:
        print("Not running a supported lvgl enabled version of Micropython. Giving up...")
        sys.exit()
        
# Create a screen and load it
scr = lv.obj()
lv.scr_load(scr)
