# pythonStudy

## やること

- Pythonの基本構文など
- ログ
- スレッド
- UnitTest
- ソース分割
- キュー
- PostgreSQLとの連携
- RESTful


## 入門

 [https://www.atmarkit.co.jp/ait/articles/1904/05/news021.html#simplehelloworld]

ここを実施中  
 [https://www.python.ambitious-engineer.com/archives/40]

 次はここのページ
 [https://www.python.ambitious-engineer.com/archives/323]

後回し
リスト内包表記
[https://www.python.ambitious-engineer.com/archives/154]

 ## メモ

 ### bool型

 複数の論理演算を行う場合、演算子の優先順位は not , and , or の順。
 可読性の観点から括弧をつけル方がよい。

```python
 b = b1 or (b2 and b3)
```

bool型はint型のサブクラスとして定義されているため、int型への変換が可能。

### None

値が存在しない場合は、Noneを使用する。  
CやJavaのnullに相当する。

### タプル

タプルはリストとは異なり、後から値や順序を変更することができないシーケンス  
イミュータブルな性質を持つ。
タプルはリストよりも少し高速に処理が可能。  

### range型

整数を要素とするイミュータブルなシーケンスを作成するオブジェクト。
初期化の際にシーケンスのサイズや値の範囲、スキップ等を指定することができる。

### set

順序は保持せずに、ユニークな値を持つ
frozensetはイミュータブルなsetを生成する

### dictionary型

キーに対して値が設定された表のようなデータ構造のこと。  
日本語では辞書、プログラミング言語によってはハッシュと呼びます。

### for文

dictionary型のvalueだけを取得したい場合は、valuesメソッドを使用する。  
dictionary型のkey,valueを取得したい場合は、itemsメソッドを使用する。

```python
dic = {"key1":110, "key2":222, "key3":333}
for key, value in dic.items():
    print("key = ", key, ", value = ", value)

```

何番目の要素だけは処理しない等の処理を入れたい場合はenumerate関数を使用したループインデックスを利用する。

```python
for i, value in enumerate(l):
    print(i, value)
```