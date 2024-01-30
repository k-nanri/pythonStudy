from sqlalchemy import create_engine
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import select


class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "student"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    school_id: Mapped[int]


    def __str__(self):
        return "id = " + str(self.id) + ", name = " + str(self.name) + ", school_id = " + str(self.school_id)

class School(Base):
    __tablename__ = "school"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))


# DBエンジンを作成
url = "postgresql://postgres:example@localhost:5432/postgres"
engine = create_engine(url, echo=True)

# テーブルをDBに作成
Base.metadata.create_all(engine)

# セッションを作成
# セッションを介してクエリを実行する
SessionClass = sessionmaker(engine)
session = SessionClass()

school = School(name="hoge")
session.add(school)
session.commit()
student = Student(name="tanaka", school_id=1)
session.add(student)
session.commit()

# relationshipの設定をしていない場合はこれで操作できる
stmt = select(Student.id, Student.name, School.name).join(School, Student.school_id == School.id)
print(stmt)
#results = session.scalars(stmt)
results = session.execute(stmt).mappings().all()
for result in results:
    print(result)

# https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html#joins
# https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html
