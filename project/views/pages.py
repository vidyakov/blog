from flask import Blueprint, render_template

from services.posts import (
    get_latest_posts, get_post_by_id,
    get_category_by_id,
    get_latest_posts_by_tag
)


pages_app = Blueprint('pages_app', __name__)


@pages_app.route('/', methods=['GET'], endpoint='index')
def index_page():
    return render_template('pages/index.html', posts=get_latest_posts())


@pages_app.route('/about_me/', methods=['GET'], endpoint='about_me')
def contact_page():
    return render_template('pages/about_me.html')


@pages_app.route('/category/<int:category_id>', methods=['GET'], endpoint='category')
def category_page(category_id):
    if category := get_category_by_id(category_id):
        posts = get_latest_posts_by_tag(category)
        return render_template('pages/category.html', category=category, posts=posts)

    error = {'code': 404, 'text': 'Такой категории не существует'}
    return render_template('pages/error.html', error=error), 404


@pages_app.route('/post/<int:post_id>', methods=['GET'], endpoint='post')
def post_page(post_id):
    if post := get_post_by_id(post_id):
        return render_template('pages/post.html', post=post)

    error = {'code': 404, 'text': 'Поста не существует'}
    return render_template('pages/error.html', error=error), 404