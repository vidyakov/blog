from models.base import Base
from models.session import Session as s
from models import Admin, Post, Tag


def create_tables():
    Base.metadata.create_all()


def create_admin(name: str, email: str, password: str):
    s.add(Admin(name, email, password))
    s.commit()


def create_tags(names: [str]):
    for name in names:
        s.add(Tag(name))
    s.commit()


def create_posts(posts: [int, str, str]):
    tag = s.query(Tag).filter_by(name='Истории').one()
    for post in posts:
        post = Post(*post)
        post.tags.append(tag)
        s.add(post)
    s.commit()


if __name__ == '__main__':
    create_tables()
    create_admin('nastya', 'nastya@gmail.com', 'qwerty')
    create_tags(['ЖурФАК', 'Записки', 'Истории'])
    create_posts([
        [1, 'Леха', 'Рыжий леха', 'img/post1.jpeg'],
        [1, 'Саня', 'Крутой саня', 'img/post2.jpeg'],
        [1, 'Настя', 'Любимая Настенька', 'img/post3.jpeg']
    ])
