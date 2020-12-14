from GUI import driver
drv = driver()
drv.init_gui()
if not drv.type:
    print("Not running a supported lvgl enabled version of Micropython. Giving up...")
