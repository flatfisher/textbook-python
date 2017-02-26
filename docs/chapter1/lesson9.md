#クラスについて学ぶ
* * * * *
ここではクラスについて学びます。クラスでは新しいオブジェクトを作成したり、関連する複数の関数（処理）などを
まとめておくことができる機能です。クラスを使いこなすことができれば、他人が作成したクラスを利用しさらに高度な
プログラムを作ることが出来ます。

##クラスの作成
簡単なクラスを作成してみます。classと記述し、後にクラス名が続きます。クラス名の後には必ず:を付けましょう。(LearnClass1.py)

```
# -*- coding: utf-8 -*- 

class Person:

    def __init__(self, gender, age):
        self.gender = gender
        self.age = age
```

こちらの関数(def __init_(self, gender, age):)は初期を設定する特別な関数です。
Personクラスにデータを格納し取り出すところまで書いてみます。

```
# -*- coding: utf-8 -*- 

class Person:

    def __init__(self, gender, age):
        self.gender = gender
        self.age = age


person1 = Person('female',20)
person2 = Person('male',21)

print(person1)
print(person2)
```

格納している変数を取り出す時はこのように書きます。

```
# -*- coding: utf-8 -*- 

class Person:

    def __init__(self, gender, age):
        self.gender = gender
        self.age = age


person1 = Person('female',20)
person2 = Person('male',21)

print(person1)
print(person2)

print(person1.gender)
print(person1.age)

print(person2.gender))
print(person2.age)
```

##クラスの継承
Prefectureという県を表すクラスを作成し、それからそのクラスを継承しさらに別なクラスを作成してみます。(LearnClass2.py)

```
# -*- coding: utf-8 -*- 

class Prefecture:

    def __init__(self, pref_name):
        self.pref_name = pref_name


class City(Prefecture):

    def __init__(self, pref_name, city_name):
        Prefecture.__init__(self, pref_name)
        self.city_name = city_name

city = City('Miyagi','Ishinomaki')
print(city.pref_name )
print(city.city_name)
```

##なぜクラス分けする？
プログラミングをしていると何度も使用する処理などがでてきたり、共通の項目を備えなければならないものが出てきたりします。
そのような処理や項目をクラスとしてまとめておけば、後から管理しやすくなったり、ライブラリとして世界中に配布することができます。
例えばスポーツカーでも普通の乗用車でも基本的にアクセルやブレーキが搭載している車ということに変わりはありません。
多種の車をを作成する際に毎回同じ項目を作成するのは非効率です。
その場合車という抽象的なクラスを作成し、車を継承し新たにスポーツカークラスを作成すれば、新たに追加されるスポーツカークラスの項目を
考えるだけで基本的な項目をまた新しく作成するといった手間を省くことが出来ます。

##練習
1. 氏名と性別と年齢を格納出来るPersonクラスを作成してください(LearnClass3.py)
2. Personクラスを継承したStudentというクラスを作成してください。(LearnClass3.py)
3. Studentに学校名を格納する機能を作ってください。(LearnClass3.py)
4. 全ての項目を画面出力してください。(LearnClass3.py)

##クラスに関数を追加しよう
クラスは単に変数をまとめるだけではなく関数をもつことができます。

```
# -*- coding: utf-8 -*- 

class Prefecture:

    def __init__(self, pref_name):
        self.pref_name = pref_name


class City(Prefecture):

    def __init__(self, pref_name, city_name):
        Prefecture.__init__(self, pref_name)
        self.city_name = city_name

    def show_name(self):
        print(self.city_name)

city = City('Miyagi','Ishinomaki')
city.show_name()
```

##練習
* 先ほど作成したStudentクラスに格納している全ての情報を画面出力する関数を作成してください。(LearnClass3.py)

##練習
小売店で販売されている商品をクラスにしてみましょう。

1. 最も抽象的なクラス商品クラスを作成しましょう(クラス名:Merchandise)
2. Merchandiseクラスに商品名と値段を登録する関数を用意しよう
3. Merchandiseクラスを継承しBookクラスを作成しよう
4. Bookクラスに新たにページ数や出版社など本クラスに必要そうな変数や関数を用意しよう
5. Merchandiseクラスを継承しFoodクラスを作成しよう
6. Foodクラスに必要そうな変数や関数を用意しよう
7. 好きな商品を自分で作成してみよう