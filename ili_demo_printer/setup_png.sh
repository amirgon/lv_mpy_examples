#!/usr/bin/bash
# This shell scripts sets up the demo_printer application
# python modules and images are uploaded to the t-watch
# Demo program for the course on the Internet of Things (IoT) at the
# University of Cape Coast (Ghana)
# Copyright (c) U. Raich April 2020
# This program is released under the MIT license

echo "Setting up the file system for the demo_printer application"
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
echo "uploading filesys_driver.py"
ampy put filesys_driver.py /lib/filesys_driver.py

dirs="$(ampy ls)"
#
# check if the /images folder exists, create it if not
#
if [[ $dirs == *"/font"* ]]
then
    echo "/font directory already exists"
    fonts="$(ampy ls /font)"    
else
    echo "Creating /font directory"
    ampy mkdir /font
    ampy mkdir /font/png
fi

echo $fonts
#
# check it fonts have already been uploaded, upload them if not
#
if echo $fonts | grep -w "montserrat-10.bin" > /dev/null ; then
    echo "montserrat-10.bin has already been uploaded"
else
    echo "Uploading montserrat-10.bin"
    ampy put font/montserrat-10.bin /font/montserrat-10.bin
fi

if echo $fonts | grep -w "montserrat-14.bin" > /dev/null ; then
    echo "montserrat-14.bin has already been uploaded"
else
    echo "Uploading montserrat-14.bin"
    ampy put font/montserrat-14.bin /font/montserrat-14.bin
fi

dirs="$(ampy ls)"
#
# check if the /images folder exists, create it if not
#
if [[ $dirs == *"/images"* ]]
then
    echo "/images directory already exists"   
else
    echo "Creating /images directory"
    ampy mkdir /images
fi

dirs="$(ampy ls /images)"

if [[ $dirs == *"/png"* ]]
then
    echo "/images/png directory already exists"
else
    echo "Creating /images/png directory"
    ampy mkdir /images/png
fi

images="$(ampy ls /images/png)"

#
# check it images have already been uploaded, upload them if not
#
if echo $images | grep -w "icon_bright_12x12.png" > /dev/null ; then
    echo "icon_bright_12x12.png has already been uploaded"
else
    echo "Uploading icon_bright_12x12.png"
    ampy put images/png/icon_bright_12x12.png /images/png/icon_bright_12x12.png
fi

if echo $images | grep -w "icon_eco_15x13.png" > /dev/null ; then
    echo "icon_eco_15x13.png has already been uploaded"
else
    echo "Uploading icon_eco15x13.png"
    ampy put images/png/icon_eco_15x13.png /images/png/icon_eco_15x13.png
fi

if echo $images | grep -w "icon_hue_12x12.png" > /dev/null ; then
    echo "icon_hue_12x12.png has already been uploaded"
else
    echo "Uploading icon_hue_12x12.png"
    ampy put images/png/icon_hue_12x12.png /images/png/icon_hue_12x12.png
fi

if echo $images | grep -w "icon_pc_16x13.png" > /dev/null ; then
    echo "icon_pc_16x13.png has already been uploaded"
else
    echo "Uploading icon_pc_16x13.png"
    ampy put images/png/icon_pc_16x13.png /images/png/icon_pc_16x13.png
fi

if echo $images | grep -w "icon_tel_14x14.png" > /dev/null ; then
    echo "icon_tel_14x14.png has already been uploaded"
else
    echo "Uploading icon_tel_14x14.png"
    ampy put images/png/icon_tel_14x14.png /images/png/icon_tel_14x14.png
fi

if echo $images | grep -w "icon_wifi_20x14.png" > /dev/null ; then
    echo "icon_wifi_20x14.png has already been uploaded"
else
    echo "Uploading icon_wifi_20x14.png"
    ampy put images/png/icon_wifi_20x14.png /images/png/icon_wifi_20x14.png
fi

#
# btn images
#

echo "uploading btn images"

if echo $images | grep -w "img_btn_bg_1_70x86.png" > /dev/null ; then
    echo "img_btn_bg_1_70x86.png has already been uploaded"
else
    echo "Uploading img_btn_bg_1_70x86.png"
    ampy put images/png/img_btn_bg_1_70x86.png /images/png/img_btn_bg_1_70x86.png
fi

if echo $images | grep -w "img_btn_bg_2_70x86.png" > /dev/null ; then
    echo "img_btn_bg_2_70x86.png has already been uploaded"
else
    echo "Uploading img_btn_bg_2_70x86.png"
    ampy put images/png/img_btn_bg_2_70x86.png /images/png/img_btn_bg_2_70x86.png
fi

if echo $images | grep -w "img_btn_bg_3_70x86.png" > /dev/null ; then
    echo "img_btn_bg_3_70x86.png has already been uploaded"
else
    echo "Uploading img_btn_bg_3_70x86.png"
    ampy put images/png/img_btn_bg_3_70x86.png /images/png/img_btn_bg_3_70x86.png
fi

if echo $images | grep -w "img_btn_bg_4_70x86.png" > /dev/null ; then
    echo "img_btn_bg_4_70x86.png has already been uploaded"
else
    echo "Uploading img_btn_bg_4_70x86.png"
    ampy put images/png/img_btn_bg_4_70x86.png /images/png/img_btn_bg_4_70x86.png
fi

echo "uploading images for copy, scan, print and setup"

if echo $images | grep -w "img_copy_20x24.png" > /dev/null ; then
    echo "img_copy_20x24.png has already been uploaded"
else
    echo "Uploading img_copy_20x24.png"
    ampy put images/png/img_copy_20x24.png /images/png/img_copy_20x24.png
fi

if echo $images | grep -w "img_scan_20x24.png" > /dev/null ; then
    echo "img_scan_20x24.png has already been uploaded"
else
    echo "Uploading img_scan_20x24.png"
    ampy put images/png/img_scan_20x24.png /images/png/img_scan_20x24.png
fi

if echo $images | grep -w "img_print_26x26.png" > /dev/null ; then
    echo "img_print_26x26.png has already been uploaded"
else
    echo "Uploading img_print_26x26.png"
    ampy put images/png/img_print_26x26.png /images/png/img_print_26x26.png
fi

if echo $images | grep -w "img_setup_25x25.png" > /dev/null ; then
    echo "img_setup_25x25.png has already been uploaded"
else
    echo "Uploading img_setup_25x25.png"
    ampy put images/png/img_setup_25x25.png /images/png/img_setup_25x25.png
fi

echo "Uploading images for cloud, internet, no_internet, phone, mobile, usb, wave"

if echo $images | grep -w "img_cloud_37x23.png" > /dev/null ; then
    echo "img_cloud_37x23.png has already been uploaded"
else
    echo "Uploading img_cloud_37x23.png"
    ampy put images/png/img_cloud_37x23.png /images/png/img_cloud_37x23.png
fi

if echo $images | grep -w "img_internet_26x26.png" > /dev/null ; then
    echo "img_internet_26x26.png has already been uploaded"
else
    echo "Uploading img_internet_26x26.png"
    ampy put images/png/img_internet_26x26.png /images/png/img_internet_26x26.png
fi

if echo $images | grep -w "img_no_internet_17x17.png" > /dev/null ; then
    echo "img_no_internet_17x17.png has already been uploaded"
else
    echo "Uploading img_no_internet_17x17.png"
    ampy put images/png/img_no_internet_17x17.png /images/png/img_no_internet_17x17.png
fi

if echo $images | grep -w "img_phone_31x40.png" > /dev/null ; then
    echo "img_phone_31x40.png has already been uploaded"
else
    echo "Uploading img_phone_31x40.png"
    ampy put images/png/img_phone_31x40.png /images/png/img_phone_31x40.png
fi

if echo $images | grep -w "img_mobile_20x24.png" > /dev/null ; then
    echo "img_mobile_20x24.png has already been uploaded"
else
    echo "Uploading img_mobile_20x24.png"
    ampy put images/png/img_mobile_20x24.png /images/png/img_mobile_20x24.png
fi

if echo $images | grep -w "img_usb_25x25.png" > /dev/null ; then
    echo "img_usb_25x25.png has already been uploaded"
else
    echo "Uploading img_usb_25x25.png"
    ampy put images/png/img_usb_25x25.png /images/png/img_usb_25x25.png
fi

if echo $images | grep -w "img_wave_11x19.png" > /dev/null ; then
    echo "img_wave_11x19.png has already been uploaded"
else
    echo "Uploading img_wave_11x19.png"
    ampy put images/png/img_wave_11x19.png /images/png/img_wave_11x19.png
fi

echo "Uploading images printer2 ready "

if echo $images | grep -w "img_ready_63x63.png" > /dev/null ; then
    echo "img_ready_63x63.png has already been uploaded"
else
    echo "Uploading img_ready_63x63.png"
    ampy put images/png/img_ready_63x63.png /images/png/img_ready_63x63.png
fi

if echo $images | grep -w "img_printer2_43x42.png" > /dev/null ; then
    echo "img_printer2_43x42.png has already been uploaded"
else
    echo "Uploading img_printer2_43x42.png"
    ampy put images/png/img_printer2_43x42.png /images/png/img_printer2_43x42.png
fi

echo "Uploading scan_example"

if echo $images | grep -w "scan_example_250x163.png" > /dev/null ; then
    echo "scan_example_250x163.png has already been uploaded"
else
    echo "Uploading img_scan_example_250x163.png"
    ampy put images/png/scan_example_250x163.png /images/png/scan_example_250x163.png
fi
