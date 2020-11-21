# Micropython version of the examples in the lvgl documentation
The lvgl documentation provides examples written in C of how to use the different widgets. Figuring out how to use the Micropython language binding is not exactly easy. I want to run lvgl on my LilyGo t-watch but had problems to understand how to do this. In order to play with the lvgl Micropython interface without having problems with external hardware I decided to try the unix port with the SDL2 driver first. This makes me a nice simulator on which I can try programs before replacing the display driver with the st7789 driver and installing them on the t-watch.
In the lvgl documentation you will find under Micropython: "No examples yet", which this repository aims at changing.
## Running the demo programs
All programs run under lv_micropython.In addition you need 
* init_gui.py
* lv_colors.py
which you will find in this repository. These modules must be visible to MicroPython which you can accomplish by copying the files to $HOME/.micropython/lib
