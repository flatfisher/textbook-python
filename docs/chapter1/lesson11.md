#ディクショナリを使ってみる
ディクショナリはキー(Key)とバリュー(Value)の１セットで１つの要素を持つことが出来る機能です。(Dict1.py)

```
test_dict = {'YEAR':'2017', 'MONTH':'2', 'DAY':'26'}

print(test_dict)
```

KeyでValueを取得してみる

```
test_dict = {'YEAR':'2017', 'MONTH':'2', 'DAY':'26'}

print(test_dict.get('YEAR'))
print(test_dict.get('MONTH'))
print(test_dict.get('DAY'))
```

要素の追加

```
test_dict = {}

test_dict['YEAR']  = '1991'
test_dict['MONTH'] = '04'
test_dict['DAY']   = '19'

print(test_dict)
```

要素の削除

```
test_dict = {}

test_dict['YEAR']  = '1991'
test_dict['MONTH'] = '04'
test_dict['DAY']   = '19'

del test_dict['DAY']
```

##練習
自分のプロフィールをディクショナリを使って保存してみよう