#if文を学ぶ
* * * * * 
ここではif文という条件分岐を学びます。if1.pyというファイルを準備し、そこにコードを書いてください。
またこれからは必要ファイルを(if1.py)や(if2.py)というように記述するので、その都度ファイルを新規で作成してください。


```
# -*- coding: utf-8 -*-

value = 1

if value == 1:
    print("value is 1")
else: 
    print("value is not 1")
```

このような形で条件分岐をすることができます。Pythonは{}が無い代わりに":"やindent(空行や余白)などで{}を表現するので
スペースの数や":"に気をつけてください。(if2.py)


```
# -*- coding: utf-8 -*-

value = 2

if value == 1:
    print("value is 1")
elif value == 2:
    print("value is 2")
else: 
    print("value is not 1 or 2")
```

elifを使えば条件式を追加することができます。また2つ以上の条件が揃った時の処理は以下のように記述します(if3.py)

```
# -*- coding: utf-8 -*-
value = 1
value2 = 2

if value == 1 and value2 == 2:
    #両方の条件が揃ったとき
    print("value is 1 , value2 is 2.")
else:
    print("value is not 1 or value2 is not 2.")
```

2つのうち1つの条件が揃ったときを比較するには以下のように表現します。(if4.py)

```
# -*- coding: utf-8 -*-
value = 1
value2 = 4

if value == 1 or value2 == 2:
    #いずれかの条件が揃ったとき
    print("value is 1 or value2 is 2.")
else:
    print("value is not 1 or value2 is not 2.")
```

前述したとおりPythonでは空白や空行をつかってクラスや関数の場所を判断しているため空行の処理をいれることができません。
例えば以下のようなif分は文法エラーになります。(if5.py)

```
# -*- coding: utf-8 -*-
value = 1

if value == 1:
    print("value is 1")
else:
    #何も書かない
```

これを実行しようとするとエラーが発生しプログラムを実行することが出来ません。何も処理を書かない場合はpassとだけ書いておきましょう。
passを使えばこのようなエラー回避することができます。(if6.py)

```
# -*- coding: utf-8 -*-
value = 1

if value == 1:
    print("value is 1")
else:
    #passを入れる
    pass
```

数字だけではなく文字列の比較も出来ます。(if7.py)

```
# -*- coding: utf-8 -*-
 
value_str_1 = "Python"
value_str_2 = "World"

if value_str_1 == "Python":
    pass
elif value_str_1 == "Python" and value_str_2 == "World":
    print("2つの条件が一致")
elif value_str_1 == "IZM" or value_str_2 == "PYTHON":
    print("いずれかの条件が一致")
```

###練習
if文の練習をしましょう。

1. 整数の変数を用意し、1であれば1、2であれば2、それ以外であれば0が表示されるプログラムを作ってください(if8.py)
2. 整数の変数を用意し、40未満であればE,40以上であればD,50以上であればC,70以上であればB,80以上であればAと表示されるプログラムを作ってください(if9.py)
3. 変数(val_1)と変数(val_2)を用意し、任意の数を入れてください。val_1とval_2が30以上かつval_1とval_2の合計が130以上であれば1それ以外であれば2と表示されるプログラムを作ってください(if10.py)
4. 変数(val_1)と変数(val_2)を用意し、任意の数を入れてください。val_1とval_2が90以上であれば1それ以外であれば2と表示されるプログラムを作ってください(if11.py)
5. 文字列の変数を用意し、文字列がJapanであればJapanと表示されるプログラムを作ってください。条件が当てはまらない場合はpassを使って処理を飛ばしてください。(id12.py)