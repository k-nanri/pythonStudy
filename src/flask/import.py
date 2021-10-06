# -*- coding: utf-8 -*-
import peewee

# データベース指定
db = peewee.SqliteDatabase("src/flask/data.db")

# ユーザモデルを定義
class User(peewee.Model):
    userId = peewee.TextField()
    userCompany = peewee.TextField()
    userDiscountRate = peewee.IntegerField()

    class Meta:
        database = db

# ユーザテーブルを作成
User.create_table()

# tsvファイルを１行ずつ読み込んでタブで分割し、データを登録
for line in open("src/flask/user.tsv", "r"):
    (userId, userCompany, userDiscountRate) = tuple(line[:-1].split(" "))
    if userDiscountRate.isdigit():
        User.create(userId = userId,
                    userCompany = userCompany,
                    userDiscountRate = int(userDiscountRate))