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
]
column = ["name", "age", "m/f", "y of experience", "score"]
df = pd.DataFrame(data=data, columns=column)
print(df)

# 特定の列を取得
