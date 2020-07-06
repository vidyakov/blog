from hashlib import sha512

from sqlalchemy import (
    Column, String
)
from sqlalchemy.orm import relationship
from flask_login import UserMixin

from .base import Base


class Admin(Base, UserMixin):
    name = Column(String(64), nullable=False, unique=True)
    email = Column(String(256), nullable=False, unique=True)
    _password = Column(String, nullable=False)
    posts = relationship('Post', back_populates='user')

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password: str):
        self._password = self.hash_password(password)

    @staticmethod
    def hash_password(password: str) -> str:
        return sha512(password.encode('utf-8')).hexdigest()

    def __str__(self):
        return f'{self.__class__.__name__}({self.name}, )'
