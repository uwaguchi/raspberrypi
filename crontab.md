### crontab
crontabはこんな感じ
```
0 5 * * * /home/uwaguchi/raspberrypi/photoframe/createfilelist.sh
30 6 * * * /home/uwaguchi/raspberrypi/photoframe/photoframe_start.sh
30 7 * * * /home/uwaguchi/raspberrypi/photoframe/photoframe_stop.sh
0 19 * * * /home/uwaguchi/raspberrypi/photoframe/photoframe_start.sh
0 23 * * * /home/uwaguchi/raspberrypi/photoframe/photoframe_stop.sh

0 21 * * * perl /home/uwaguchi/raspberrypi/chirashiChecker/chirashiChecker.pl
#0 22 * * * python /home/uwaguchi/raspberrypi/scheduleNotifier/scheduleNotifier.py

@reboot python -u /home/uwaguchi/raspberrypi/BeebotteClient/BeebotteClient.py > /home/uwaguchi/raspberrypi/BeebotteClient/BeebotteClient.log 2>&1
```
```
30 6 * * * /home/uwaguchi/raspberrypi/photoframe/backlight_control.sh 0
30 7 * * * /home/uwaguchi/raspberrypi/photoframe/backlight_control.sh 1
0 19 * * * /home/uwaguchi/raspberrypi/photoframe/backlight_control.sh 0
0 23 * * * /home/uwaguchi/raspberrypi/photoframe/backlight_control.sh 1
```
