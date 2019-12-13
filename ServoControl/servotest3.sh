#!/bin/bash

# Usage: ./servotest3.sh 18 150

# GPIOピン番号
PIN=$1

# DUTY値
# -90度：60
# 0度：150
# 90度：250
DUTY=$2

# 設定(SG90)
gpio -g mode ${PIN} pwm
gpio pwm-ms
gpio pwmc 192
gpio pwmr 2000

# 実行
gpio -g pwm ${PIN} ${DUTY}

exit 0
