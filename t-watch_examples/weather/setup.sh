#!/usr/bin/bash
# This shell scripts sets up the t-watch weather application
# It uploads the weather icons to the esp32 into the "images" folder
# Demo program for the course on the Internet of Things (IoT) at the
# University of Cape Coast (Ghana)
# Copyright (c) U. Raich April 2020
# This program is released under the MIT license
echo "Setting up the file system for the t-watch program"
dirs="$(ampy ls)"
echo $dirs
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
#
# check if images have already been uploaded, upload them if not
#
echo "upoading the weather app icons"
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
echo "All icons are uploaded"
