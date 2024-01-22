from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker

# DBエンジンを作成
engine = create_engine("postgresql://postgres:example@localhost:5432/postgres")

# モデルベースクラスを作成
Base = declarative_base()

# モデルベースを拡張して、ORMのデータクラスを作成
class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    age = Column(Integer)

    def full_name(self):
        return "{self.first_name} {self.last_name}"

# テーブルをDBに作成
Base.metadata.create_all(engine)

# セッションを作成
# セッションを介してクエリを実行する
SessionClass = sessionmaker(engine)
session = SessionClass()

user_a = User(first_name="tanaka", last_name="hoge", age=30)
session.add(user_a)
session.commit()

users = session.query(User).all()
print(users[0].first_name)


# https://qiita.com/arkuchy/items/75799665acd09520bed2