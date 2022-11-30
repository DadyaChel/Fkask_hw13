from flask_wtf import FlaskForm
import wtforms as ws


class TransactionsForm(FlaskForm):
    period = ws.StringField('period')
    value = ws.IntegerField('value')
    status = ws.StringField('status')
    unit = ws.StringField('unit')
    subject = ws.StringField('subject')


class UserForm(FlaskForm):
    username = ws.StringField('Имя пользователя', validators=[
        ws.validators.DataRequired(),
        ws.validators.Length(min=4, max=20)
    ])
    password = ws.PasswordField('Пароль', validators=[
        ws.validators.DataRequired(),
        ws.validators.Length(min=8, max=24)
    ])

