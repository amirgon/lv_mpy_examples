#!/bin/sh
echo "Copying all argb8888 binary files"
cp * ../argb8888_bin/* .
echo "converting all argb8888 image files to png"
argb8888_to_png icon_bright_29x29_argb8888.bin 29 29
argb8888_to_png icon_eco_38x34_argb8888.bin 38 34
argb8888_to_png icon_hue_23x23_argb8888.bin 23 23
argb8888_to_png icon_pc_41x33_argb8888.bin 41 43
argb8888_to_png icon_tel_35x35_argb8888.bin 35 35
argb8888_to_png icon_wifi_48x34_argb8888.bin 48 34
argb8888_to_png img_btn_bg_1_174x215_argb8888.bin 174 215
argb8888_to_png img_btn_bg_2_174x215_argb8888.bin 174 215
argb8888_to_png img_btn_bg_3_174x215_argb8888.bin 174 215
argb8888_to_png img_btn_bg_4_174x215_argb8888.bin 174 215
argb8888_to_png img_cloud_93x59_argb8888.bin 93 59
argb8888_to_png img_copy_51x60_argb8888.bin 51 60
argb8888_to_png img_internet_65x64_argb8888.bin 65 64
argb8888_to_png img_mobile_50x60_argb8888.bin 50 60
argb8888_to_png img_no_internet_42x42_argb8888.bin 42 42
argb8888_to_png img_phone_77x99_argb8888.bin 77 99
argb8888_to_png img_print_65x64_argb8888.bin 65 64
argb8888_to_png img_printer2_107x104_argb8888.bin 107 104
argb8888_to_png img_ready_158x158_argb8888.bin 158 158
argb8888_to_png img_scan_51x61_argb8888.bin 51 61
argb8888_to_png img_setup_63x64_argb8888.bin 63 64
argb8888_to_png img_usb_62x61_argb8888.bin 62 61
argb8888_to_png img_wave_27x47_argb8888.bin 27 47
argb8888_to_png scan_example_522x340_argb8888.bin 522 340
echo "removing the argb8888 binary files again"
rm *.bin
echo "adapting the file names"
for filename in *.png; do
    new_filename=$(echo $filename | sed s/_argb8888//)
    mv $filename $new_filename
done
