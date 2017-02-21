#for文について学ぶ
* * * * *
これからPythonの繰り返し処理の1つであるfor文を学びたいと思います。(For1.py)

```
# -*- coding: utf-8 -*-

print("Hello")
```

このHelloを10行出力するプログラムを作ろうとするとこういったコードになると思います。

```
# -*- coding: utf-8 -*-

print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

では1000行や10000行書く時も同じように記述すればいいでしょうか。同じように記述すると、
時間がかかりますし、タイプミスも増えてしまいます。その時便利なのが繰り返し処理のforです.

```
# -*- coding: utf-8 -*-

for value in range(0,10):
    print("Hello")
```

10のHelloが表示されたと思います

```
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
```

100表示させたい場合はrange(0,100)にします。

```
# -*- coding: utf-8 -*-

for value in range(0,100):
    print("Hello")
```

rangeの0の意味の意味は開始の数、100は繰り返しの数を表しています。結果0から始まり100回繰り返すので
0回~99回繰り返し処理されます。それをprintで確認することが出来ます(For2.py)

```
# -*- coding: utf-8 -*-

for value in range(0,100):
    print(value)
```

もう少し分かりやすくするために文字列を入れてみましょう

```
# -*- coding: utf-8 -*-

for value in range(0,100):
     print(str(value),"回目の処理")
```

#練習
1. for文を使いHelloを24回表示させてください。(For3.py)
2. for文を使い24時間分の時間を表示させてください。(For4.py)
3. for文を使い1+2+3+4+5...+100の計算をしその結果を表示させてください。(For5.py)