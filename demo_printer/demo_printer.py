#!/opt/bin/lv_micropython -i
import lvgl as lv
from display_driver_utils import driver,ORIENT_LANDSCAPE
from lv_colors import lv_colors
from theme import Theme, LV_DEMO_PRINTER_BLUE,LV_DEMO_PRINTER_TITLE_PAD,LV_DEMO_PRINTER_THEME_TITLE
from theme import LV_DEMO_PRINTER_THEME_ICON,LV_DEMO_PRINTER_THEME_LABEL_WHITE,LV_DEMO_PRINTER_RED
from theme import LV_DEMO_PRINTER_THEME_BTN_BORDER
import utime as time

import ulogging as logging


class DemoPrinter(object):
    
    def __init__(self):
        self.LV_HOR_RES = lv.scr_act().get_disp().driver.hor_res
        self.LV_VER_RES = lv.scr_act().get_disp().driver.ver_res
        # Bg positions
        self.LV_DEMO_PRINTER_BG_NONE   = -self.LV_VER_RES
        self.LV_DEMO_PRINTER_BG_FULL   =  0
        self.LV_DEMO_PRINTER_BG_NORMAL = -2 * (self.LV_VER_RES // 3)
        self.LV_DEMO_PRINTER_BG_SMALL  = -5 * (self.LV_VER_RES // 6)
        
        # Animations
        self.LV_DEMO_PRINTER_ANIM_Y       = self.LV_VER_RES // 20
        self.LV_DEMO_PRINTER_ANIM_DELAY   = 40
        self.LV_DEMO_PRINTER_ANIM_TIME    = 150
        self.LV_DEMO_PRINTER_ANIM_TIME_BG = 300
        
        self.LV_DEMO_PRINTER_BG_NORMAL = (-2 * (self.LV_VER_RES // 3))

        self.log = logging.getLogger("DemoPrinter")
        self.log.setLevel(logging.DEBUG)
        
        self.icon_wifi_data = None
        self.icon_wifi_dsc = None
        self.icon_tel_data = None
        self.icon_tel_dsc = None
        self.icon_eco_data = None
        self.icon_eco_dsc = None
        self.icon_pc_data = None
        self.icon_pc_dsc = None
        
        self.img_btn_bg_1_data = None
        self.img_btn_bg_1_dsc = None
        self.img_btn_bg_2_data = None
        self.img_btn_bg_2_dsc = None
        self.img_btn_bg_3_data = None
        self.img_btn_bg_3_dsc = None
        self.img_btn_bg_4_data = None
        self.img_btn_bg_4_dsc = None

        self.img_copy_data = None
        self.img_copy_dsc = None
        self.img_print_data = None
        self.img_print_dsc = None
        self.img_scan_data = None
        self.img_scan_dsc = None
        self.img_setup_data = None
        self.img_setup_dsc = None

        self.scan_img = None
        self.bg_top = None
        self.bg_bottom = None

        self.bg_color_prev = LV_DEMO_PRINTER_BLUE
        self.bg_color_act = LV_DEMO_PRINTER_BLUE
        self.bg_top = lv.obj(lv.scr_act(),None)
        self.bg_top.set_size(self.LV_HOR_RES,self.LV_VER_RES)
        self.theme = Theme()
        self.image_files_read = False
        self.home_open(0)

    def home_open(self,delay):
        
        self.bg_top.set_style_local_bg_opa(lv.obj.PART.MAIN, lv.STATE.DEFAULT,lv.OPA.COVER)
        self.bg_top.set_style_local_bg_color(lv.obj.PART.MAIN, lv.STATE.DEFAULT,LV_DEMO_PRINTER_BLUE)
        self.bg_top.set_y(self.LV_DEMO_PRINTER_BG_NORMAL)

        if not self.image_files_read:
        # read all the images fromm the raw image files
        
            (self.icon_wifi_data,self.icon_wifi_dsc) = self.get_icon("icon_wifi_48x34",48,34)
            (self.icon_tel_data,self.icon_tel_dsc)   = self.get_icon("icon_tel_35x35",35,35)
            (self.icon_eco_data,self.icon_eco_dsc)   = self.get_icon("icon_eco_38x34",38,34)
            (self.icon_pc_data,self.icon_pc_dsc)     = self.get_icon("icon_pc_41x33",41,33)

            (self.img_btn_bg_1_data,self.img_btn_bg_1_dsc) = self.get_icon("img_btn_bg_1_174x215",174,215)
            (self.img_btn_bg_2_data,self.img_btn_bg_2_dsc) = self.get_icon("img_btn_bg_2_174x215",174,215)
            (self.img_btn_bg_3_data,self.img_btn_bg_3_dsc) = self.get_icon("img_btn_bg_3_174x215",174,215)
            (self.img_btn_bg_4_data,self.img_btn_bg_4_dsc) = self.get_icon("img_btn_bg_4_174x215",174,215)
            
            (self.img_copy_data,self.img_copy_dsc) = self.get_icon("img_copy_51x60",51,60)
            (self.img_print_data,self.img_print_dsc) = self.get_icon("img_print_65x64",65,64)
            (self.img_scan_data,self.img_scan_dsc) = self.get_icon("img_scan_51x61",51,61)
            (self.img_setup_data,self.img_setup_dsc) = self.get_icon("img_setup_63x64",63,64)
            
            (self.img_printer2_data,self.img_printer2_dsc)       = self.get_icon("img_printer2_107x104",107,104)
            (self.img_no_internet_data,self.img_no_internet_dsc) = self.get_icon("img_no_internet_42x42",42,42)
            (self.img_cloud_data,self.img_cloud_dsc)             = self.get_icon("img_cloud_93x59",93,59)
            
        self.image_files_read = True
        
        self.cont = lv.cont(lv.scr_act(),None)
        self.cont.set_size(350,80)
        self.cont.clean_style_list(lv.cont.PART.MAIN)
        self.cont.align(None, lv.ALIGN.IN_TOP_LEFT, 60, 0)
        
        icon = lv.img(self.cont, None)
        icon.set_src(self.icon_wifi_dsc)
        icon.align(None, lv.ALIGN.IN_TOP_LEFT, 20, 45)
        self.anim_in(icon, delay);

        icon = lv.img(self.cont, None)
        icon.set_src(self.icon_tel_dsc)
        icon.align(None, lv.ALIGN.IN_TOP_LEFT, 110, 45)
        self.anim_in(icon, delay);

        icon = lv.img(self.cont, None)
        icon.set_src(self.icon_eco_dsc)
        icon.align(None, lv.ALIGN.IN_TOP_LEFT, 200, 45)
        self.anim_in(icon, delay);

        icon = lv.img(self.cont, None)
        icon.set_src(self.icon_pc_dsc)
        icon.align(None, lv.ALIGN.IN_TOP_LEFT, 290, 45)
        self.anim_in(icon, delay);

        title = self.add_title("22 April 2020 15:36");
        title.align(None, lv.ALIGN.IN_TOP_RIGHT, -60, LV_DEMO_PRINTER_TITLE_PAD)
        
        delay += self.LV_DEMO_PRINTER_ANIM_DELAY
        self.anim_in(title, delay)
        
        box_w = 720;
        box = lv.obj(lv.scr_act(), None)
        box.set_size(box_w, 260)
        self.theme.apply(box,lv.THEME.CONT)
        
        box.align(None, lv.ALIGN.IN_TOP_MID, 0, 100)

        # delay += LV_DEMO_PRINTER_ANIM_DELAY;
        # lv_demo_printer_anim_in(box, delay);
        
        icon = self.add_icon(box, self.img_btn_bg_1_dsc, self.img_copy_dsc, "COPY")
        icon.align(None, lv.ALIGN.IN_LEFT_MID, 1 * (box_w - 20) // 8 - 80, 0)
        icon.set_event_cb(self.copy_open_icon_event_cb)
        icon.fade_in(self.LV_DEMO_PRINTER_ANIM_TIME * 2, delay + self.LV_DEMO_PRINTER_ANIM_TIME + 50)
        
        icon = self.add_icon(box, self.img_btn_bg_2_dsc, self.img_scan_dsc, "SCAN")
        icon.align(None, lv.ALIGN.IN_LEFT_MID, 3 * (box_w - 20) // 8 - 80, 0)
        icon.fade_in(self.LV_DEMO_PRINTER_ANIM_TIME * 2, delay + self.LV_DEMO_PRINTER_ANIM_TIME + 50)
        icon.set_event_cb(self.scan_open_icon_event_cb)
        
        icon = self.add_icon(box, self.img_btn_bg_3_dsc, self.img_print_dsc, "PRINT")
        icon.align(None, lv.ALIGN.IN_LEFT_MID, 5 * (box_w - 20) // 8 - 80, 0)
        icon.fade_in(self.LV_DEMO_PRINTER_ANIM_TIME * 2, delay + self.LV_DEMO_PRINTER_ANIM_TIME + 50)
        # lv_obj_set_event_cb(icon, print_open_event_cb);

        icon = self.add_icon(box, self.img_btn_bg_4_dsc, self.img_setup_dsc, "SETUP");
        icon.align(None, lv.ALIGN.IN_LEFT_MID, 7 * (box_w - 20) // 8 - 80, 0)
        icon.fade_in(self.LV_DEMO_PRINTER_ANIM_TIME * 2, delay + self.LV_DEMO_PRINTER_ANIM_TIME + 50)
        icon.set_event_cb(self.setup_icon_event_cb)

        box = lv.obj(lv.scr_act(), None)
        box.set_size(500, 80)
        box.align(None, lv.ALIGN.IN_BOTTOM_LEFT, self.LV_HOR_RES // 20,
                     - self.LV_HOR_RES // 40)
        label = lv.label(box,None)
        label.set_text("What do you want to do today?")
        self.theme.apply(label,lv.THEME.LABEL)
        label.align(box,lv.ALIGN.CENTER,0,0)
    
        delay += self.LV_DEMO_PRINTER_ANIM_DELAY;
        self.anim_in(box,delay)
        
        box = lv.obj(lv.scr_act(), None)
        box_w = 200;
        box.set_size(box_w, 80)
        box.align(None, lv.ALIGN.IN_BOTTOM_RIGHT, - self.LV_HOR_RES // 20,
                     - self.LV_HOR_RES // 40)
        
        bar = lv.bar(box, None)
        bar.set_style_local_bg_color(lv.bar.PART.INDIC, lv.STATE.DEFAULT,
                                        lv.color_hex(0x01d3d4))
        bar.set_size(25, 50)
        bar.align(None, lv.ALIGN.IN_LEFT_MID, 1 * (box_w - 20) // 8 + 10, 0)
        bar.set_value(60, lv.ANIM.ON)

        bar = lv.bar(box, None)
        bar.set_style_local_bg_color(lv.bar.PART.INDIC, lv.STATE.DEFAULT,
                                        lv.color_hex(0xe600e6))
        bar.set_size(25, 50)
        bar.align(None, lv.ALIGN.IN_LEFT_MID, 3 * (box_w - 20) // 8 + 10, 0)
        bar.set_value(30, lv.ANIM.ON)
        
        bar = lv.bar(box, None)
        bar.set_style_local_bg_color(lv.bar.PART.INDIC, lv.STATE.DEFAULT,
                                     lv.color_hex(0xefef01))
        bar.set_size(25, 50)
        bar.align(None, lv.ALIGN.IN_LEFT_MID, 5 * (box_w - 20) // 8 + 10, 0)
        bar.set_value(80, lv.ANIM.ON)
        
        bar = lv.bar(box, None)
        bar.set_style_local_bg_color(lv.bar.PART.INDIC, lv.STATE.DEFAULT,
                                        lv.color_hex(0x1d1d25))
        bar.set_size(25, 50)
        bar.align(None, lv.ALIGN.IN_LEFT_MID, 7 * (box_w - 20) // 8 + 10, 0)
        bar.set_value(20, lv.ANIM.ON)
    #
    # get an icon
    #
    def get_icon(self,filename,xres,yres):

        try:
            sdl_filename = 'images/' + filename + "_argb8888.bin"
            self.log.debug('sdl filename: ' + sdl_filename)
            with open(sdl_filename,'rb') as f:
                icon_data = f.read()
                self.log.debug(sdl_filename + " successfully read")
        except:
            self.log.error("Could not find image file: " + filename) 
            return None
        
        icon_dsc = lv.img_dsc_t(
            {
                "header": {"always_zero": 0, "w": xres, "h": yres, "cf": lv.img.CF.TRUE_COLOR_ALPHA},
                "data": icon_data,
                "data_size": len(icon_data),
            }
        )
        return (icon_data,icon_dsc) 

    def add_title(self,txt):
        title = lv.label(lv.scr_act(), None)
        self.theme.apply(title,LV_DEMO_PRINTER_THEME_TITLE)
        title.set_text(txt)
        title.align(None, lv.ALIGN.IN_TOP_MID, 0, LV_DEMO_PRINTER_TITLE_PAD)
        return title

    def add_icon(self,parent,src_bg_dsc,src_icon_dsc,txt):
        bg = lv.img(parent,None)
        bg.set_click(True)
        bg.set_src(src_bg_dsc)
        self.theme.apply(bg,LV_DEMO_PRINTER_THEME_ICON)
        bg.set_antialias(False)

        icon = lv.img(bg,None)
        icon.set_src(src_icon_dsc)
        icon.set_style_local_image_recolor_opa(lv.img.PART.MAIN, lv.STATE.DEFAULT, lv.OPA.TRANSP)
        icon.align(None, lv.ALIGN.IN_TOP_RIGHT, -30, 30)

        label = lv.label(bg,None)
        label.set_text(txt)
        label.align(None, lv.ALIGN.IN_BOTTOM_LEFT, 30, -30)
        self.theme.apply(label,lv.THEME.LABEL)
        return bg
                
    def copy_open_icon_event_cb(self,obj,evt):
        if evt == lv.EVENT.CLICKED:
            self.anim_out_all(lv.scr_act(), 0)
            self.log.debug("copy_open_icon_event_cb")
            scan_btn_txt = "NEXT"
            delay = 200
            self.anim_bg(150, LV_DEMO_PRINTER_BLUE, LV_DEMO_PRINTER_BG_FULL)

            arc = self.add_loader(self.scan_anim_ready)
            arc.align(None, lv.ALIGN.CENTER, 0, -40)

            txt = lv.label(lv.scr_act(), None)
            txt.set_text("Scanning, please wait...")
            self.theme.apply(txt, LV_DEMO_PRINTER_THEME_LABEL_WHITE)
            txt.align(arc, lv.ALIGN.OUT_BOTTOM_MID, 0, 60)

            #lv_demo_printer_anim_in(arc, delay);
            delay += self.LV_DEMO_PRINTER_ANIM_DELAY
            #lv_demo_printer_anim_in(txt, delay);
    
            # icon_generic_event_cb(obj, e);
            
    def scan_open_icon_event_cb(self,obj,evt):
        if evt == lv.EVENT.CLICKED:
            self.log.debug("scan_open_icon_event_cb")
            self.scan_btn_txt = "SAVE"
            self.anim_out_all(lv.scr_act(), 0)
            delay = 200
            # lv_demo_printer_anim_bg(150, LV_DEMO_PRINTER_BLUE, LV_DEMO_PRINTER_BG_FULL);
            arc = self.add_loader(self.scan_anim_ready)
            arc.align(None, lv.ALIGN.CENTER, 0, -40)

            txt = lv.label(lv.scr_act(), None)
            txt.set_text("Scanning, please wait...");
            self.theme.apply(txt, LV_DEMO_PRINTER_THEME_LABEL_WHITE)
            txt.align(arc, lv.ALIGN.OUT_BOTTOM_MID, 0, 60)

            # lv_demo_printer_anim_in(arc, delay);
            delay += self.LV_DEMO_PRINTER_ANIM_DELAY
            # lv_demo_printer_anim_in(txt, delay);
            
    def setup_icon_event_cb(self,obj,evt):
        if evt == lv.EVENT.CLICKED:
            self.log.debug("setup_icon_event_cb")
            self.anim_out_all(lv.scr_act(), 0)
            
            self.anim_bg(0, LV_DEMO_PRINTER_RED, self.LV_DEMO_PRINTER_BG_FULL)
            delay = 200
            
            img = lv.img(lv.scr_act(), None)
            img.set_src(self.img_printer2_dsc);
            img.align(None, lv.ALIGN.CENTER, -90, 0)

            self.anim_in(img, delay)
            delay += self.LV_DEMO_PRINTER_ANIM_DELAY        
            
            img = lv.img(lv.scr_act(), None)
            img.set_src(self.img_no_internet_dsc)
            img.align(None, lv.ALIGN.CENTER, 0, -40)
            
            self.anim_in(img, delay)
            delay += self.LV_DEMO_PRINTER_ANIM_DELAY   
            
            img = lv.img(lv.scr_act(), None)
            img.set_src(self.img_cloud_dsc)
            img.align(None, lv.ALIGN.CENTER, 80, -80)
            
            self.anim_in(img, delay)
            delay += self.LV_DEMO_PRINTER_ANIM_DELAY

            self.info_bottom_create("You have no permission to change the settings.", "BACK", self.back_to_home_event_cb, delay)
                        
    def add_loader(self, a):
        arc = lv.arc(lv.scr_act(),None)
        arc.set_bg_angles(0, 0)
        arc.set_start_angle(270)
        arc.set_size(180, 180)
        
        self.log.debug("Starting loader anim")
        a = lv.anim_t()
        a.init()
        a.set_custom_exec_cb(lambda a, val: self.loader_anim_cb(a,arc,val))
        a.set_values(0, 110)
        a.set_time(2000)
        a.set_ready_cb(lambda a:  self.end_cb(a,arc))
        lv.anim_t.start(a)                

        return arc

    def end_cb(self,a,arc):
        self.log.debug("in anim ended")
        
    def loader_anim_cb(self,a,arc,v):
        # self.log.debug("loader_anim_cb called with value: %d"%v)
        if v > 100:
            v = 100
        arc.set_end_angle(v * 360 // 100 + 270)
        percent_txt = "%d %%"%v
        arc.set_style_local_value_str(lv.arc.PART.BG, lv.STATE.DEFAULT, percent_txt)

                                     
    def anim_in(self,obj,delay):
        a = lv.anim_t()
        a.init()
        a.set_var(obj)
        a.set_time(self.LV_DEMO_PRINTER_ANIM_TIME)
        a.set_delay(delay)
        # a.set_exec_cb(obj.set_y)
        # a.set_values(obj.get_y() -  self.LV_DEMO_PRINTER_ANIM_Y, obj.get_y())
        # a.start()
        obj.fade_in(self.LV_DEMO_PRINTER_ANIM_TIME - 50, delay)

    def anim_out_all(self,obj,delay):
        self.log.debug("anim_out_all")
        child = obj.get_child_back(None)
        while child:
            if child != self.scan_img and child != self.bg_top and child != self.bg_bottom and child != lv.scr_act():
                a = lv.anim_t()
                a.init()
                a.set_var(child)
                a.set_time(self.LV_DEMO_PRINTER_ANIM_TIME)
                # a.set_exec_cb(lambda y: lv.obj.set_y(y))
                if child.get_y() < 80:
                    a.set_values(child.get_y(),child.get_y() - self.LV_DEMO_PRINTER_ANIM_Y)
                else:
                    a.set_values(child.get_y(),child.get_y() + self.LV_DEMO_PRINTER_ANIM_Y)
                    delay += self.LV_DEMO_PRINTER_ANIM_DELAY
                a.set_ready_cb(lv.obj.del_anim_ready_cb)
                lv.anim_t.start(a)
            child = obj.get_child_back(child)                   
        
    def scan_anim_ready(self,a):
        self.log.debug("scan_anim_ready")
        self.anim_out_all(lv_scr_act(), None)
        self.scan1_open(self.scan_btn_txt)
        
    def scan1_open(btn_txt):
        self.log.debug("scan1_open %d"%txt)
        anim_out_all(lv.scr_act(), None)
        

    def anim_bg(self,delay,color,y_new):
        self.log.debug("anim_bg: new y: %d"%y_new)
        y_act = self.bg_top.get_y()
        self.log.debug("current y: %d"%y_act)
        if y_new != self.LV_DEMO_PRINTER_BG_NORMAL and y_new == y_act and  act_color.full == color.full:
            return
        
        if (y_new == self.LV_DEMO_PRINTER_BG_NORMAL and y_new == y_act) or \
           (y_new == self.LV_DEMO_PRINTER_BG_NORMAL and y_act == self.LV_DEMO_PRINTER_BG_FULL):            
            path = lv.anim_path_t()
            path.init()
            path.set_cb(anim_path.triangle)
            
            a = lv.anim_t()
            a.set_var(self.bg_top)
            a.set_time(self.LV_DEMO_PRINTER_ANIM_TIME_BG + 200)
            a.set_delay(delay)
            a.set_custom_exec_cb(lambda a, val: self.set_y(self.bg_top,val))
            #a.set_exec_cb(lv.obj.set_y)
            a.set_values(y_act, y_new)
            a.set_path(path)
            lv.anim_t.start(a)
        else:
            a = lv.anim_t()
            a.set_var(self.bg_top)
            a.set_time(self.LV_DEMO_PRINTER_ANIM_TIME_BG)
            a.set_delay(delay)
            a.set_custom_exec_cb(lambda a, val: self.set_y(self.bg_top,val))
            # a.set_exec_cb(lv.obj.set_y)
            a.set_values(self.bg_top.get_y(), y_new)
            lv.anim_t.start(a)

        color_anim = lv.anim_t()
        self.bg_color_prev = self.bg_color_act
        self.bg_color_act = color
        color_anim.set_custom_exec_cb(lambda color_anim, val: self.anim_bg_color_cb(val))
        color_anim.set_values(0, 255)
        color_anim.set_time(self.LV_DEMO_PRINTER_ANIM_TIME_BG)
        path = lv.anim_path_t()
        path.init()
        path.set_cb(lv.anim_path_t.linear)
        # a.set_path(lv.anim_t.path_def)
        lv.anim_t.start(color_anim)

    def set_y(self,obj,new_y):
        self.log.debug("Setting y to %d"%new_y)
        obj.set_y(new_y)
 
    def anim_bg_color_cb(self,v):
        self.log.debug("anim_bg_color_cb: Mixing colors with value: %d"%v)
        c = self.bg_color_act.color_mix(self.bg_color_prev,v)
        self.bg_top.set_style_local_bg_color(lv.obj.PART.MAIN, lv.STATE.DEFAULT, c)
        
    def info_bottom_create(self, label_txt, btn_txt, btn_event_cb, delay):
        LV_DEMO_PRINTER_BTN_W = 200
        LV_DEMO_PRINTER_BTN_H =  50
        
        txt = lv.label(lv.scr_act(), None)
        txt.set_text(label_txt)
        self.theme.apply(txt,LV_DEMO_PRINTER_THEME_LABEL_WHITE)
        txt.align(None,lv.ALIGN.CENTER, 0, 100)

        btn = lv.btn(lv.scr_act(), None)
        self.theme.apply(btn,LV_DEMO_PRINTER_THEME_BTN_BORDER)
        btn.set_size(LV_DEMO_PRINTER_BTN_W,LV_DEMO_PRINTER_BTN_H)
        btn.align(txt, lv.ALIGN.OUT_BOTTOM_MID, 0, 60)
        
        btn.set_style_local_value_str(lv.btn.PART.MAIN, lv.STATE.DEFAULT, btn_txt)
        btn.set_event_cb(btn_event_cb)
        
        self.anim_in(txt, delay)
        delay += self.LV_DEMO_PRINTER_ANIM_DELAY;
        
        self.anim_in(btn, delay);
        delay += self.LV_DEMO_PRINTER_ANIM_DELAY;
        
        self.anim_in(btn, delay);        

    def back_to_home_event_cb(self,obj,evt):
        if evt == lv.EVENT.CLICKED:
            self.anim_out_all(lv.scr_act(), 0)
            self.home_open(200)
        pass
    
drv = driver(width=800,height=480,orientation=ORIENT_LANDSCAPE)
printer = DemoPrinter()
