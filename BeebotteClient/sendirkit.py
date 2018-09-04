# -*- coding: utf-8 -*-

import os
import requests

# 指定されたファイルの内容をIRKitに投げる
def send(messagefile)
    # 自分自身のディレクトリ
    scriptdir = os.path.dirname(os.path.abspath(__file__))

    # IRKitホスト設定ファイル読み込み
    f = open(scriptdir + "/IRKit.dat")
    # ホスト名取得
    host = f.readline().rstrip("\n")
    # URL生成
    url = "http://" + host + "/messages" 
    # ヘッダ設定
    headers = "X-Requested-With: curl"
    f.close()

    # メッセージ本体
    f.open(scriptdir + "/" + messagefile)
    message = f.readline().rstrip("\n")    

    # リクエスト実行
    response = requests.post(url,data=json.dumps(message), headers=headers) 

    return
