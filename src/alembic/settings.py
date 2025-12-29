from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

path = "postgresql://postgres:example@localhost:5432/postgres"

Engine = create_engine(path, echo=True)

Base = declarative_base()
