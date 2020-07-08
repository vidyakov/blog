from models import Session, Post, Tag


def get_post_by_id(post_id: int) -> Post or None:
    return Session.query(Post).filter_by(id=post_id).one_or_none()


def get_latest_posts() -> [Post, ]:
    return Session.query(Post).all()


def get_category_by_id(category_id: int) -> Tag or None:
    return Session.query(Tag).filter_by(id=category_id).one_or_none()


def get_latest_posts_by_tag(category_id: int) -> [Post, ]:
    tag = get_category_by_id(category_id)
    return tag.posts


def get_all_tags() -> [Tag, ]:
    return Session.query(Tag).all()
