# -*- coding: utf-8 -*-

import os
import json
import requests

# 指定されたファイルの内容をIRKitに投げる
def send(messagefile):
    # 自分自身のディレクトリ
    scriptdir = os.path.dirname(os.path.abspath(__file__))

    # IRKitホスト設定ファイル読み込み
    try:
        with open(scriptdir + "/IRKit_host.dat") as fh:
            # ホスト名取得
            host = fh.readline().rstrip("\n")
            # URL生成
            url = "http://" + host + "/messages" 
            # ヘッダ設定
            headers = {"X-Requested-With": "curl"}
    except:
        print("IRKit_host.dat read error.")
        return False

    # メッセージbodyファイル読み込み
    try:
        with open(scriptdir + "/" + messagefile) as fm:
            message = fm.readline().rstrip("\n")
    except:
        print(messagefile + " read error.")
        return False

    # リクエスト実行
    response = requests.post(url,data=message, headers=headers) 

    print(response)
    return True
