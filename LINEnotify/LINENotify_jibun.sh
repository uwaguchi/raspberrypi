#!/bin/bash
# LINE Notifyさんから自分にメッセージを送る
curl -s -X POST -H "Authorization: Bearer `cat /home/uwaguchi/raspberrypi/LINEnotify/token/jibun.token`" -F "message=$1" https://notify-api.line.me/api/notify
