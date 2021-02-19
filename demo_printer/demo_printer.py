#!/opt/bin/lv_micropython -i
import lvgl as lv
from display_driver_utils import driver,ORIENT_LANDSCAPE
from lv_colors import lv_colors
from theme import Theme, LV_DEMO_PRINTER_BLUE,LV_DEMO_PRINTER_TITLE_PAD,LV_DEMO_PRINTER_THEME_TITLE
from theme import LV_DEMO_PRINTER_THEME_ICON
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

        self.delay = 200
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
        
        '''
        flag = lv.THEME_MATERIAL_FLAG.LIGHT
        demo_printer_theme = lv.theme_material_init(LV_THEME_DEFAULT_COLOR_PRIMARY,LV_THEME_DEFAULT_COLOR_SECONDARY,flag,
                                       lv.theme_get_font_small(), lv.theme_get_font_normal(), lv.theme_get_font_subtitle(),
                                       lv.theme_get_font_title())   
        '''
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
        self.anim_in(icon, self.delay);

        icon = lv.img(self.cont, None)
        icon.set_src(self.icon_tel_dsc)
        icon.align(None, lv.ALIGN.IN_TOP_LEFT, 110, 45)
        # lv_demo_printer_anim_in(icon, delay);

        icon = lv.img(self.cont, None)
        icon.set_src(self.icon_eco_dsc)
        icon.align(None, lv.ALIGN.IN_TOP_LEFT, 200, 45)
        # lv_demo_printer_anim_in(icon, delay);

        icon = lv.img(self.cont, None)
        icon.set_src(self.icon_pc_dsc)
        icon.align(None, lv.ALIGN.IN_TOP_LEFT, 290, 45)
        # lv_demo_printer_anim_in(icon, delay);

        title = self.add_title("22 April 2020 15:36");
        title.align(None, lv.ALIGN.IN_TOP_RIGHT, -60, LV_DEMO_PRINTER_TITLE_PAD)
        
        # delay += LV_DEMO_PRINTER_ANIM_DELAY
        # lv_demo_printer_anim_in(title, delay)
        
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
        # lv_obj_set_event_cb(icon, copy_open_icon_event_cb);
        # lv_obj_fade_in(icon, LV_DEMO_PRINTER_ANIM_TIME * 2, delay + LV_DEMO_PRINTER_ANIM_TIME + 50);
        
        icon = self.add_icon(box, self.img_btn_bg_2_dsc, self.img_scan_dsc, "SCAN")
        icon.align(None, lv.ALIGN.IN_LEFT_MID, 3 * (box_w - 20) // 8 - 80, 0)
        # lv_obj_fade_in(icon, LV_DEMO_PRINTER_ANIM_TIME * 2, delay + LV_DEMO_PRINTER_ANIM_TIME + 50);
        # lv_obj_set_event_cb(icon, scan_open_icon_event_cb);
        
        icon = self.add_icon(box, self.img_btn_bg_3_dsc, self.img_print_dsc, "PRINT")
        icon.align(None, lv.ALIGN.IN_LEFT_MID, 5 * (box_w - 20) // 8 - 80, 0)
        # icon.fade_in(LV_DEMO_PRINTER_ANIM_TIME * 2, delay + LV_DEMO_PRINTER_ANIM_TIME + 50);
        # lv_obj_set_event_cb(icon, print_open_event_cb);

        icon = self.add_icon(box, self.img_btn_bg_4_dsc, self.img_setup_dsc, "SETUP");
        icon.align(None, lv.ALIGN.IN_LEFT_MID, 7 * (box_w - 20) // 8 - 80, 0)
        # lv_obj_fade_in(icon, LV_DEMO_PRINTER_ANIM_TIME * 2, delay + LV_DEMO_PRINTER_ANIM_TIME + 50);
        # lv_obj_set_event_cb(icon, setup_icon_event_cb);

        box = lv.obj(lv.scr_act(), None)
        box.set_size(500, 80)
        box.align(None, lv.ALIGN.IN_BOTTOM_LEFT, self.LV_HOR_RES // 20,
                     - self.LV_HOR_RES // 40)
        box.set_style_local_value_str(lv.cont.PART.MAIN, lv.STATE.DEFAULT,
                                         "What do you want to do today?")
        
        # delay += LV_DEMO_PRINTER_ANIM_DELAY;
        # lv_demo_printer_anim_in(box, delay);        box = lv.obj(lv.scr_act(), None)
        
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
        self.theme.apply(bg,LV_DEMO_PRINTER_THEME_ICON)
        bg.set_src(src_bg_dsc)
        bg.set_antialias(False)

        icon = lv.img(bg,None)
        icon.set_src(src_icon_dsc)
        icon.set_style_local_image_recolor_opa(lv.img.PART.MAIN, lv.STATE.DEFAULT, lv.OPA.TRANSP)
        icon.align(None, lv.ALIGN.IN_TOP_RIGHT, -30, 30)

        label = lv.label(bg,None)
        label.set_text(txt)
        label.align(None, lv.ALIGN.IN_BOTTOM_LEFT, 30, -30)

        return bg
        
    def anim_in(self,obj,delay):
        a = lv.anim_t()
        a.init()
        a.set_var(obj)
        a.set_time(self.LV_DEMO_PRINTER_ANIM_TIME)
        a.set_delay(delay)
        # a.set_exec_cb(obj.set_y)
        # a.set_values(obj.get_y() -  self.LV_DEMO_PRINTER_ANIM_Y, obj.get_y())
        # a.start()
        obj.fade_in(self.LV_DEMO_PRINTER_ANIM_TIME - 50, self.delay)

drv = driver(width=800,height=480,orientation=ORIENT_LANDSCAPE)
printer = DemoPrinter()
