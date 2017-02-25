#リストについて学ぶ
* * * * *
プログラミングの世界では同じような要素を1つの変数のようにまとめておく、配列と呼ばれる
機能があります。例えば以下のようなものです。

```
int[] results = new int[3];
results[0] = 0;
results[1] = 1;
results[2] = 2;

System.out.print(results[2]);

//結果
//2
```

Pythonの世界にも配列がありますが、大きく分けてタプル（tuple）、リスト（list）、
ディクショナリ・辞書（dict）、セット・集合（set）の4つがあります。
今回は配列の1つであるリストについて紹介したいと思います。 (List1.py)

```
# -*- coding: utf-8 -*-

print("Hello")
```

##リストの作成
文字列を格納するlistを作成してみます。

```
# -*- coding: utf-8 -*-

# 文字列のリストを用意
tohoku_list = ['Aomori','Akita','Iwate','Yamagata','Miyagi','Fukushima']
```

リストは0から5番地の6つの値が格納されています。0番地目のAomoriを取得するには以下のように書きます。

```
# -*- coding: utf-8 -*-

# 文字列のリストを用意
tohoku_list = ['Aomori','Akita','Iwate','Yamagata','Miyagi','Fukushima']

#Aomoriを文字列の変数として取得
pref = tohoku_list[0]
```

Aomoriを画面出力してみます。直接出力してもいいですし、分かりやすいようにいったん変数に代入するのもありです。

```
# -*- coding: utf-8 -*-

# 文字列のリストを用意
tohoku_list = ['Aomori','Akita','Iwate','Yamagata','Miyagi','Fukushima']

#Aomoriを文字列の変数として取得
pref = tohoku_list[0]

#Aomoriを変数に入れてから画面出力
print(pref)

#Aomoriを直接リストから画面出力
print(tohoku_list[0])
```

##練習
1. Akitaを画面出力してみよう(List2.py)
1. Iwateを画面出力してみよう(List3.py)
1. Yamagataを画面出力してみよう(List4.py)
1. Miyagiを画面出力してみよう(List5.py)
1. Fukushimaを画面出力してみよう(List6.py)

リストはindex(番号)で取得できるのでfor文で0から5に変わる変数iを用意し、リストの中身を取得するのが楽です。(List7.py)

```
# -*- coding: utf-8 -*-

# 文字列のリストを用意
tohoku_list = ['Aomori','Akita','Iwate','Yamagata','Miyagi','Fukushima']

#Listの中身を全て画面表示

for i in range(0,6):
    print(tohoku_list[i])
```

##練習
1. if文を活用し偶数の時だけリストの中身を出すプログラムを作成してください(List8.py)
3. if文を活用し奇数の時だけリストの中身を出すプログラムを作成してください(List9.py)

##リストに要素の追加
最初に空のリストを作成しあとから要素を追加することができます。appendをすると末尾indexに値が保存されます。(List10.py)

```
# -*- coding: utf-8 -*-

# 文字列のリストを用意
tohoku_list = []

#文字列を追加
tohoku_list.append('Aomori')
tohoku_list.append('Akita')
tohoku_list.append('Iwate')
tohoku_list.append('Yamagata')
tohoku_list.append('Miyagi')
tohoku_list.append('Fukushima')

#Listの中身を全て画面表示

for i in range(0,6):
    print(tohoku_list[i])
```

indexを指定し要素を追加することも出来ます。(List11.py)

```
# -*- coding: utf-8 -*-

# 文字列のリストを用意
tohoku_list = []

#文字列を追加
tohoku_list.insert(0,'Aomori')
tohoku_list.insert(1,'Akita')
tohoku_list.insert(2,'Iwate')
tohoku_list.insert(3,'Yamagata')
tohoku_list.insert(4,'Miyagi')
tohoku_list.insert(5,'Fukushima')

#Listの中身を全て画面表示

for i in range(0,6):
    print(tohoku_list[i])
```

##リストの要素を削除
リストに格納されている値を削除してみます。直接値を指定し削除を行います。
最初に発見された値が削除されるだけなので、複数同じ値がある場合は注意が必要です。(List12.py)

```
# -*- coding: utf-8 -*-

# 文字列のリストを用意
tohoku_list = ['Aomori','Akita','Iwate','Yamagata','Miyagi','Fukushima']

#Aomoriを削除
tohoku_list.remove('Aomori')

for i in range(0,5):
    print(tohoku_list[i])
```

indexを指定し削除を行います。(List13.py)もしindexを指定しない場合は末尾の値が削除されます。

```
# -*- coding: utf-8 -*-

# 文字列のリストを用意
tohoku_list = ['Aomori','Akita','Iwate','Yamagata','Miyagi','Fukushima']

#1番地を削除 Akita
tohoku_list.pop(1)

#末尾をを削除 Fukushima
tohoku_list.pop()

for i in range(0,4):
    print(tohoku_list[i])
```

##indexを調べる
値を指定し格納されているindexを調べることができます。(List14.py)
こちらも最初に取得されたindexのみを返すので

```
# -*- coding: utf-8 -*-

# 文字列のリストを用意
tohoku_list = ['Aomori','Akita','Iwate','Yamagata','Miyagi','Fukushima']

#Akitaの番地を取得
print(tohoku_list.index('Akita'))
```

##リストに格納されている特定の値の数を調べる
リストに特定の値がいくつ格納されているか調べることができます。(List15.py)

```
# -*- coding: utf-8 -*-

# 文字列のリストを用意
tohoku_list = ['Aomori','Aomori','Akita','Iwate','Yamagata','Miyagi','Fukushima']

#要素数を取得
print(tohoku_list.count('Aomori'))
```

##リストに格納されている値の数を調べる
リストに値がいくつ格納されているか調べることができます。(List16.py)

```
# -*- coding: utf-8 -*-

# 文字列のリストを用意
tohoku_list = ['Aomori','Akita','Iwate','Yamagata','Miyagi','Fukushima']

#要素数を取得
print(len(tohoku_list))
```

この要素数を利用し繰り返し処理を行えばリストに格納されている値の範囲内でループさせることができます。(List17.py)

```
# -*- coding: utf-8 -*-

# 文字列のリストを用意
tohoku_list = ['Aomori','Akita','Iwate','Yamagata','Miyagi','Fukushima']

#リスト内の値を表示
length = len(tohoku_list)

for i in range(0,length):
    print(tohoku_list[i])
```

しかしこのように長さを取得しなくともPythonでは以下のようにfor文に直接リストしていすることで
ループを実現することができます。(List18.py)

```
# -*- coding: utf-8 -*-

# 文字列のリストを用意
tohoku_list = ['Aomori','Akita','Iwate','Yamagata','Miyagi','Fukushima']

for pref in tohoku_list:
    print(pref)
```

indexを指定したい場合は以下のようにenumerateを使用すると実現できます(List19.py)

```
# -*- coding: utf-8 -*-

# 文字列のリストを用意
tohoku_list = ['Aomori','Akita','Iwate','Yamagata','Miyagi','Fukushima']

for (i, value) in enumerate(tohoku_list):
    # index指定
    print(tohoku_list[i])
    # value指定
    print(value)
```

##練習
1. 好きな地方の都道府県のリストを作成してください。(List19.py)
2. 全ての都道府県を画面出力してください。(List20.py)
3. indexが偶数の都道府県を画面出力してください。(List21.py)
4. indexが奇数の都道府県を画面出力してください。(List22.py)
5. 特定の県を追加してください。(List23.py)
6. 特定の県を削除してください。(List24.py)
7. リストに5つの点数を格納してください。（List25.py）
8. 5つの点数の合計点をだしてください。※for文,len(),を使ってください。（List25.py）
9. 5つの点数の平均点をだしてください。※for文,len(),を使ってください。（List25.py）