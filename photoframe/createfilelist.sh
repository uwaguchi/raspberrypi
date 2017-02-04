#!/bin/bash

find /mnt/share/photo/2006 -type f > filelist.work
find /mnt/share/photo/2007 -type f >> filelist.work
find /mnt/share/photo/2008 -type f >> filelist.work
find /mnt/share/photo/2009 -type f >> filelist.work
find /mnt/share/photo/201* -type f >> filelist.work
find /mnt/share/Eye-Fi -type f >> filelist.work
perl -lne 'print if /JPG$|jpg$/' filelist.work > filelist.txt
rm -f filelist.work
