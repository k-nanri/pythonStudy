# pythonStudy

## やること

- スレッド
  [https://docs.python.org/ja/3/library/threading.html]

- キュー
  [https://docs.python.org/ja/3/library/queue.html]
  [https://docs.python.org/ja/3/library/queue.html]

- PostgreSQLとの連携
  [https://www.ashisuto.co.jp/db_blog/article/20160308_postgresql_with_python.html]
  [https://www.utakata.work/entry/20190410/1554849000]

- RESTful
 - flask 
   [https://qiita.com/Morinikiz/items/c2af4ffa180856d1bf30]
   [https://qiita.com/zaburo/items/5091041a5afb2a7dffc8]

 - django
   [https://docs.djangoproject.com/ja/3.2/]
   [https://qiita.com/kaki_k/items/511611cadac1d0c69c54]

 - OpenPyXL
   - セルからの値取得
   - セルへの値の設定
   - 表の作成
   - グラフの作成
   - vmstatとかの結果をグラフにする

## やったこと

- Pythonの基本構文など
- ログ
- UnitTest
- ソース分割


## 入門

 [https://www.atmarkit.co.jp/ait/articles/1904/05/news021.html#simplehelloworld]

## 応用編

[https://www.python.ambitious-engineer.com/application]

 次はここのページ
 [https://www.python.ambitious-engineer.com/archives/1185]
 

後回し
リスト内包表記
[https://www.python.ambitious-engineer.com/archives/154]
クラスデコレータ
[https://www.python.ambitious-engineer.com/archives/348]
基本的な特殊メソッドと_str_
オブジェクト同士の演算
変数の型を判定するその2type関数
文字列の種別判定と数値変換
文字列のフォーマット（値の埋め込み）
正規表現



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

### Pythoneにはプライベート変数はない

プライベート変数はないが、アンダースコア２つで始まり、末尾がアンダースコア１つ以下となる変数名の場合、その変数に対する外部からアクセスするとAttributeErrorを発生させることができる。

### プロパティ

専用のアクセス用メソッドを経由して処理を行うためにプロパティと呼ばれる組み込みデコレータがある。

| プロパティ | 機能 |
| --------- | ---- |
| @property | getter |
| @属性名.setter | setter |
| @属性名.deleter | deleter |

### with文でclose漏れを防ぐ

```python
with open('ファイルパス','モード') as 変数名:
    処理
```

途中で例外が発生しても、close処理が自動的に呼び出される

### パッケージ化

モジュールが増えた場合はパッケージディレクトリで分けて管理したほうがよい。  
その際は、__init__.pyでまとめて定義することで使用する側でimport文をたくさん書く必要がなくなる。

[https://www.python.ambitious-engineer.com/archives/429]

### うまくテスト対象が認識されない

手順通りに設定してみたが、うまくテストスイートが実行できなかった。
unittest 単体テスト入門 その2 テストパッケージとテストスイート
[https://www.python.ambitious-engineer.com/archives/841]