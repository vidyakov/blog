import re

from models import Session, Admin


VALIDATION_ERRORS = {
    'name_unique': 'Пользователь с таким именем уже существует',
    'email_unique': 'Пользователь с такой почтой уже существует',
    'password_length': 'Слишком маленький пароль',
    'password': 'Ваш пароль слишком похож на что-то)'
}


def get_form_data(form: dict, *args):
    return [form.get(item) for item in args]


def valid_auth_form(form: dict) -> Admin or None:
    """If the user enters correct email and password, the func will return the user object.
    Otherwise the function will return None.
    """
    email, password = get_form_data(form, 'email', 'password')
    user = Session.query(Admin).filter_by(email=email).one_or_none()
    if user and user.password == Admin.hash_password(password):
        return user


def valid_register_form(form: dict) -> str or None:
    name, email, password = get_form_data(form, 'name', 'email', 'password')
    if Session.query(Admin).filter_by(name=name).one_or_none():
        return VALIDATION_ERRORS['name_unique']
    if Session.query(Admin).filter_by(email=email).one_or_none():
        return VALIDATION_ERRORS['email_unique']
    if len(password) < 6:
        return VALIDATION_ERRORS['password_length']
    if re.search(password.lower(), name + email):
        return VALIDATION_ERRORS['password']


def save_new_user(form: dict):
    data = get_form_data(form, 'name', 'email', 'password')
    new_admin = Admin(*data)
    Session.add(new_admin)
    Session.commit()
