#!/opt/bin/lv_micropython
import lvgl as lv
import init_gui
import time

def arc_loader(task):
    arc=lv.arc.__cast__(task.user_data)
    angle = arc.get_value()
    print("angle: ",angle)
    angle += 5
    if angle > 360:
        task._del()
    else:
        arc.set_value(angle)
    
# create an arc which acts as a loader

arc = lv.arc(lv.scr_act(),None)
arc.set_bg_angles(0,360)
arc.set_rotation(270)
arc.align(None,lv.ALIGN.CENTER,0,0)

# Create an `lv_task` to update the arc.
# Store the `arc` in the user data
arc.set_value(10)
lv.task_create(arc_loader, 20, lv.TASK_PRIO.LOWEST, arc)

while True:
    lv.task_handler()
    time.sleep_ms(5)
