#!/bin/bash

# 対象文字列
TALKSTR=$1

# 一時保存用ファイル名
TMPWAV=`mktemp`

# 音声ファイルパス。
HTS_ATR503=/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice
MEI_BASHFUL=/usr/share/hts-voice/mei/mei_bashful.htsvoice

# 合成ファイル生成
echo "$1" | open_jtalk \
-m ${MEI_BASHFUL} \
-x /var/lib/mecab/dic/open-jtalk/naist-jdic \
-ow ${TMPWAV}

# 再生
aplay ${TMPWAV}

# 一時ファイル削除
rm -f ${TMPWAV}

exit 0

