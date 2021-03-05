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
    images="$(ampy ls /images)"    
else
    echo "Creating /images directory"
    ampy mkdir /images
fi
image_dir = "$(ampy ls /images)"
if [[ $dirs == *"/png"* ]]
then
    echo "/images/png directory already exists"
    images="$(ampy ls /images/png)"    
else
    echo "Creating /images/png directory"
    ampy mkdir /images/png
fi

images="$(ampy ls /images/png)"
echo $images
#
# check it images have already been uploaded, upload them if not
#
if echo $images | grep -w "icon_bright.png" > /dev/null ; then
    echo "icon_bright.png has already been uploaded"
else
    echo "Uploading icon_bright.png"
    ampy put images/png/icon_bright.png /images/png/icon_bright.png
fi

if echo $images | grep -w "icon_eco.png" > /dev/null ; then
    echo "icon_eco.png has already been uploaded"
else
    echo "Uploading icon_eco.png"
    ampy put images/png/icon_eco.png /images/png/icon_eco.png
fi

if echo $images | grep -w "icon_hue.png" > /dev/null ; then
    echo "icon_hue.png has already been uploaded"
else
    echo "Uploading icon_hue.png"
    ampy put images/png/icon_hue.png /images/png/icon_hue.png
fi

if echo $images | grep -w "icon_pc.png" > /dev/null ; then
    echo "icon_pc.png has already been uploaded"
else
    echo "Uploading icon_pc.png"
    ampy put images/png/icon_pc.png /images/png/icon_pc.png
fi

if echo $images | grep -w "icon_tel.png" > /dev/null ; then
    echo "icon_tel.png has already been uploaded"
else
    echo "Uploading icon_tel.png"
    ampy put images/png/icon_tel.png /images/png/icon_tel.png
fi

if echo $images | grep -w "icon_wifi.png" > /dev/null ; then
    echo "icon_wifi.png has already been uploaded"
else
    echo "Uploading icon_wifi.png"
    ampy put images/png/icon_wifi.png /images/png/icon_wifi.png
fi

#
# btn images
#

echo "uploading btn images"

if echo $images | grep -w "img_btn_bg_1.png" > /dev/null ; then
    echo "img_btn_bg_1.png has already been uploaded"
else
    echo "Uploading img_btn_bg_1.png"
    ampy put images/png/img_btn_bg_1.png /images/png/img_btn_bg_1.png
fi

if echo $images | grep -w "img_btn_bg_2.png" > /dev/null ; then
    echo "img_btn_bg_2.png has already been uploaded"
else
    echo "Uploading img_btn_bg_2.png"
    ampy put images/png/img_btn_bg_2.png /images/png/img_btn_bg_2.png
fi

if echo $images | grep -w "img_btn_bg_3.png" > /dev/null ; then
    echo "img_btn_bg_3.png has already been uploaded"
else
    echo "Uploading img_btn_bg_3.png"
    ampy put images/png/img_btn_bg_3.png /images/png/img_btn_bg_3.png
fi

if echo $images | grep -w "img_btn_bg_4.png" > /dev/null ; then
    echo "img_btn_bg_4.png has already been uploaded"
else
    echo "Uploading img_btn_bg_4.png"
    ampy put images/png/img_btn_bg_4.png /images/png/img_btn_bg_4.png
fi

echo "uploading images for copy, scan, print and setup"

if echo $images | grep -w "img_copy.png" > /dev/null ; then
    echo "img_copy.png has already been uploaded"
else
    echo "Uploading img_copy.png"
    ampy put images/png/img_copy.png /images/png/img_copy.png
fi

if echo $images | grep -w "img_scan.png" > /dev/null ; then
    echo "img_scan.png has already been uploaded"
else
    echo "Uploading img_scan.png"
    ampy put images/png/img_scan.png /images/png/img_scan.png
fi

if echo $images | grep -w "img_print.png" > /dev/null ; then
    echo "img_print.png has already been uploaded"
else
    echo "Uploading img_print.png"
    ampy put images/png/img_print.png /images/png/img_print.png
fi

if echo $images | grep -w "img_setup.png" > /dev/null ; then
    echo "img_setup.png has already been uploaded"
else
    echo "Uploading img_setup.png"
    ampy put images/png/img_setup.png /images/png/img_setup.png
fi

echo "Uploading images for cloud, internet, no_internet, phone, mobile, usb, wave"

if echo $images | grep -w "img_cloud.png" > /dev/null ; then
    echo "img_cloud.png has already been uploaded"
else
    echo "Uploading img_cloud.png"
    ampy put images/png/img_cloud.png /images/png/img_cloud.png
fi

if echo $images | grep -w "img_internet.png" > /dev/null ; then
    echo "img_internet.png has already been uploaded"
else
    echo "Uploading img_internet.png"
    ampy put images/png/img_internet.png /images/png/img_internet.png
fi

if echo $images | grep -w "img_no_internet.png" > /dev/null ; then
    echo "img_no_internet.png has already been uploaded"
else
    echo "Uploading img_no_internet.png"
    ampy put images/png/img_no_internet.png /images/png/img_no_internet.png
fi

if echo $images | grep -w "img_phone.png" > /dev/null ; then
    echo "img_phone.png has already been uploaded"
else
    echo "Uploading img_phone.png"
    ampy put images/png/img_phone.png /images/png/img_phone.png
fi

if echo $images | grep -w "img_mobile.png" > /dev/null ; then
    echo "img_mobile.png has already been uploaded"
else
    echo "Uploading img_mobile.png"
    ampy put images/png/img_mobile.png /images/png/img_mobile.png
fi

if echo $images | grep -w "img_usb.png" > /dev/null ; then
    echo "img_usb.png has already been uploaded"
else
    echo "Uploading img_usb.png"
    ampy put images/png/img_usb.png /images/png/img_usb.png
fi

if echo $images | grep -w "img_wave.png" > /dev/null ; then
    echo "img_wave.png has already been uploaded"
else
    echo "Uploading img_wave.png"
    ampy put images/png/img_wave.png /images/png/img_wave.png
fi

echo "Uploading images printer2 ready "

if echo $images | grep -w "img_ready.png" > /dev/null ; then
    echo "img_ready.png has already been uploaded"
else
    echo "Uploading img_ready.png"
    ampy put images/png/img_ready.png /images/png/img_ready.png
fi

if echo $images | grep -w "img_printer2.png" > /dev/null ; then
    echo "img_printer2.png has already been uploaded"
else
    echo "Uploading img_printer2.png"
    ampy put images/png/img_printer2.png /images/png/img_printer2.png
fi

echo "Uploading scan_example"

if echo $images | grep -w "scan_example.png" > /dev/null ; then
    echo "scan_example.png has already been uploaded"
else
    echo "Uploading img_scan_example.png"
    ampy put images/png/scan_example.png /images/png/scan_example.png
fi
