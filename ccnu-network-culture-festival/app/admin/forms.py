# coding: utf-8

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField,SelectField
from wtforms.validators import DataRequired,Email,EqualTo


class UserForm(Form):
    username = StringField('用户名', validators=[DataRequired()])
    user_kind=SelectField("用户类型",choices=[('3', '普通用户'), ('1', '协管员'), ('2', '管理员')])
    password = PasswordField('密码', validators=[DataRequired()])
    password2=PasswordField("确认密码",validators=[EqualTo(password)])
    email=StringField("邮箱",validators=[Email(),DataRequired()])
    submit = SubmitField('创建')

