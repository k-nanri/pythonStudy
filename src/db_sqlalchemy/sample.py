from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, ForeignKey

# モデルベースクラスを作成
#Base = declarative_base() と同等(2.0から)
class Base(DeclarativeBase):
    pass

# モデルベースを拡張して、ORMのデータクラスを作成
# mapped_columnは2.0からの新機能
class Manufacturer(Base):
    __tablename__ = "manufacturer"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    address: Mapped[str] = mapped_column(String(1024), nullable=False)

class Product(Base):
    __tablename__ = "product"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    cost: Mapped[int] = mapped_column(Integer, nullable=False)
    manufacturer_id: Mapped[int] = mapped_column(ForeignKey("manufacturer.id"))
   

# DBエンジンを作成
url = "postgresql://postgres:example@localhost:5432/postgres"
engine = create_engine(url, echo=True)

# テーブルをDBに作成
Base.metadata.create_all(engine)

# セッションを作成
# セッションを介してクエリを実行する
SessionClass = sessionmaker(engine)
session = SessionClass()

# Insert
manufacturer1 = Manufacturer(name="toky", address="tokyo")
manufacturer2 = Manufacturer(name="kana", address="kanagawa")
session.add_all([manufacturer1, manufacturer2])
session.commit()

product1 = Product(name="チョコ", cost=100, manufacturer_id=1)
product2 = Product(name="ガム", cost=10, manufacturer_id=2)
session.add_all([product1, product2])
session.commit()

# 検索
stmt = select(Product).where(Product.name.in_(["チョコ"]))
products = session.scalars(stmt)
for product in products:
    print("Name = " + str(product.id))

# 検索(Join)
stmt = (
        select(Product)
        .join(Product.manufacturer_id)
        .where(Product.name == "チョコ"))

res = session.scalars(stmt).one()


# https://qiita.com/arkuchy/items/75799665acd09520bed2