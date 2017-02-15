#コメントアウトしてみる
* * * * *
プログラミングにはコメントアウトというものがあります。コメントは実際にプログラムを実行するときには無視されます。
誰が呼んでも分かるコードになるようコメントを記述することがよくあるのでここで覚えておきましょう。
必要ファイルを準備しましょう。


```
python 
    - project
        - chapter1
            - Comment.py
```

2行の文字列を表示するプログラムを書いてみる

```
print("Hello ")
print("World!")
```

結果

```
Hello 
World!
```

ではコメントを入れてみましょう。Pythonではコマンドが ```#```となります

```
# Hello World と表示
print("Hello ")
print("World!")
```

日本語記述でエラーが起きた人は```# -*- coding: utf-8 -*-```をコードの一番上に記述します。

```
# -*- coding: utf-8 -*-
# Hello World と表示
print("Hello ")
print("World!")
```

結果

```
Hello 
World!
```

無事表示されれば成功です。