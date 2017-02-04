#!/bin/bash

# ディスプレイON
#echo 0 > /sys/class/backlight/rpi_backlight/bl_power

# 対象ファイル
TARGET=/mnt/share/photo/2017/*/*.JPG

# feh起動
DISPLAY=:0.0 feh -D 10 -z -Y -F ${TARGET}
