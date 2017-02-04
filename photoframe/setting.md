### スクリプトセット
cd ~
git pull origin

### cron設定
#### スクリプト本体
```
crontab -e
```
```
30 6 * * * /home/uwaguchi/raspberrypi/photoframe/photoframe_start.sh
30 7 * * * /home/uwaguchi/raspberrypi/photoframe/photoframe_stop.sh
0 19 * * * /home/uwaguchi/raspberrypi/photoframe/photoframe_start.sh
30 23 * * * /home/uwaguchi/raspberrypi/photoframe/photoframe_stop.sh
```
#### バックライト制御だけはrootで
```
sudo crontab -u root -e
```
```
30 6 * * * /home/uwaguchi/raspberrypi/photoframe/backlight_control.sh 0
30 7 * * * /home/uwaguchi/raspberrypi/photoframe/backlight_control.sh 1
0 19 * * * /home/uwaguchi/raspberrypi/photoframe/backlight_control.sh 0
0 23 * * * /home/uwaguchi/raspberrypi/photoframe/backlight_control.sh 1
```

