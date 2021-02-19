#!/opt/bin/lv_micropython -i
import lvgl as lv
from display_driver_utils import driver,ORIENT_LANDSCAPE
from lv_colors import lv_colors
from theme import Theme, LV_DEMO_PRINTER_BLUE,LV_DEMO_PRINTER_TITLE_PAD,LV_DEMO_PRINTER_THEME_TITLE
import ulogging as logging

class DemoPrinter(object):
    
    def __init__(self):
        self.LV_HOR_RES = lv.scr_act().get_disp().driver.hor_res
        self.LV_VER_RES = lv.scr_act().get_disp().driver.ver_res
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
        self.icon_copy_data = None
        self.icon_copy_dsc = None
        self.icon_scan_data = None
        self.icon_scan_dsc = None
        self.icon_setup_data = None
        self.icon_setup_dsc = None
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
        #lv_demo_printer_anim_in(icon, delay);

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

    def add_icon(parent,src_bg_dsc,src_icon_dsc,txt):
        bg = lv.img(parent,None)
        gb.set_click(True)
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
        
        
drv = driver(width=800,height=480,orientation=ORIENT_LANDSCAPE)
printer = DemoPrinter()
