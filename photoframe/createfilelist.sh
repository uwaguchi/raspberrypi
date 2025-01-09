#!/bin/bash

FILELISTPATH=/home/uwaguchi/raspberrypi/photoframe

find /mnt/share/photo/2006 -type d -name  '.*' -prune -or -not -name '.*' > ${FILELISTPATH}/filelist.work
find /mnt/share/photo/2007 -type d -name  '.*' -prune -or -not -name '.*' >> ${FILELISTPATH}/filelist.work
find /mnt/share/photo/2008 -type d -name  '.*' -prune -or -not -name '.*' >> ${FILELISTPATH}/filelist.work
find /mnt/share/photo/2009 -type d -name  '.*' -prune -or -not -name '.*' >> ${FILELISTPATH}/filelist.work
find /mnt/share/photo/201* -type d -name  '.*' -prune -or -not -name '.*' >> ${FILELISTPATH}/filelist.work
find /mnt/share/photo/202* -type d -name  '.*' -prune -or -not -name '.*' >> ${FILELISTPATH}/filelist.work
find /mnt/share/Eye-Fi -type d -name  '.*' -prune -or -not -name '.*' >> ${FILELISTPATH}/filelist.work
perl -lne 'print if /JPG$|jpg$/' ${FILELISTPATH}/filelist.work > ${FILELISTPATH}/filelist.txt
rm -f ${FILELISTPATH}/filelist.work
