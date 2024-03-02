from ulid import ULID
import datetime
import uuid
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import uuid

class Base(DeclarativeBase):
    pass

class UUID_Sample(Base):
    __tablename__ = 'uuid_sample'

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)

# DBエンジンを作成
url = "postgresql://postgres:example@localhost:5432/postgres"
engine = create_engine(url, echo=False)

# テーブルをDBに作成
Base.metadata.create_all(engine)
SessionClass = sessionmaker(engine)
session = SessionClass()

def use_db():
    
    # 日時指定で1日ずらして、ULIDオブジェクトを生成
    specfic_datetime = datetime.datetime.strptime("2023-03-02 18:00:00 +0000", "%Y-%m-%d %H:%M:%S %z")
    ulid1 = ULID.from_datetime(specfic_datetime).to_uuid()
    print("ulid1 = " + str(ulid1))
    ulid1_obj = UUID_Sample(id=ulid1)

    specfic_datetime = datetime.datetime.strptime("2023-03-03 18:00:00 +0000", "%Y-%m-%d %H:%M:%S %z")
    ulid2 = ULID.from_datetime(specfic_datetime).to_uuid()
    print("ulid2 = " + str(ulid2))
    ulid2_obj = UUID_Sample(id=ulid2)

    specfic_datetime = datetime.datetime.strptime("2023-03-04 18:00:00 +0000", "%Y-%m-%d %H:%M:%S %z")
    ulid3 = ULID.from_datetime(specfic_datetime).to_uuid()
    print("ulid3 = " + str(ulid3))
    ulid3_obj = UUID_Sample(id=ulid3)

    specfic_datetime = datetime.datetime.strptime("2023-03-05 18:00:00 +0000", "%Y-%m-%d %H:%M:%S %z")
    ulid4 = ULID.from_datetime(specfic_datetime).to_uuid()
    print("ulid4 = " + str(ulid4))
    ulid4_obj = UUID_Sample(id=ulid4)
    session.add_all([ulid2_obj, ulid4_obj, ulid1_obj, ulid3_obj])
    session.commit()

    # 整列した順番のリストを作成
    expected_list = list()
    expected_list.append(ulid1)
    expected_list.append(ulid2)
    expected_list.append(ulid3)
    expected_list.append(ulid4)

    stmt = select(UUID_Sample)
    results = session.scalars(stmt)
    print("Not use order by")
    i = 0
    for result in results:
        print("id = " + str(result.id))
        print("Is Sample = " + str(result.id == expected_list[i]))
        i += 1

    print("Use order by")
    stmt = select(UUID_Sample).order_by(UUID_Sample.id)
    results = session.scalars(stmt)
    i = 0
    for result in results:
        print("id = " + str(result.id))
        print("Is Sample = " + str(result.id == expected_list[i]))
        i += 1

def execute():
    # 現在のタイムスタンプからULIDオブジェクトを生成
    ulid = ULID()
    print("ULID = " + str(ulid))

    # 2023-03-02 18:00:00 からULIDオブジェクトを生成
    specfic_datetime = datetime.datetime.strptime("2023-03-02 18:00:00 +0000", "%Y-%m-%d %H:%M:%S %z")
    ulid = ULID.from_datetime(specfic_datetime)
    print("ULID = " + str(ulid))

    # ulidに含まれる日時を確認
    print("Datetime = " + ulid.datetime.strftime('%Y-%m-%d %H:%M:%S'))

    # UUIDに変換
    uuid_from_ulid = ulid.to_uuid()
    print("UUID = " + str(uuid_from_ulid))

    # UUIDからulidを生成
    ulid2 = ULID.from_uuid(uuid.uuid4())
    print("ULID from uuid = " + str(ulid2))
    print(ulid2.datetime)

def sort_execute():
    
    # 日時指定で1日ずらして、ULIDオブジェクトを生成
    specfic_datetime = datetime.datetime.strptime("2023-03-02 18:00:00 +0000", "%Y-%m-%d %H:%M:%S %z")
    ulid1 = ULID.from_datetime(specfic_datetime).to_uuid()
    print("ulid1 = " + str(ulid1))

    specfic_datetime = datetime.datetime.strptime("2023-03-03 18:00:00 +0000", "%Y-%m-%d %H:%M:%S %z")
    ulid2 = ULID.from_datetime(specfic_datetime).to_uuid()
    print("ulid2 = " + str(ulid2))

    specfic_datetime = datetime.datetime.strptime("2023-03-04 18:00:00 +0000", "%Y-%m-%d %H:%M:%S %z")
    ulid3 = ULID.from_datetime(specfic_datetime).to_uuid()
    print("ulid3 = " + str(ulid3))

    specfic_datetime = datetime.datetime.strptime("2023-03-05 18:00:00 +0000", "%Y-%m-%d %H:%M:%S %z")
    ulid4 = ULID.from_datetime(specfic_datetime).to_uuid()
    print("ulid4 = " + str(ulid4))

    # 整列した順番のリストを作成
    expected_list = list()
    expected_list.append(ulid1)
    expected_list.append(ulid2)
    expected_list.append(ulid3)
    expected_list.append(ulid4)

    # 順番をばらばらにしたリストを作成
    list_ulid = list()
    list_ulid.append(ulid2)
    list_ulid.append(ulid4)
    list_ulid.append(ulid1)
    list_ulid.append(ulid3)

    # 整列した順番のリストとばらばらなリストを比較
    print("Before = " + str(list_ulid))
    print("Is Same = " + str(expected_list == list_ulid))

    # ソート後にソートしたリストと整列した順番のリストを比較
    sorted_list = sorted(list_ulid)
    print("After  = " + str(sorted_list))
    print("Is Same = " + str(expected_list == sorted_list))


    
    

if __name__ == '__main__':
    #execute()
    #sort_execute()
    use_db()