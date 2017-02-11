#-*- coding:utf-8 -*-
from pyicloud import PyiCloudService
from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
import os
import requests

# 自分自身のディレクトリ
scriptdir = os.path.dirname(os.path.abspath(__file__))

# アカウントファイル読み込み
f = open(scriptdir + "/account.dat")
accounts = f.readlines()

# tokenファイル読み込み
f = open(scriptdir + "/token.dat")
token = f.readline().rstrip("\n")

# PyiCloudServec 初期化
api = PyiCloudService(accounts[0].rstrip("\n"), accounts[1].rstrip("\n"))

# 指定日のイベントデータを取得
def getEventList( targetdate ):
    # 指定日に属するイベントデータを取得
    # 前日から指定しないと0:00の予定がとれないぽいのでこうしておく
    eventlist = api.calendar.events(targetdate-timedelta(days=1), targetdate)

    # イベントデータオブジェクトリスト
    retlist = []

    # イベントリストからイベントデータを取得
    for curevent in eventlist:
        # 開始時刻を取得
        curstartdate = datetime( curevent["startDate"][1], curevent["startDate"][2], curevent["startDate"][3] )

        # 指定日のイベントのみ取得対象
        if curstartdate == targetdate:
            # イベントデータオブジェクト
            eventdataobj = {}

            # guid
            eventdataobj["guid"] = curevent["guid"]
            # タイトル
            eventdataobj["title"] = curevent["title"]
            # 開始時刻
            eventdataobj["startDate"] = curevent["startDate"]
            # 終了時刻
            eventdataobj["endDate"] = curevent["endDate"]

            # リストに追加
            retlist.append( eventdataobj )

    # オブジェクトリストを返す
    return retlist

# LINEにメッセージをなげる
def notifyToLINE( message ):
    # URL
    url = "https://notify-api.line.me/api/notify"

    # リクエストヘッダ
    header = { "Authorization": "Bearer " + token } 

    # リクエストパラメータ
    data = { "message": message }

    # リクエスト実行
    res = requests.post( url, data=data, headers=header )

    #print res.text


if __name__ == '__main__':

    # 基準日
    targetdate = datetime.combine( date.today(), time() )
    #targetdate = datetime(2017,1,31)

    # 明日のイベントリストを取得
    targeteventdata = getEventList( targetdate + timedelta(days=1))

    # 取得したデータから文字列組み立て
    outstr = ""
    for curevent in targeteventdata:
        if outstr != "":
            outstr += "　あと、"
        outstr += "あしたは"
        if curevent["startDate"][4] != 0 or curevent["startDate"][4] != curevent["endDate"][4] or curevent["startDate"][5] != curevent["endDate"][5]:
            outstr += str( curevent["startDate"][4] )
            outstr += "時"
            if curevent["startDate"][5] != 0:
                outstr += str( curevent["startDate"][5] )
                outstr += "分"
            outstr += "から"
        outstr += curevent["title"].encode( "utf-8" )
        outstr += "があるよ！"

    # LINE に飛ばしてみる
    if outstr != "":
        notifyToLINE( outstr )

    # スピーカーでしゃべってもらうとか



