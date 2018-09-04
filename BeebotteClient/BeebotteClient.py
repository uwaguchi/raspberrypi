# -*- coding: utf-8 -*-

import os
import json
import paho.mqtt.client as mqtt

# 接続時の処理
def on_connect(client, userdata, flags, rc):
    print("connected. result code: " + str(rc))

# メッセージ受信時の処理
def on_message(client, userdata, msg):
    print("received message. topic: " + msg.topic + ", payload: " + str(msg.payload))

# メイン
if __name__ == '__main__':
    # 自分自身のディレクトリ
    scriptdir = os.path.dirname(os.path.abspath(__file__))

    # 設定ファイル読み込み
    f = open(scriptdir + "/config.json")
    conf = json.load(f)

    # Beebotte MQTT ブローカーに接続
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set('token:%s' % conf["token"])
    client.tls_set(conf["cacert"])
    client.connect(conf["host"], int(conf["port"]))
    client.subscribe(conf["topic"])
    client.loop_forever()

