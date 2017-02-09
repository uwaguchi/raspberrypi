#-*- coding:utf-8 -*-
from pyicloud import PyiCloudService
from datetime import datetime
from datetime import date
from datetime import timedelta

# アカウントファイル読み込み
f = open("account.dat")
accounts = f.readlines()

#以下は接続するiCloudのアカウントとパスワードを記載します。
api = PyiCloudService(accounts[0].rstrip("\n"), accounts[1].rstrip("\n"))

# 指定日のイベントデータを取得
def getEventList( targetdate ):
    # 指定日に属するイベントデータを取得 
    eventlist = api.calendar.events(targetdate, targetdate)

    # イベントデータオブジェクトリスト
    retlist = []

    # イベントリストからイベントデータを取得
    for curevent in eventlist:
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


if __name__ == '__main__':

    # 基準日
    #targetdate = date.today()
    #targetdate = datetime(2016,8,31)
    targetdate = datetime(2017,1,20)

    # 明日のイベントリストを取得
    targeteventdata = getEventList( targetdate + timedelta(days=1))

    outstr = ""
    for curevent in targeteventdata:
        if outstr != "":
            outstr += "　あと、"
        outstr += "あしたは"
        outstr += str( curevent["startDate"][4] )
        outstr += "時"
        if curevent["startDate"][5] != 0:
            outstr += str( curevent["startDate"][5] )
            outstr += "分"
        outstr += "から"
        outstr += curevent["title"].encode( "utf-8" )
        outstr += "があるよ！"

    # LINE に飛ばすとか
    print outstr

    # スピーカーでしゃべってもらうとか



