from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.ext.declarative import declared_attr, declarative_base

from conf import DB_URL


engine = create_engine(DB_URL)


class Base:
    @declared_attr
    def __tablename__(cls):
        return f'blog_{cls.__name__.lower()}'

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


Base = declarative_base(cls=Base, bind=engine)
