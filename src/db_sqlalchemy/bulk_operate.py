
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import String, Text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert, update


class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "student"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    address: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255))

url = "postgresql://postgres:example@localhost:5432/postgres"
engine = create_engine(url, echo=True)
# テーブルをDBに作成
Base.metadata.create_all(engine)
session_class = sessionmaker(engine)
session = session_class()

# Insert
students = list()
students.append(Student(name="sato", address="Tokyo", email="sato@ddd.com"))
students.append(Student(name="tanaka", address="Kanagawa", email="tanaka@ddd.com"))
students.append(Student(name="wata", address="Chiba", email="wata@ddd.com"))

# add_allでbulk insertができる
#session.add_all(students)
#session.commit()

# これだとInsert後の結果が取れない。（検索処理が必要）
session.execute(
    insert(Student),
    [
        {"name": "sato", "address": "Tokyo", "email": "sato@ddd.com"},
        {"name": "tanaka", "address": "Kanagawa", "email": "tanaka@ddd.com"},
        {"name": "wata", "address": "Chiba", "email": "wata@ddd.com"}
    ]
)
session.commit()

# TODO
# scalars
# Execute a statement and return the results as scalars.
# ステートメントを実行し、結果をスカラーとして返します。
# スカラーって何？

students = session.scalars(
    insert(Student).returning(Student, sort_by_parameter_order=True),
    [
        {"name": "sato", "address": "Tokyo", "email": "sato@ddd.com"},
        {"name": "tanaka", "address": "Kanagawa", "email": "tanaka@ddd.com"},
        {"name": "wata", "address": "Chiba", "email": "wata@ddd.com"}
    ]
)
session.commit()
for student in students:
    print("id = " + str(student.id) + ", name = " + student.name)

# TODO エラー
students = session.scalars(
    update(Student).returning(students),
    [
        {"id": 1, "name": "sato2"},
        {"id": 2, "name": "tanaka2"},
        {"id": 3, "name": "wata2"}
    ]
)
session.commit()
for student in students:
    print("id = " + str(student.id) + ", name = " + student.name + ", email = " + student.email)
