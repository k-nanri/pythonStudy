from sqlalchemy import create_engine
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import select


class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "student"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    school_id: Mapped[int] = mapped_column(ForeignKey("school.id"))
    school: Mapped["School"] = relationship()


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
#Base.metadata.create_all(engine)

# セッションを作成
# セッションを介してクエリを実行する
SessionClass = sessionmaker(engine)
session = SessionClass()

school1 = School(name="あいうえお学園")
school2 = School(name="かきくけこ学園")
school3 = School(name="さしすせそ学校")
session.add_all([school1, school2, school3])
session.commit()
student1 = Student(name="sato", school_id=1)
student2 = Student(name="tanaka", school_id=2)
student3 = Student(name="watanabe", school_id=3)
session.add_all([student1, student2, student3])
session.commit()

# relationshipの設定をしていない場合はこれで操作できる
stmt = select(Student, School).join(School, Student.school_id == School.id).where(Student.id == 1)
results = session.scalars(stmt)

for result in results:
    print("student.id = " + str(result.id))
    print("student.name = " + str(result.name))
    print("student.school_id = " + str(result.school_id))
    print("student.school.id = " + str(result.school.id))
    print("student.school.name = " + str(result.school.name))

# https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html#joins
# https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html
