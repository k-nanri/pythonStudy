from sqlmodel import Field, SQLModel, Session, create_engine, select


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


hero_1 = Hero(name="test1", secret_name="hoge1")
hero_2 = Hero(name="test2", secret_name="hoge2")
hero_3 = Hero(name="test3", secret_name="hoge3")

url = "postgresql://postgres:example@localhost:5432/postgres"
engine = create_engine(url, echo=True)

SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.commit()

with Session(engine) as session:
    statement = ""

with Session(engine) as session:
    statement = select(Hero).where(Hero.name == "test3").with_for_update(nowait=True)
    hero = session.exec(statement).first()
    print(hero)
