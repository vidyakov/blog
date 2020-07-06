from flask import Flask
from flask_login import LoginManager

from views.pages import pages_app
from views.admin import admin_app

from models.users import Admin
from models.session import Session


app = Flask(__name__)

app.config.from_pyfile('conf.py')

login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(pages_app)
app.register_blueprint(admin_app, url_prefix='/admin')


@login_manager.user_loader
def load_user(admin_id):
    return Session.query(Admin).filter_by(id=admin_id).one_or_none()


@app.teardown_request
def remove_session(*args):
    Session.remove()


if __name__ == '__main__':
    app.run()
