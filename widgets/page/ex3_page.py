#!/opt/bin/lv_micropython -i
import lvgl as lv
import display_driver

# Create a scroll bar style
style_sb = lv.style_t()
style_sb.init()
#lv.style_copy(style_sb, lv.style_plain)
style_sb.set_bg_color(lv.STATE.DEFAULT,lv.color_make(0,0,0))
style_sb.set_bg_grad_color(lv.STATE.DEFAULT,lv.color_make(0,0,0))
style_sb.set_border_color(lv.STATE.DEFAULT,lv.color_make(0xff,0xff,0xff))
style_sb.set_border_width(lv.STATE.DEFAULT,1)
style_sb.set_border_opa(lv.STATE.DEFAULT,lv.OPA._70)
style_sb.set_radius(lv.STATE.DEFAULT,800)  # large enough to make a circle
style_sb.set_bg_opa(lv.STATE.DEFAULT,lv.OPA._60)
style_sb.set_pad_right(lv.STATE.DEFAULT, 3)
style_sb.set_pad_bottom(lv.STATE.DEFAULT, 3)
style_sb.set_pad_inner(lv.STATE.DEFAULT, 8)        # Scrollbar width

# Create a page
page = lv.page(lv.scr_act())
page.set_size(150, 200)
page.align(None, lv.ALIGN.CENTER, 0, 0)
page.add_style(lv.page.PART.SCROLLABLE, style_sb)           # Set the scrollbar style

# Create a label on the page
label = lv.label(page)
label.set_long_mode(lv.label.LONG.BREAK)       # Automatically break long lines
label.set_width(page.get_fit_width())          # Set the label width to max value to not show hor. scroll bars
label.set_text("""Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco
laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure
dolor in reprehenderit in voluptate velit esse cillum dolore
eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa
qui officia deserunt mollit anim id est laborum.""")
