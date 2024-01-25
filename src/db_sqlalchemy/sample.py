from sqlalchemy import create_engine
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

# モデルベースクラスを作成
#Base = declarative_base() と同等(2.0から)
class Base(DeclarativeBase):
    pass

# モデルベースを拡張して、ORMのデータクラスを作成
# mapped_columnは2.0からの新機能
class Product(Base):
    __tablename__ = "product"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    cost: Mapped[int] = mapped_column(Integer, nullable=False)
   


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
product1 = Product(name="チョコ", cost=100)
product2 = Product(name="ガム", cost=10)
session.add_all([product1, product2])
session.commit()

# 検索
stmt = select(Product).where(Product.name.in_(["チョコ"]))
products = session.scalars(stmt)
for product in products:
    print("Name = " + str(product.name))

# 変更
stmt = select(Product).where(Product.id == 1)
product = session.scalars(stmt).one()
product.name = "パン"
session.commit()

# 検索
stmt = select(Product)
products = session.scalars(stmt)
for product in products:
    print("Name = " + str(product.name))

# 削除



# https://qiita.com/arkuchy/items/75799665acd09520bed2