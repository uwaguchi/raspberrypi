#!/bin/bash

# 対象ファイルリスト
TARGET=/home/uwaguchi/raspberrypi/photoframe/filelist.txt

# feh起動
DISPLAY=:0.0 feh -D 10 -z -Y -q -F --draw-filename --draw-tinted -f ${TARGET}
