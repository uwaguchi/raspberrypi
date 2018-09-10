# -*- coding: utf-8 -*-

import os
import json
import paho.mqtt.client as mqtt
import datetime

import sendirkit

# トピック
g_topic = ""

# 接続時の処理
def on_connect(client, userdata, flags, rc):
    print(datetime.datetime.now().strftime("[%Y/%m/%d %H:%M:%S] ") + "connected. result code: " + str(rc))
    # 保存したトピックをsubscribe
    client.subscribe(g_topic)

# メッセージ受信時の処理
def on_message(client, userdata, msg):
    print(datetime.datetime.now().strftime("[%Y/%m/%d %H:%M:%S] ") + "received message. topic: " + msg.topic + ", payload: " + str(msg.payload))

    # payloadのdata要素を取得
    data = json.loads(msg.payload)["data"]
    print(data)

    # ファイル名にしてIRkitにリクエスト送信
    if sendirkit.send(data + ".json") == True:
        print(datetime.datetime.now().strftime("[%Y/%m/%d %H:%M:%S] ") + "request OK.")
    else:
        print(datetime.datetime.now().strftime("[%Y/%m/%d %H:%M:%S] ") + "request Error.")
    return

# メイン
if __name__ == '__main__':

    # 自分自身のディレクトリ
    scriptdir = os.path.dirname(os.path.abspath(__file__))

    # 設定ファイル読み込み
    f = open(scriptdir + "/config.json")
    conf = json.load(f)

    # トピックをグローバル変数に保存
    g_topic = conf["topic"]

    # Beebotte MQTT ブローカーに接続
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set('token:%s' % conf["token"])
    client.tls_set(conf["cacert"])
    client.connect(conf["host"], int(conf["port"]))
    client.loop_forever()

