import os
import secrets
from PIL import Image
from flask import url_for, current_app
from justsmthpy import mail
from flask_mail import Message


def save_picture(form_picture):
    # TODO add deleting previous picture
    random_hex = secrets.token_hex(8)
    _, file_extension = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + file_extension
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_filename)
    output_size = (150, 150)
    image = Image.open(form_picture)
    image.thumbnail(output_size)
    image.save(picture_path)
    return picture_filename


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='anastas.ego@gmail.com', recipients=[user.email])
    msg.body = f'''
    To reset your password, visit the following link: {url_for('users.reset_token', token=token, _external=True)}
    If you did not make this request blah blah
    '''
    mail.send(msg)
