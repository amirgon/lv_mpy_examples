#!/usr/bin/bash
# This shell scripts sets up the t-watch application
# python modules and images are uploaded to the t-watch
# Demo program for the course on the Internet of Things (IoT) at the
# University of Cape Coast (Ghana)
# Copyright (c) U. Raich April 2020
# This program is released under the MIT license

echo "Setting up the file system for the t-watch program"
dirs="$(ampy ls)"
echo "dirs in /:" $dirs
# check if /lib already exists, create it if not
#
if [[ $dirs == *"/lib"* ]]
then
    echo "/lib directory already exists"
else
    echo "Creating /lib directory"
    ampy mkdir /lib
fi
echo "------------------------------"
echo "Uploading  Python code to /lib"
echo "------------------------------"
echo "uploading theme.py"
ampy put theme.py /lib/theme.py

dirs="$(ampy ls)"
#
# check if the /images folder exists, create it if not
#
if [[ $dirs == *"/images"* ]]
then
    echo "/images directory already exists"
    images="$(ampy ls /images)"    
else
    echo "Creating /images directory"
    ampy mkdir /images
    images=""
fi
images="$(ampy ls /images)"
# echo $images
#
# check it images have already been uploaded, upload them if not
#
if echo $images | grep -w "icon_bright.png" > /dev/null ; then
    echo "icon_bright.png has already been uploaded"
else
    echo "Uploading icon_bright.png"
    ampy put src/images/icon_bright.png /images/icon_bright.png
fi

#
# btn images
#

echo "uploading btn images"

if echo $images | grep -w "bg1_240px_rgb565.bin" > /dev/null ; then
    echo "bg1_240px_rgb565.bin has already been uploaded"
else
    echo "Uploading bg1_240px_rgb565.bin"
    ampy put src/images/bg1_240px_rgb565.bin /images/bg1_240px_rgb565.bin
fi
if echo $images | grep -w "bg2_240px_rgb565.bin" > /dev/null ; then
    echo "bg2_240px_rgb565.bin has already been uploaded"
else
    echo "Uploading bg2_240px_rgb565.bin"
    ampy put src/images/bg2_240px_rgb565.bin /images/bg2_240px_rgb565.bin
fi
if echo $images | grep -w "bg3_240px_rgb565.bin" > /dev/null ; then
    echo "bg3_240px_rgb565.bin has already been uploaded"
else
    echo "Uploading bg3_240px_rgb565.bin"
    ampy put src/images/bg3_240px_rgb565.bin /images/bg3_240px_rgb565.bin
fi

echo "---------------------------"
echo "uploading application icons"
echo "---------------------------"

if echo $images | grep -w "message_64px_argb565.bin" > /dev/null ; then
    echo "message_64pxargb565.bin has already been uploaded"
else
    echo "Uploading message_argb565.bin"
    ampy put src/images/message_64px_argb565.bin /images/message_64px_argb565.bin
fi

if echo $images | grep -w "weather_64px_argb565.bin" > /dev/null ; then
    echo "weather_64px_argb565.bin has already been uploaded"
else
    echo "Uploading weather_argb565.bin"
    ampy put src/images/weather_64px_argb565.bin /images/weather_64px_argb565.bin
fi

if echo $images | grep -w "mondaine_clock_64px_argb565.bin" > /dev/null ; then
    echo "mondaine_clock_64px_argb565.bin has already been uploaded"
else
    echo "Uploading mondaine_clock_64px_argb565.bin"
    ampy put src/images/mondaine_clock_64px_argb565.bin /images/mondaine_clock_64px_argb565.bin
fi

if echo $images | grep -w "stopwatch_64px_argb565.bin" > /dev/null ; then
    echo "stopwatch_64px_argb565.bin has already been uploaded"
else
    echo "Uploading stopwatch_64px_argb565.bin"
    ampy put src/images/stopwatch_64px_argb565.bin /images/stopwatch_64px_argb565.bin
fi

if echo $images | grep -w "alarm_clock_64px_argb565.bin" > /dev/null ; then
    echo "alarm_clock_64px_argb565.bin has already been uploaded"
else
    echo "Uploading alarm_clock_64px_argb565.bin"
    ampy put src/images/alarm_clock_64px_argb565.bin /images/alarm_clock_64px_argb565.bin
fi

if echo $images | grep -w "calendar_64px_argb565.bin" > /dev/null ; then
    echo "calendar_64px_argb565.bin has already been uploaded"
else
    echo "Uploading calendar_64px_argb565.bin"
    ampy put src/images/calendar_64px_argb565.bin /images/calendar_64px_argb565.bin
fi

if echo $images | grep -w "powermeter_64px_argb565.bin" > /dev/null ; then
    echo "powermeter_argb565.bin has already been uploaded"
else
    echo "Uploading powermeter_64px_argb565.bin"
    ampy put src/images/powermeter_64px_argb565.bin /images/powermeter_64px_argb565.bin
fi

if echo $images | grep -w "calculator_64px_argb565.bin" > /dev/null ; then
    echo "calculator_64px_argb565.bin has already been uploaded"
else
    echo "Uploading calculator_64px_argb565.bin"
    ampy put src/images/calculator_64px_argb565.bin /images/calculator_64px_argb565.bin
fi

if echo $images | grep -w "status_64px_argb565.bin" > /dev/null ; then
    echo "status_64px_argb565.bin has already been uploaded"
else
    echo "Uploading status_64px_argb565.bin"
    ampy put src/images/status_64px_argb565.bin /images/status_64px_argb565.bin
fi

if echo $images | grep -w "myapp_64px_argb565.bin" > /dev/null ; then
    echo "myapp_64px_argb565.bin has already been uploaded"
else
    echo "Uploading myapp_64px_argb565.bin"
    ampy put src/images/myapp_64px_argb565.bin /images/myapp_64px_argb565.bin
fi
echo "---------------------------"
echo "uploading weather icons"
echo "---------------------------"

if echo $images | grep -w "c_64px_argb565.bin" > /dev/null ; then
    echo "c_64px_argb565.bin has already been uploaded"
else
    echo "Uploading c_64px_argb565.bin"
    ampy put images/c_64px_argb565.bin /images/c_64px_argb565.bin
fi

if echo $images | grep -w "h_64px_argb565.bin" > /dev/null ; then
    echo "h_64px_argb565.bin has already been uploaded"
else
    echo "Uploading h_64px_argb565.bin"
    ampy put images/h_64px_argb565.bin /images/h_64px_argb565.bin
fi

if echo $images | grep -w "hc_64px_argb565.bin" > /dev/null ; then
    echo "hc_64px_argb565.bin has already been uploaded"
else
    echo "Uploading hc_64px_argb565.bin"
    ampy put images/hc_64px_argb565.bin /images/hc_64px_argb565.bin
fi

if echo $images | grep -w "hr_64px_argb565.bin" > /dev/null ; then
    echo "hr_64px_argb565.bin has already been uploaded"
else
    echo "Uploading hr_64px_argb565.bin"
    ampy put images/hr_64px_argb565.bin /images/hr_64px_argb565.bin
fi

if echo $images | grep -w "lc_64px_argb565.bin" > /dev/null ; then
    echo "lc_64px_argb565.bin has already been uploaded"
else
    echo "Uploading lc_64px_argb565.bin"
    ampy put images/lc_64px_argb565.bin /images/lc_64px_argb565.bin
fi

if echo $images | grep -w "lr_64px_argb565.bin" > /dev/null ; then
    echo "lr_64px_argb565.bin has already been uploaded"
else
    echo "Uploading lr_64px_argb565.bin"
    ampy put images/lr_64px_argb565.bin /images/lr_64px_argb565.bin
fi

if echo $images | grep -w "s_64px_argb565.bin" > /dev/null ; then
    echo "s_64px_argb565.bin has already been uploaded"
else
    echo "Uploading s_64px_argb565.bin"
    ampy put images/s_64px_argb565.bin /images/s_64px_argb565.bin
fi

if echo $images | grep -w "sl_64px_argb565.bin" > /dev/null ; then
    echo "sl_64px_argb565.bin has already been uploaded"
else
    echo "Uploading sl_64px_argb565.bin"
    ampy put images/sl_64px_argb565.bin /images/sl_64px_argb565.bin
fi

if echo $images | grep -w "sn_64px_argb565.bin" > /dev/null ; then
    echo "sn_64px_argb565.bin has already been uploaded"
else
    echo "Uploading sn_64px_argb565.bin"
    ampy put images/sn_64px_argb565.bin /images/sn_64px_argb565.bin
fi

if echo $images | grep -w "t_64px_argb565.bin" > /dev/null ; then
    echo "t_64px_argb565.bin has already been uploaded"
else
    echo "Uploading t_64px_argb565.bin"
    ampy put images/t_64px_argb565.bin /images/t_64px_argb565.bin
fi

if echo $images | grep -w "bg_240px_rgb565.bin" > /dev/null ; then
    echo "bg_240px_rgb565.bin has already been uploaded"
else
    echo "Uploading bg_240px_rgb565.bin"
    ampy put images/bg_240px_rgb565.bin /images/bg_240px_rgb565.bin
fi

echo "---------------------"
echo "uploading setup icons"
echo "---------------------"

if echo $images | grep -w "battery_icon_64px_argb565.bin" > /dev/null ; then
    echo "battery_icon_65px_argb565.bin has already been uploaded"
else
    echo "Uploading battery_icon_64px_argb565.bin"
    ampy put src/images/battery_icon_64px_argb565.bin /images/battery_icon_64px_argb565.bin
fi

if echo $images | grep -w "brightness_64px_argb565.bin" > /dev/null ; then
    echo "brightness_64px_argb565.bin has already been uploaded"
else
    echo "Uploading brightness_64px_argb565.bin"
    ampy put src/images/brightness_64px_argb565.bin images/brightness_64px_argb565.bin
fi

if echo $images | grep -w "move_64px_argb565.bin" > /dev/null ; then
    echo "move_64px_argb565.bin has already been uploaded"
else
    echo "Uploading move_64px_argb565.bin"
    ampy put src/images/move_64px_argb565.bin images/move_64px_argb565.bin
fi

if echo $images | grep -w "wifi_64px_argb565.bin" > /dev/null ; then
    echo "wifi_64px_argb565.bin has already been uploaded"
else
    echo "Uploading wifi_64px_argb565.bin"
    ampy put src/images/wifi_64px_argb565.bin images/wifi_64px_argb565.bin
fi

if echo $images | grep -w "bluetooth_64px_argb565.bin" > /dev/null ; then
    echo "bluetooth_64_px_argb565.bin has already been uploaded"
else
    echo "Uploading bluetooth_argb565.bin"
    ampy put src/images/bluetooth_64px_argb565.bin images/bluetooth_64px_argb565.bin
fi

if echo $images | grep -w "time_64px_argb565.bin" > /dev/null ; then
    echo "time_64px_argb565.bin has already been uploaded"
else
    echo "Uploading time_64px_argb565.bin"
    ampy put src/images/time_64px_argb565.bin images/time_64px_argb565.bin
fi

if echo $images | grep -w "update_64px_argb565.bin" > /dev/null ; then
    echo "update_64px_argb565.bin has already been uploaded"
else
    echo "Uploading update_64px_argb565.bin"
    ampy put src/images/update_64px_argb565.bin images/update_64px_argb565.bin
fi

if echo $images | grep -w "utilities_64px_argb565.bin" > /dev/null ; then
    echo "utilities_64px_argb565.bin has already been uploaded"
else
    echo "Uploading utilities_64px_argb565.bin"
    ampy put src/images/utilities_64px_argb565.bin images/utilities_64px_argb565.bin
fi
if echo $images | grep -w "sound_64px_argb565.bin" > /dev/null ; then
    echo "sound_64px_argb565.bin has already been uploaded"
else
    echo "Uploading sound_64px_argb565.bin"
    ampy put src/images/sound_64px_argb565.bin images/sound_64px_argb565.bin
fi

if echo $images | grep -w "exit_32px_argb565.bin" > /dev/null ; then
    echo "exit_32px_argb565.bin has already been uploaded"
else
    echo "Uploading exit_32px_argb565.bin"
    ampy put src/images/exit_32px_argb565.bin images/exit_32px_argb565.bin
fi

if echo $images | grep -w "setup_32px_argb565.bin" > /dev/null ; then
    echo "setup_32px_argb565.bin has already been uploaded"
else
    echo "Uploading setup_32px_argb565.bin"
    ampy put src/images/setup_32px_argb565.bin images/setup_32px_argb565.bin
fi

if echo $images | grep -w "foot_16px_argb565.bin" > /dev/null ; then
    echo "foot_16px_argb565.bin has already been uploaded"
else
    echo "Uploading foot_16px_argb565.bin"
    ampy put src/images/foot_16px_argb565.bin images/foot_16px_argb565.bin
fi

echo "---------------------"
echo "uploading info icons"
echo "---------------------"

if echo $images | grep -w "info_1_16px_argb565.bin" > /dev/null ; then
    echo "info_1_16px_argb565.bin has already been uploaded"
else
    echo "Uploading info_1_16px_argb565.bin"
    ampy put src/images/info_1_16px_argb565.bin images/info_1_16px_argb565.bin
fi

if echo $images | grep -w "info_2_16px_argb565.bin" > /dev/null ; then
    echo "info_2_16px_argb565.bin has already been uploaded"
else
    echo "Uploading info_2_16px_argb565.bin"
    ampy put src/images/info_2_16px_argb565.bin images/info_2_16px_argb565.bin
fi

if echo $images | grep -w "info_3_16px_argb565.bin" > /dev/null ; then
    echo "info_3_16px_argb565.bin has already been uploaded"
else
    echo "Uploading info_3_16px_argb565.bin"
    ampy put src/images/info_3_16px_argb565.bin images/info_3_16px_argb565.bin
fi

if echo $images | grep -w "info_n_16px_argb565.bin" > /dev/null ; then
    echo "info_n_16px_argb565.bin has already been uploaded"
else
    echo "Uploading info_n_16px_argb565.bin"
    ampy put src/images/info_n_16px_argb565.bin images/info_n_16px_argb565.bin
fi

if echo $images | grep -w "info_fail_16px_argb565.bin" > /dev/null ; then
    echo "info_fail_16px_argb565.bin has already been uploaded"
else
    echo "Uploading info_fail_16px_argb565.bin"
    ampy put src/images/info_fail_16px_argb565.bin images/info_fail_16px_argb565.bin
fi

if echo $images | grep -w "info_ok_16px_argb565.bin" > /dev/null ; then
    echo "info_ok_16px_argb565.bin has already been uploaded"
else
    echo "Uploading info_ok_16px_argb565.bin"
    ampy put src/images/info_ok_16px_argb565.bin images/info_ok_16px_argb565.bin
fi

if echo $images | grep -w "info_update_16px_argb565.bin" > /dev/null ; then
    echo "info_1_16px_argb565.bin has already been uploaded"
else
    echo "Uploading info_update_16px_argb565.bin"
    ampy put src/images/info_update_16px_argb565.bin images/info_update_16px_argb565.bin
fi
