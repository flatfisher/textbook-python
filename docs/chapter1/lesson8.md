#関数について学ぶ
* * * * *
プログラミングの世界には何度も同じ処理を書き直さなくてもいいように、関数という処理を1つにまとめる機能があります。
当然Pythonにもその機能があるので使ってみましょう。(Func1.py)

```
# -*- coding: utf-8 -*-

print("Hello")
print("Japan")
```

こちらの処理を関数にまとめてみます。

```
# -*- coding: utf-8 -*-

def test_func():
    print("Hello")
    print("Japan")

test_func()
```

こちらもif文やfor文同様インデントに注意してください。

##引数を付けてみる
引数を利用すれば引数に応じた処理を作成することができます。(Func2.py)

```
# -*- coding: utf-8 -*-

def sum():
    value = 1 + 1
    print(value)

sum()
```

こちらは1+1の結果を画面表示する関数です。これを引数を利用し任意の数字を足す機能に変更してみます。

```
# -*- coding: utf-8 -*-

def sum(num1,num2):
    value = num1 + num2
    print(value)

sum(2,3)
```

結果

```
5
```

###練習
1. 引き算をする関数を作成してください。(Func3.py)
2. 掛け算をする関数を作成してください。(Func4.py)
3. 割り算をする関数を作成してください。(Func5.py)

####ヒント
* 6 - 2 引き算
* 6 * 2 掛け算
* 6 / 2 割り算

##引数の初期値
引数が指定されなくとも動くように、引数に初期値を設定することができます。(Func6.py)

```
# -*- coding: utf-8 -*-

def show_num(num = 10):
    print(num)

show_num()
```

結果

```
10
```

5を指定すれば5と表示されます。

```
# -*- coding: utf-8 -*-

def show_num(num = 10):
    print(num)

show_num(5)
```

結果

```
5
```

##戻り値を作成する
足し算など結果を任意に使用したい時は結果を戻り値として返します。(Func7.py)

```
# -*- coding: utf-8 -*-

def sum(num1 = 0,num2 = 0):
    val = num1 + num2
    print(val)

sum(2,3)
```

returnを使用し整数型の変数を受取画面出力をしてみます。

```
# -*- coding: utf-8 -*-

def sum(num1 = 0,num2 = 0):
    val = num1 + num2
    return val

total = sum(2,3)
print(total)
```

###練習
1. 引き算をする関数を作成してください。(Func8.py)
2. 掛け算をする関数を作成してください。(Func9.py)
3. 割り算をする関数を作成してください。(Func10.py)
4. 三角形の面積を出す関数を作成してください。(Func11.py)
※全てreturnを使用してください。


##コラム
pythonでは2つの戻り値を作成することができます。受け取る時に2つの変数を用意してください。

```
# -*- coding: utf-8 -*-

def do_calc(num1 = 0,num2 = 0):
    val1 = num1 + num2
    val2 = num1 - num2
    return val1,val2

value1,value2 = do_calc(6,2)
print(value1)
print(value2)
```

結果

```
8
4
```

###練習
1. リストにテストの点数を10こ入れてください。※点数は任意の数字でかまいません (Func12.py)
2. 引数をリストにし合計点をだす関数を作成してください。(Func12.py)
3. 平均点を出す関数を作成してください。(Func12.py)
4. 点数の最大値を出す関数を作成してください。(Func12.py) ※リストの関数は使用しないでください。
5. 最大値のIndexを返す関数を作成してください。(Func12.py) ※リストの関数は使用しないでください。
6. 点数の最小値を出す関数を作成してください。(Func12.py) ※リストの関数は使用しないでください。
7. 最小値のIndexを返す関数を作成してください。(Func12.py) ※リストの関数は使用しないでください。
8. 点数からA~E評価する関数を作成してください。(Func12.py)