#!/opt/bin/lv_micropython -i
import lvgl as lv
from display_driver_utils import driver,ORIENT_LANDSCAPE
from lv_colors import lv_colors
from theme import Theme, LV_DEMO_PRINTER_BLUE,LV_DEMO_PRINTER_TITLE_PAD,LV_DEMO_PRINTER_THEME_TITLE
from theme import LV_DEMO_PRINTER_THEME_ICON,LV_DEMO_PRINTER_THEME_LABEL_WHITE
import ulogging as logging


class DemoPrinter(object):
    
    def __init__(self):
        self.LV_HOR_RES = lv.scr_act().get_disp().driver.hor_res
        self.LV_VER_RES = lv.scr_act().get_disp().driver.ver_res
        
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
 
        bg_top = lv.obj(lv.scr_act(),None)
        bg_top.set_style_local_bg_opa(lv.obj.PART.MAIN, lv.STATE.DEFAULT,lv.OPA.COVER)
        bg_top.set_style_local_bg_color(lv.obj.PART.MAIN, lv.STATE.DEFAULT,LV_DEMO_PRINTER_BLUE)
        bg_top.set_size(self.LV_HOR_RES,self.LV_VER_RES)
        bg_top.set_y(self.LV_DEMO_PRINTER_BG_NORMAL)
        self.theme = Theme()
        self.home_open(0)


    def home_open(self,delay):

        (self.icon_wifi_data,self.icon_wifi_dsc) = self.get_icon("icon_wifi_48x34",48,34)
        (self.icon_tel_data,self.icon_tel_dsc)   = self.get_icon("icon_tel_35x35",35,35)
        (self.icon_eco_data,self.icon_eco_dsc)   = self.get_icon("icon_eco_38x34",38,34)
        (self.icon_pc_data,self.icon_pc_dsc)     = self.get_icon("icon_pc_41x33",41,33)

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
        
        box.align(None, lv.ALIGN.IN_TOP_MID, 0, 100)

        # delay += LV_DEMO_PRINTER_ANIM_DELAY;
        # lv_demo_printer_anim_in(box, delay);

        (self.img_btn_bg_1_data,self.img_btn_bg_1_dsc) = self.get_icon("img_btn_bg_1_174x215",174,215)
        (self.img_btn_bg_2_data,self.img_btn_bg_2_dsc) = self.get_icon("img_btn_bg_2_174x215",174,215)
        (self.img_btn_bg_3_data,self.img_btn_bg_3_dsc) = self.get_icon("img_btn_bg_3_174x215",174,215)
        (self.img_btn_bg_4_data,self.img_btn_bg_4_dsc) = self.get_icon("img_btn_bg_4_174x215",174,215)
        
        (self.img_copy_data,self.img_copy_dsc) = self.get_icon("img_copy_51x60",51,60)
        (self.img_print_data,self.img_print_dsc) = self.get_icon("img_print_65x64",65,64)
        (self.img_scan_data,self.img_scan_dsc) = self.get_icon("img_scan_51x61",51,61)
        (self.img_setup_data,self.img_setup_dsc) = self.get_icon("img_setup_63x64",63,64)
        
        icon = self.add_icon(box, self.img_btn_bg_1_dsc, self.img_copy_dsc, "COPY")
        icon.align(None, lv.ALIGN.IN_LEFT_MID, 1 * (box_w - 20) // 8 - 80, 0)
        icon.set_event_cb(self.copy_open_icon_event_cb)
        icon.fade_in(self.LV_DEMO_PRINTER_ANIM_TIME * 2, delay + self.LV_DEMO_PRINTER_ANIM_TIME + 50)
        
        icon = self.add_icon(box, self.img_btn_bg_2_dsc, self.img_scan_dsc, "SCAN")
        icon.align(None, lv.ALIGN.IN_LEFT_MID, 3 * (box_w - 20) // 8 - 80, 0)
        icon.fade_in(self.LV_DEMO_PRINTER_ANIM_TIME * 2, delay + self.LV_DEMO_PRINTER_ANIM_TIME + 50);
        icon.set_event_cb(self.scan_open_icon_event_cb)
        
        icon = self.add_icon(box, self.img_btn_bg_3_dsc, self.img_print_dsc, "PRINT")
        icon.align(None, lv.ALIGN.IN_LEFT_MID, 5 * (box_w - 20) // 8 - 80, 0)
        icon.fade_in(self.LV_DEMO_PRINTER_ANIM_TIME * 2, delay + self.LV_DEMO_PRINTER_ANIM_TIME + 50);
        # lv_obj_set_event_cb(icon, print_open_event_cb);

        icon = self.add_icon(box, self.img_btn_bg_4_dsc, self.img_setup_dsc, "SETUP");
        icon.align(None, lv.ALIGN.IN_LEFT_MID, 7 * (box_w - 20) // 8 - 80, 0)
        icon.fade_in(self.LV_DEMO_PRINTER_ANIM_TIME * 2, delay + self.LV_DEMO_PRINTER_ANIM_TIME + 50);
        # lv_obj_set_event_cb(icon, setup_icon_event_cb);

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
            # lv_demo_printer_anim_bg(150, LV_DEMO_PRINTER_BLUE, LV_DEMO_PRINTER_BG_FULL);

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
            # self.anim_out_all(lv_scr_act(), 0)
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
                    delay += LV_DEMO_PRINTER_ANIM_DELAY
                a.set_ready_cb(lv.obj.del_anim_ready_cb)
                lv.anim_t.start(a)
                               
        
    def scan_anim_ready(self,a):
        self.log.debug("scan_anim_ready")
        self.anim_out_all(lv_scr_act(), None)
        self.scan1_open(self.scan_btn_txt)
        
    def scan1_open(btn_txt):
        self.log.debug("scan1_open %d"%txt)
        anim_out_all(lv.scr_act(), None)
        

    def anim_bg(self,delay,color,y_new):
        self.log.debug("anim_bg: new y: %d"&y_new)
        y_act = self.bg_top.get_y()
        self.log.debug("current y: %d"&y_act)
        
        
drv = driver(width=800,height=480,orientation=ORIENT_LANDSCAPE)
printer = DemoPrinter()
