import pandas as pd

# Series
# 1次元データ構造
s = [1, 2, 3, 4, 5]
index = ["a", "b", "c", "d", "e"]
series = pd.Series(s, index=index)
print(series)

# DataFrame
# 2次元データ構造
data = [
    ["tanaka", 20, "female", 1, 600],
    ["suzuki", 30, "male", 8, 492],
    ["tanaka", 23, "male", 3, 890],
    ["sato", 28, "male", 4, 833],
    ["takano", None, "male", 20, 234],
]
column = ["name", "age", "m/f", "y of experience", "score"]
index = ["0001", "0002", "0003", "0004", "0005"]
df = pd.DataFrame(data=data, columns=column, index=index)
print(df)

# 特定の列を取得
print("ageカラムを取得")
print(df["age"])

# 特定の行を取得
print("3行目を取得")
print(df[2:3])

# 特定の列と行を取得
print("locを使用")
print(df.loc["0003":"0005", "age":"m/f"])
print(df.loc["0004":"0006"])

# 特定の列と行を取得
print("ilocを使用")
print(df.iloc[2:4, 1:3])
print(df.iloc[3:6])

# 先頭と末尾を取得
print("= 先頭 ==========")
print(df.head(2))

print("= 末尾 ==========")
print(df.tail(2))

# 条件指定
print("== ageが30より小さい行を取得 ======")
print(df.query("age < 30"))
print("== nameがtanakaの行を取得 ======")
print(df.query("name == 'tanaka'"))
print("== nameがtanakaかつageが23の行を取得 ======")
print(df.query("name == 'tanaka' and age == 23"))


data = [["tanaka", 20, "female", 1, 600], ["suzuki", 20, "male", 8, 492]]
column = ["name", "age", "m/f", "y of experience", "score"]
df = pd.DataFrame(data=data, columns=column)
print("== 追加前 ================")
print(df)
print("== 列を追加1 ==============")
df["like"] = ["movie", "cook"]
print(df)
print("== 列を追加2 ==============")
df = df.assign(food=["sushi", "apple"])
print(df)
print("== 行を追加1 ==============")
df.loc[2] = ["yamada", 40, "male", 20, 500, "cycle", "beaf"]
print(df)

print(df["age"].value_counts())
