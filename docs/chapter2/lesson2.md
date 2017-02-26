#簡易的なアラームを作ってみる
指定の時間に来ていなかったらずっとループをする処理を書き、
ループが終わったところで"アラーム終了"と表示する。

```
# -*- coding: utf-8 -*-

import time
t = time.ctime()

print (t)

#指定の時間までループする
while t != "Sun Feb 26 08:55:26 2017":
    t = time.ctime()

print ("ループ終了")
```

