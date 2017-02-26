#指定した時間が来たらブラウザを開く
簡易的な目覚まし時計の完成です。

```
# -*- coding: utf-8 -*-

import time
import webbrowser
t = time.ctime()

print (t)

#指定の時間までループする
while t != "Sun Feb 26 09:06:00 2017":
    t = time.ctime()

print ("ループ終了")
webbrowser.open('https://www.youtube.com/watch?v=McRmF9ccjUA#t=0m02s')
```
