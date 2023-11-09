from flask import render_template, url_for, redirect
from app import app
from app.main.forms import *
from app.email_sender import EmailMessage, EmailSender
from flask_babel import _
from app.main import bp
import logging
# pip install python-dotenv
# pip freeze >requirements.txt


@bp.route('/')
def home():
    form = ContactForm()
    return render_template('index.html', form=form, hero_bg_img=app.config['HERO_BG_IMG_PATH'])


@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        full_name = form.full_name.data
        email = form.email.data
        options = form.options.data
        message = form.message.data
        if full_name and email and options and message:
            email_message = EmailMessage(sender_name=full_name, sender_email=email, subject=options, message=message)
            email_sender = EmailSender(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            try:
                email_sender.send_email(email_message)
                flash(_('Your message has been sent successfully!')), 'success'
                return redirect(url_for('main.message_sent'))
            except Exception as e:
                logging.error(f'Error sending email: {str(e)}')
                flash(_('An error occurred while sending the email. Please try again later.')), 'error'
                return redirect(url_for('main.message_sent'))
    return render_template('index.html', form=form)


@bp.route('/sent')
def message_sent():
    form = ContactForm()
    return render_template('sent-form.html', form=form)


@bp.route('/about')
def about():
    form = ContactForm()
    return render_template('index.html', form=form)


@bp.route('/features')
def features():
    form = ContactForm()
    return render_template('index.html', form=form)