from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

from services.posts import get_latest_posts
from services.auth import valid_auth_form, save_new_user, valid_register_form


admin_app = Blueprint('admin', __name__)


@admin_app.route('/', methods=['GET', 'POST'], endpoint='panel')
def admin_panel():
    if not current_user.is_authenticated:
        return redirect(url_for('admin.login'))
    return render_template('admin/admin_panel.html', admin=current_user, posts=get_latest_posts())


@admin_app.route('/login/', methods=['GET', 'POST'], endpoint='login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.panel'))

    if request.method == 'GET':
        return render_template('admin/auth.html')

    if user := valid_auth_form(request.form):
        login_user(user)
        return redirect(url_for('admin.panel'))
    return render_template('admin/auth.html', error='Пользателя с таким логином и паролем не существует')


@admin_app.route('/register/', methods=['GET', 'POST'], endpoint='register')
@login_required
def register():
    if request.method == 'GET':
        return render_template('admin/register.html')
    if error := valid_register_form(request.form):
        return render_template('admin/register.html', error=error)

    save_new_user(request.form)
    return redirect(url_for('admin.panel'))


@admin_app.route('/logout/', methods=['GET', 'POST'], endpoint='logout')
def logout():
    logout_user()
    return redirect(url_for('pages_app.index'))
