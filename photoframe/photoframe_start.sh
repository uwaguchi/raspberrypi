#!/bin/bash

# 対象ファイルリスト
TARGET=filelist.txt

# feh起動
DISPLAY=:0.0 feh -D 10 -z -Y -q -F -f ${TARGET}
