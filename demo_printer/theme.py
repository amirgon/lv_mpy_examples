import lvgl as lv
from display_driver_utils import driver,ORIENT_LANDSCAPE
from lv_colors import lv_colors
import ulogging as logging

LV_THEME_DEFAULT_COLOR_PRIMARY=lv.color_hex(0x01a2b1)
LV_THEME_DEFAULT_COLOR_SECONDARY=lv.color_hex(0x44d1b6)
LV_DEMO_PRINTER_WHITE      = lv_colors.WHITE
LV_DEMO_PRINTER_LIGHT      = lv.color_hex(0xf3f8fe)
LV_DEMO_PRINTER_GRAY       = lv.color_hex(0x8a8a8a)
LV_DEMO_PRINTER_LIGHT_GRAY = lv.color_hex(0xc4c4c4)
LV_DEMO_PRINTER_BLUE       = lv.color_hex(0x2f3243) # 006fb6
LV_DEMO_PRINTER_GREEN      = lv.color_hex(0x4cb242)
LV_DEMO_PRINTER_RED        = lv.color_hex(0xd51732)

LV_RADIUS_CIRCLE           = 0x7FFF  # A very big radius to always draw as circle
LV_DEMO_PRINTER_TITLE_PAD  = 35
LV_DEMO_PRINTER_THEME_TITLE = lv.THEME.CUSTOM_START
LV_DEMO_PRINTER_THEME_LABEL_WHITE = lv.THEME.CUSTOM_START + 1
LV_DEMO_PRINTER_THEME_ICON = lv.THEME.CUSTOM_START + 2
LV_DEMO_PRINTER_THEME_BTN_BORDER = lv.THEME.CUSTOM_START + 3
LV_DEMO_PRINTER_THEME_BTN_CIRCLE = lv.THEME.CUSTOM_START + 4
LV_DEMO_PRINTER_THEME_BOX_BORDER = lv.THEME.CUSTOM_START + 5
LV_DEMO_PRINTER_THEME_BTN_BACK = lv.THEME.CUSTOM_START + 6

class Theme():
    def __init__(self):
        self.LV_HOR_RES = lv.scr_act().get_disp().driver.hor_res
        self.LV_VER_RES = lv.scr_act().get_disp().driver.ver_res
        
        self.style_pad = lv.style_t()
        self.style_pad.init()
        self.style_pad.set_pad_top(lv.STATE.DEFAULT, self.LV_VER_RES // 30)
        self.style_pad.set_pad_bottom(lv.STATE.DEFAULT, self.LV_VER_RES // 30)
        self.style_pad.set_pad_left(lv.STATE.DEFAULT, self.LV_VER_RES // 40)
        self.style_pad.set_pad_right(lv.STATE.DEFAULT, self.LV_VER_RES // 40)

        self.style_circle = lv.style_t()       
        self.style_circle.init()
        self.style_circle.set_radius(lv.STATE.DEFAULT, LV_RADIUS_CIRCLE)

        self.style_bg = lv.style_t()
        self.style_bg.init()
        self.style_bg.set_bg_opa(lv.STATE.DEFAULT, lv.OPA.COVER)
        self.style_bg.set_bg_color(lv.STATE.DEFAULT,LV_DEMO_PRINTER_LIGHT)
        self.style_bg.set_text_font(lv.STATE.DEFAULT, self.get_font_normal())

        self.style_box = lv.style_t()
        self.style_box.init()
        
        self.style_box.set_bg_opa(lv.STATE.DEFAULT, lv.OPA.COVER)
        self.style_box.set_radius(lv.STATE.DEFAULT, 10)
        self.style_box.set_value_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_BLUE)
        self.style_box.set_value_font(lv.STATE.DEFAULT, self.get_font_normal())

        self.style_box_border = lv.style_t()
        self.style_box_border.init()
        self.style_box_border.set_border_width(lv.STATE.DEFAULT, 2)
        self.style_box_border.set_border_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_GRAY)
        self.style_box_border.set_text_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_BLUE)
    
        self.style_title = lv.style_t()
        self.style_title.init()
        self.style_title.set_text_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_WHITE)
        self.style_title.set_text_font(lv.STATE.DEFAULT, self.get_font_subtitle())

        self.style_label = lv.style_t()
        self.style_label.init()
        self.style_label.set_text_font(lv.STATE.DEFAULT, self.get_font_normal())
        
        self.style_label_white = lv.style_t()
        self.style_label_white.init()
        self.style_label_white.set_text_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_WHITE)
        
        self.style_btn = lv.style_t()
        self.style_btn.init()
        self.style_btn.set_radius(lv.STATE.DEFAULT, 10)
        self.style_btn.set_bg_opa(lv.STATE.DEFAULT, lv.OPA.COVER)
        self.style_btn.set_bg_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_BLUE)
        self.style_btn.set_bg_color(lv.STATE.PRESSED, LV_DEMO_PRINTER_BLUE.color_darken(lv.OPA._20))
        self.style_btn.set_text_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_WHITE)
        self.style_btn.set_value_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_WHITE)
        self.style_btn.set_pad_top(lv.STATE.DEFAULT, self.LV_VER_RES // 40)
        self.style_btn.set_pad_bottom(lv.STATE.DEFAULT, self.LV_VER_RES // 40)

        self.style_btn_border = lv.style_t()
        self.style_btn_border.init()
        self.style_btn.set_radius(lv.STATE.DEFAULT, LV_RADIUS_CIRCLE)
        self.style_btn_border.set_border_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_WHITE)
        self.style_btn_border.set_border_width(lv.STATE.DEFAULT, 2)
        self.style_btn_border.set_bg_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
        self.style_btn_border.set_bg_opa(lv.STATE.PRESSED, lv.OPA._30)
        self.style_btn_border.set_bg_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_WHITE)
        self.style_btn_border.set_bg_color(lv.STATE.PRESSED, LV_DEMO_PRINTER_WHITE)
        self.style_btn_border.set_text_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_WHITE)
        self.style_btn_border.set_value_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_WHITE)
        self.style_btn_border.set_transition_prop_3(lv.STATE.DEFAULT, lv.STYLE.BG_OPA)

        self.style_icon = lv.style_t()
        self.style_icon.init()
        self.style_icon.set_text_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_WHITE)
        self.style_icon.set_transform_zoom(lv.STATE.PRESSED, 245)
        self.style_icon.set_transition_time(lv.STATE.DEFAULT, 100)
        self.style_icon.set_transition_delay(lv.STATE.PRESSED, 0)
        self.style_icon.set_transition_delay(lv.STATE.DEFAULT, 70)
        self.style_icon.set_transition_prop_1(lv.STATE.DEFAULT, lv.STYLE.TRANSFORM_ZOOM)
        self.style_icon.set_value_font(lv.STATE.DEFAULT, self.get_font_subtitle())
                
        self.style_back = lv.style_t()
        self.style_back.init()
        self.style_back.set_value_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_WHITE)
        self.style_back.set_value_color(lv.STATE.PRESSED, LV_DEMO_PRINTER_LIGHT_GRAY)
        self.style_back.set_value_str(lv.STATE.DEFAULT, lv.SYMBOL.LEFT)
        self.style_back.set_value_font(lv.STATE.DEFAULT, self.get_font_subtitle())
        
        self.style_bar_indic = lv.style_t()
        self.style_bar_indic.init()
        self.style_bar_indic.set_bg_opa(lv.STATE.DEFAULT, lv.OPA.COVER)
        self.style_bar_indic.set_radius(lv.STATE.DEFAULT, 10)

        self.style_scrollbar = lv.style_t()
        self.style_scrollbar.init()
        self.style_scrollbar.set_bg_opa(lv.STATE.DEFAULT, lv.OPA.COVER)
        self.style_scrollbar.set_radius(lv.STATE.DEFAULT, LV_RADIUS_CIRCLE)
        self.style_scrollbar.set_bg_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_LIGHT_GRAY)
        self.style_scrollbar.set_size(lv.STATE.DEFAULT, self.LV_HOR_RES // 80)
        self.style_scrollbar.set_pad_right(lv.STATE.DEFAULT, self.LV_HOR_RES // 60)

        self.style_list_btn = lv.style_t()
        self.style_list_btn.init()
        self.style_list_btn.set_bg_opa(lv.STATE.DEFAULT, lv.OPA.COVER)
        self.style_list_btn.set_bg_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_WHITE)
        self.style_list_btn.set_bg_color(lv.STATE.PRESSED, LV_DEMO_PRINTER_LIGHT_GRAY)
        self.style_list_btn.set_bg_color(lv.STATE.CHECKED, LV_DEMO_PRINTER_GRAY)
        self.style_list_btn.set_bg_color(lv.STATE.CHECKED | lv.STATE.PRESSED, LV_DEMO_PRINTER_GRAY.color_darken(lv.OPA._20))
        self.style_list_btn.set_text_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_BLUE)
        self.style_list_btn.set_text_color(lv.STATE.PRESSED, LV_DEMO_PRINTER_BLUE.color_darken(lv.OPA._20))
        self.style_list_btn.set_text_color(lv.STATE.CHECKED, LV_DEMO_PRINTER_WHITE)
        self.style_list_btn.set_text_color(lv.STATE.CHECKED | lv.STATE.PRESSED, LV_DEMO_PRINTER_WHITE)
        self.style_list_btn.set_image_recolor(lv.STATE.DEFAULT, LV_DEMO_PRINTER_BLUE)
        self.style_list_btn.set_image_recolor(lv.STATE.PRESSED, LV_DEMO_PRINTER_BLUE.color_darken(lv.OPA._20))
        self.style_list_btn.set_image_recolor(lv.STATE.CHECKED, LV_DEMO_PRINTER_WHITE)
        self.style_list_btn.set_image_recolor(lv.STATE.CHECKED | lv.STATE.PRESSED, LV_DEMO_PRINTER_WHITE)
        self.style_list_btn.set_pad_left(lv.STATE.DEFAULT, self.LV_HOR_RES // 25)
        self.style_list_btn.set_pad_right(lv.STATE.DEFAULT, self.LV_HOR_RES // 25)
        self.style_list_btn.set_pad_top(lv.STATE.DEFAULT, self.LV_HOR_RES // 100)
        self.style_list_btn.set_pad_bottom(lv.STATE.DEFAULT, self.LV_HOR_RES // 100)
        self.style_list_btn.set_pad_inner(lv.STATE.DEFAULT, self.LV_HOR_RES // 50)
        
        self.style_ddlist_list = lv.style_t()
        self.style_ddlist_list.init()
        self.style_ddlist_list.set_text_line_space(lv.STATE.DEFAULT, self.LV_VER_RES // 25)
        self.style_ddlist_list.set_shadow_width(lv.STATE.DEFAULT, self.LV_VER_RES // 20)
        self.style_ddlist_list.set_shadow_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_GRAY)

        self.style_ddlist_selected = lv.style_t()
        self.style_ddlist_selected.init()
        self.style_ddlist_selected.set_bg_opa(lv.STATE.DEFAULT, lv.OPA.COVER)
        self.style_ddlist_selected.set_bg_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_BLUE)
        self.style_ddlist_selected.set_bg_color(lv.STATE.PRESSED, LV_DEMO_PRINTER_LIGHT_GRAY)
        self.style_ddlist_selected.set_text_color(lv.STATE.PRESSED, LV_DEMO_PRINTER_GRAY.color_darken(lv.OPA._20))
        

        self.style_sw_knob = lv.style_t()
        self.style_sw_knob.init()
        self.style_sw_knob.set_bg_opa(lv.STATE.DEFAULT, lv.OPA.COVER)
        self.style_sw_knob.set_bg_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_WHITE)
        self.style_sw_knob.set_radius(lv.STATE.DEFAULT, LV_RADIUS_CIRCLE)
        self.style_sw_knob.set_pad_top(lv.STATE.DEFAULT, - 4)
        self.style_sw_knob.set_pad_bottom(lv.STATE.DEFAULT, - 4)
        self.style_sw_knob.set_pad_left(lv.STATE.DEFAULT, - 4)
        self.style_sw_knob.set_pad_right(lv.STATE.DEFAULT,  - 4)

        self.style_slider_knob = lv.style_t()
        self.style_slider_knob.init()
        self.style_slider_knob.set_bg_opa(lv.STATE.DEFAULT, lv.OPA.COVER)
        self.style_slider_knob.set_bg_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_BLUE)
        self.style_slider_knob.set_border_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_WHITE)
        self.style_slider_knob.set_border_width(lv.STATE.DEFAULT, 3)
        self.style_slider_knob.set_radius(lv.STATE.DEFAULT, LV_RADIUS_CIRCLE)
        self.style_slider_knob.set_pad_top(lv.STATE.DEFAULT, 10)
        self.style_slider_knob.set_pad_bottom(lv.STATE.DEFAULT, 10)
        self.style_slider_knob.set_pad_left(lv.STATE.DEFAULT, 10)
        self.style_slider_knob.set_pad_right(lv.STATE.DEFAULT,  10)
        self.style_slider_knob.set_pad_top(lv.STATE.PRESSED, 14)
        self.style_slider_knob.set_pad_bottom(lv.STATE.PRESSED, 14)
        self.style_slider_knob.set_pad_left(lv.STATE.PRESSED, 14)
        self.style_slider_knob.set_pad_right(lv.STATE.PRESSED,  14)
        self.style_slider_knob.set_transition_time(lv.STATE.DEFAULT, 150)
        self.style_slider_knob.set_transition_delay(lv.STATE.PRESSED, 0)
        self.style_slider_knob.set_transition_delay(lv.STATE.DEFAULT, 70)
        self.style_slider_knob.set_transition_prop_1(lv.STATE.DEFAULT, lv.STYLE.PAD_BOTTOM)
        self.style_slider_knob.set_transition_prop_2(lv.STATE.DEFAULT, lv.STYLE.PAD_TOP)
        self.style_slider_knob.set_transition_prop_3(lv.STATE.DEFAULT, lv.STYLE.PAD_LEFT)
        self.style_slider_knob.set_transition_prop_4(lv.STATE.DEFAULT, lv.STYLE.PAD_RIGHT)
        
        self.style_arc_indic = lv.style_t()
        self.style_arc_indic.init()
        self.style_arc_indic.set_line_width(lv.STATE.DEFAULT, 5)
        self.style_arc_indic.set_line_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_WHITE)

        self.style_arc_bg = lv.style_t()
        self.style_arc_bg.init()
        self.style_arc_bg.set_value_color(lv.STATE.DEFAULT, LV_DEMO_PRINTER_WHITE)
        self.style_arc_bg.set_value_font(lv.STATE.DEFAULT, self.get_font_title())
    
    def apply(self,obj,name):
        if name == lv.THEME.NONE:
            return
        if name == lv.THEME.SCR:
            obj.add_style(obj.PART.MAIN,self.style.bg)
            return
        if name == lv.THEME.OBJ:
            obj.add_style(obj.PART.MAIN,self.style_box)
            return
        
        if name == LV_DEMO_PRINTER_THEME_TITLE:
            obj.add_style(obj.PART.MAIN,self.style_title)
            return
        
        if name ==  LV_DEMO_PRINTER_THEME_BOX_BORDER:
            obj.add_style(lv.obj.PART.MAIN,self.style_box)
            obj.add_style(lv.obj.PART.MAIN,self.style_box_border)
            return


        if name == lv.THEME.CONT:
            obj.add_style(obj,self.style_box)
            return

        if name == LV_DEMO_PRINTER_THEME_BTN_CIRCLE:
            obj.add_style(lv.obj.PART.MAIN,style_btn);
            obj.add_style(lv.obj.PART.MAIN,self.style_circle);
            return

        if name == LV_DEMO_PRINTER_THEME_BTN_BORDER:
            obj.add_style(lv.obj.PART.MAIN,style_btn)
            obj.add_style(lv.obj.PART.MAIN,self.style_btn_border)
            return

        if name == LV_DEMO_PRINTER_THEME_BTN_BACK:
            obj.add_style(lv.obj.PART.MAIN,self.style_back)
            return

        if name == lv.THEME.BTN:
            obj.add_style(lv.obj.PART.MAIN,self.style_btn)
            return

        if name == LV_DEMO_PRINTER_THEME_ICON:
            obj.add_style(lv.obj.PART.MAIN,self.style_icon)
            return
        
        '''
        if name == LV_THEME_BAR:
            lv_obj_clean_style_list(obj, LV_BAR_PART_BG);
            list = lv_obj_get_style_list(obj, LV_BAR_PART_BG);

            lv_obj_clean_style_list(obj, LV_BAR_PART_INDIC);
            list = lv_obj_get_style_list(obj, LV_BAR_PART_INDIC);
            _lv_style_list_add_style(list, &style_bar_indic);
            break;

        case LV_THEME_IMAGE:
            lv_obj_clean_style_list(obj, LV_IMG_PART_MAIN);
            list = lv_obj_get_style_list(obj, LV_IMG_PART_MAIN);
            break;
        '''
        if name == lv.THEME.LABEL:
            obj.add_style(lv.label.PART.MAIN,self.style_label)       
            return
        
        if name == LV_DEMO_PRINTER_THEME_TITLE:
            obj.add_style(lv.obj.PART.MAIN,swelf.style_title)
            return

        if name ==  LV_DEMO_PRINTER_THEME_LABEL_WHITE:
            obj.add_style(lv.obj.PART.MAIN,self.style_label_white)
            return
        '''
        case LV_THEME_SLIDER:
            lv_obj_clean_style_list(obj, LV_SLIDER_PART_BG);
            list = lv_obj_get_style_list(obj, LV_SLIDER_PART_BG);
            _lv_style_list_add_style(list, &style_sw_bg);

            lv_obj_clean_style_list(obj, LV_SLIDER_PART_INDIC);
            list = lv_obj_get_style_list(obj, LV_SLIDER_PART_INDIC);

            lv_obj_clean_style_list(obj, LV_SLIDER_PART_KNOB);
            list = lv_obj_get_style_list(obj, LV_SLIDER_PART_KNOB);
            _lv_style_list_add_style(list, &style_slider_knob);
            break;

        case LV_THEME_LIST:
            lv_obj_clean_style_list(obj, LV_LIST_PART_BG);
            list = lv_obj_get_style_list(obj, LV_LIST_PART_BG);
            _lv_style_list_add_style(list, &style_box);

            lv_obj_clean_style_list(obj, LV_LIST_PART_SCROLLABLE);
            list = lv_obj_get_style_list(obj, LV_LIST_PART_SCROLLABLE);

            lv_obj_clean_style_list(obj, LV_LIST_PART_SCROLLBAR);
            list = lv_obj_get_style_list(obj, LV_LIST_PART_SCROLLBAR);
            _lv_style_list_add_style(list, &style_scrollbar);
            break;

        case LV_THEME_LIST_BTN:
            lv_obj_clean_style_list(obj, LV_BTN_PART_MAIN);
            list = lv_obj_get_style_list(obj, LV_BTN_PART_MAIN);
            _lv_style_list_add_style(list, &style_list_btn);
            break;


        case LV_THEME_ARC:
            lv_obj_clean_style_list(obj, LV_ARC_PART_BG);
            list = lv_obj_get_style_list(obj, LV_ARC_PART_BG);
            _lv_style_list_add_style(list, &style_arc_bg);

            lv_obj_clean_style_list(obj, LV_ARC_PART_INDIC);
            list = lv_obj_get_style_list(obj, LV_ARC_PART_INDIC);
            _lv_style_list_add_style(list, &style_arc_indic);
            break;


        case LV_THEME_SWITCH:
            lv_obj_clean_style_list(obj, LV_SWITCH_PART_BG);
            list = lv_obj_get_style_list(obj, LV_SWITCH_PART_BG);
            _lv_style_list_add_style(list, &style_sw_bg);

            lv_obj_clean_style_list(obj, LV_SWITCH_PART_INDIC);
            list = lv_obj_get_style_list(obj, LV_SWITCH_PART_INDIC);
            _lv_style_list_add_style(list, &style_sw_indic);

            lv_obj_clean_style_list(obj, LV_SWITCH_PART_KNOB);
            list = lv_obj_get_style_list(obj, LV_SWITCH_PART_KNOB);
            _lv_style_list_add_style(list, &style_sw_knob);
            break;

        case LV_THEME_DROPDOWN:
            lv_obj_clean_style_list(obj, LV_DROPDOWN_PART_MAIN);
            list = lv_obj_get_style_list(obj, LV_DROPDOWN_PART_MAIN);
            _lv_style_list_add_style(list, &style_btn);
            _lv_style_list_add_style(list, &style_pad);

            lv_obj_clean_style_list(obj, LV_DROPDOWN_PART_LIST);
            list = lv_obj_get_style_list(obj, LV_DROPDOWN_PART_LIST);
            _lv_style_list_add_style(list, &style_box);
            _lv_style_list_add_style(list, &style_ddlist_list);
            _lv_style_list_add_style(list, &style_pad);

            lv_obj_clean_style_list(obj, LV_DROPDOWN_PART_SELECTED);
            list = lv_obj_get_style_list(obj, LV_DROPDOWN_PART_SELECTED);
            _lv_style_list_add_style(list, &style_ddlist_selected);

            lv_obj_clean_style_list(obj, LV_DROPDOWN_PART_SCROLLBAR);
            list = lv_obj_get_style_list(obj, LV_DROPDOWN_PART_SCROLLBAR);
            _lv_style_list_add_style(list, &style_scrollbar);
            break;
        '''
    def get_font_small(self):
        return lv.font_montserrat_14
        
    def get_font_normal(self):
        return lv.font_montserrat_22

    def get_font_subtitle(self):
        return lv.font_montserrat_28

    def get_font_title(self):
        return lv.font_montserrat_48
