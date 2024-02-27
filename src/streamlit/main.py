import streamlit as st

from sqlalchemy import create_engine
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import sessionmaker
import datetime

class Base(DeclarativeBase):
    pass

class Moviequestionnaire(Base):
    __tablename__ = "movie_questionnaire"

    time: Mapped[datetime.datetime] = mapped_column(DateTime, primary_key=True, nullable=False)
    gender: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    frequency_show: Mapped[str] = mapped_column(String, nullable=False)
    good_movie: Mapped[int] = mapped_column(Integer, nullable=False)

# DBエンジンを作成
url = "postgresql://postgres:example@localhost:5432/postgres"
engine = create_engine(url, echo=True)
# セッションの作成
SessionClass = sessionmaker(engine)
session = SessionClass()


with st.form("my_form"):
    st.title("Let's try!!!")
    gender = st.radio("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=20, max_value=60, format="%d")
    frequency_show = st.radio('映画はよく見ますか？', ["月5回以上", "月1回", "半年に1回", "見ない"])
    good_movie = st.slider("今回の映画の評価を教えてください(0-5)", 0, 5, 0)

    submitted = st.form_submit_button("送信")
    if submitted:
        movie_questionnaire = Moviequestionnaire(time=datetime.datetime.now(),
                                                 gender=gender,
                                                 age=age,
                                                 frequency_show=frequency_show,
                                                 good_movie=good_movie)
        session.add(movie_questionnaire)
        session.commit()





