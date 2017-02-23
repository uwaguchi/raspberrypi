#!/bin/bash

# ホスト名設定ファイル
HOST=`cat $1`

# postするJSON
MESSAGE=`cat $2`

# 信号を送信
curl "http://${HOST}/messages" -H "X-Requested-With: curl" -d "${MESSAGE}"

