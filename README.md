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
 [https://www.python.ambitious-engineer.com/archives/198]
range型

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
