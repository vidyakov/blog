from sqlalchemy import (
    Column, Integer,
    ForeignKey, String,
    Text, Table,
    Date
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .base import Base
from .users import Admin


posts_tags_table = Table(
    'posts_tags',
    Base.metadata,
    Column('post_id', Integer, ForeignKey('blog_post.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('blog_tag.id'), primary_key=True)
)


class Post(Base):
    admin_id = Column(Integer, ForeignKey(Admin.id), nullable=False)
    title = Column(String(256), nullable=False)
    text = Column(Text, nullable=False)
    img = Column(Text, nullable=False)
    date = Column(Date, server_default=func.now())

    def __init__(self, admin_id, title, text, img):
        self.admin_id = admin_id
        self.title = title
        self.text = text
        self.img = img

    user = relationship(Admin, back_populates='posts')
    tags = relationship('Tag', secondary=posts_tags_table, back_populates='posts')

    def __str__(self):
        return f'{self.__class__.__name__}({self.title[:30]}, )'


class Tag(Base):
    name = Column(String(16), nullable=False, unique=True)

    def __init__(self, name):
        self.name = name

    posts = relationship(Post, secondary=posts_tags_table, back_populates='tags')

    def __str__(self):
        return f'{self.__class__.__name__}({self.name})'
