from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:example@localhost:5432/postgres")
Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    age = Column(Integer)

    def full_name(self):
        return "{self.first_name} {self.last_name}"
    
Base.metadata.create_all(engine)
SessionClass = sessionmaker(engine)
session = SessionClass()

user_a = User(first_name="tanaka", last_name="hoge", age=30)
session.add(user_a)
session.commit()

users = session.query(User).all()
print(users[0].first_name)