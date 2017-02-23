#!/bin/bash

# ホスト名設定ファイル
HOST=`cat $1`

# 直前に受信した信号を返す
curl "http://${HOST}/messages" -H "X-Requested-With: curl" 

